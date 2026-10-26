from typing import Any, Callable, Dict, List, Optional, Union
from pathlib import Path
import re, subprocess

from cg112.feedback import RubricCategory
from cg112.styling import *

ID_NAME_RAW_PATTERN: str = r"[_a-zA-Z][0-9a-zA-Z_]*:? ?\w*"
#r"[_a-zA-Z]\w*:?? ??\w*?"

file_cache: Dict[Path, str] = {}

def get_subprocess_output(arg: str) -> Optional[str]:
    proc: subprocess.Popen[bytes] = subprocess.Popen(arg, stdout=subprocess.PIPE, shell=True)
    output: str = ""
    if (out := proc.stdout) and out:
        output = out.read().decode()
    return output

def str_to_path(file_path: str) -> Path:
    if isinstance(file_path, str):
        return Path(file_path).resolve()

def resolve_file(file_path: Union[str, Path]) -> Path:
    fp: Path
    if isinstance(file_path, str):
        fp = str_to_path(file_path)
    else:
        fp = file_path.resolve()

    return fp

def check_secret_hex(file_path: Union[str, Path], hex_value: str) -> RubricCategory:
    def helper() -> bool:
        fp = resolve_file(file_path)
        if not fp.exists():
            print("File not found")
            return False
        
        proc_out: Optional[str] = get_subprocess_output(f'grep -i -c "{hex_value}" {fp}')
        if not proc_out: return False

        try:
            return int(proc_out) > 0
        except ValueError:
            return False

    name = "Check for Secret Hex Value"
    weight = -9001.0
    description = "Check the script for the secret hex value as a check of authenticity."

    res: bool = helper()
    return RubricCategory(
        name, weight, 
        weight if not res else 0.0,
        description,
        "[red]The secret hex value was NOT found. \
            As a result, the maximum possible score possible is a 0 on the assignments." \
            if not res else \
            "[green]The secret hex value was found."
    )

def script_runs_without_error(file_path: Union[str, Path], weight: float) -> RubricCategory:
    def helper() -> bool:
        fp = resolve_file(file_path)
        if not fp.exists():
            print("File not found")
            return False
        proc_out: Optional[str] = get_subprocess_output(
f"""
python3 -m py_compile {fp} 2> error.msg

if [ -s error.msg ]; then    # if file is NOT empty
    echo 0
else
    echo 1
fi

rm error.msg
""")
        if not proc_out: return False
        try:
            return int(proc_out) == 1
        except ValueError:
            return False

    res: bool = helper()
    return RubricCategory(
        "Script Runs without Error", weight, weight if res else 0,
        "Check if the script runs without error.",
        "[red]The script encountered errors. " \
            "Run the program normally (without this tool) to examine those errors." if not res \
            else "[green]The script runs without error."
    )

def generic_grep(pattern: str, file_path: Union[str, Path]) -> bool:
    """Grep the file."""
    def helper() -> bool:
        fp = resolve_file(file_path)
        if not fp.exists():
            print("[yellow]File not found")
            return False
        proc_out: Optional[str] = get_subprocess_output(f'grep -i -c "{pattern}" {fp}')
        if not proc_out: return False
        try:
            return int(proc_out) > 0
        except ValueError:
            return False
        
    return helper()

def generic_re(pattern: str, file_path: Union[str, Path]) -> bool:
    """Regex the file."""
    fp = resolve_file(file_path)
    if not fp.exists():
        print("[yellow]File not found")
        return False
    re_pattern: re.Pattern = re.compile(pattern)

    file_contents: str = file_cache.get(fp, "")

    if file_contents == "":
        with open(fp) as fh:
            file_contents = fh.read()
        file_cache[fp] = file_contents
    re_match: Optional[re.Match] = re_pattern.search(file_contents)

    return re_match is not None

def generic_semgrep(pattern: str, file_path: Union[str, Path]) -> bool:
    """Semgrep the file."""
    fp = resolve_file(file_path)
    if not fp.exists():
        print("[yellow]File not found")
        return False
    file_contents: str = ""
    with open(fp) as fh:
        file_contents = fh.read()
    
    placeholders = list(
        map(
            lambda tos : tos[0] if isinstance(tos, tuple) else tos,
            filter(lambda g : "$" in  g[0], re.findall(fr"(\${ID_NAME_RAW_PATTERN})", pattern))))
    
    new_pattern = pattern
    if len(placeholders) > 0:
        for ph in set(placeholders):
            new_pattern = new_pattern.replace(ph, f"({ID_NAME_RAW_PATTERN})")

        re_pattern: re.Pattern = re.compile(new_pattern)
        
        re_match: Optional[re.Match] = re_pattern.search(file_contents)
        
        if not re_match:
            return False

        placeholder_var_dict: dict[str, str] = {}
        for i, group in enumerate(re_match.groups()):
            var = group.split(":")[0].strip()
            placeholder = placeholders[i]

            if placeholder in placeholder_var_dict.keys():
                if var != placeholder_var_dict.get(placeholder):
                    print(var, placeholder_var_dict.get(placeholder))
                    return False
            else:
                placeholder_var_dict[placeholder] = var

    if "..." in new_pattern:
        pass

    return True

def get_files(files: List[str], names: List[str]) -> Dict[str, Optional[Path]]:
    ret: Dict[str, Optional[Path]] = {}
    for file in files:
        fp: Path = Path(file).resolve()
        if not fp.exists():
            print_warning(f"File not found (skipping): {file}")
            continue
        file_found: bool = False
        for name in names:
            if fp.name == name:
                ret[fp.name] = fp
                file_found = True
        if not file_found:
            print_warning(f"File not recognized (skipping): {file}")
    return ret

