from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from pathlib import Path
import re, subprocess

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
        fp = str_to_path(file_path).resolve()
    else:
        fp = file_path.resolve()

    return fp

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
    
    file_contents: str = file_cache.get(fp, "")
    if file_contents == "":
        with open(fp) as fh:
            file_contents = fh.read()
        file_cache[fp] = file_contents
    
    placeholders = list(
        map(
            lambda tos : tos[0] if isinstance(tos, tuple) else tos,
            filter(lambda g : "$" in  g[0], re.findall(fr"(\${ID_NAME_RAW_PATTERN})", pattern))))
    
    new_pattern = pattern

    if "..." in new_pattern:
        new_pattern = new_pattern.replace("...", r"(?:.|\s)*")

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

    return True

def generic_io_test(file_path: Union[str, Path], cmds: List[str], inputs: List[str], outputs: List[str]) -> List[Tuple[bool, str, str]]:
    """
    Returns matches of IO from commands.

    Parameters
    ----------
    file_path : Union[str, Path]
        The file path (as a str or Path object) to run IO tests on.

    cmds : List[str]
        The commands to run in which to test IO on.

    inputs : List[str]
        The inputs to run on every iteration of commands.

    outputs : List[str]
        The expected output from each command run.

    Returns
    -------
    : List[Tuple[bool, str, str]]
        A list of tuples corresponding to each run command where the 3-tuple is (success, expected, actual)
    """
    if len(cmds) != len(outputs):
        print_err("The length of commands must be the same as the length of outputs.")
        return []

    fp, file_contents = get_file_and_contents(file_path)
    if not file_contents:
        return []

    ret: List[Tuple[bool, str, str]] = []
    tmp_file: Path = Path(__file__).parent / 'tmp.py'
    input_file: Path = Path(__file__).parent / "inputs.txt"

    with open(tmp_file, "w") as writer:
        writer.write(file_contents)
    with open(input_file, "w") as writer:
        writer.write("\n".join(inputs))

    for i, cmd in enumerate(cmds):
        expected: str = outputs[i]
        actual: Optional[str] = get_subprocess_output(f"python3 -c \"from cg112.tmp import *; {cmd}\" << {input_file}")

        if actual and actual.endswith("\n"):
            actual = actual[:-1]
        
        ret.append(
            (expected == actual, expected, actual or "")
        )

    tmp_file.unlink(True)
    input_file.unlink(True)

    return ret

def score_io_test(test: List[Tuple[bool, str, str]], weight: float) -> float:
    weight_per: float = weight / len(test)
    return weight_per * len(list(filter(lambda item : item[0], test)))

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

def get_file_and_contents(file_path: Union[str, Path]) -> Tuple[Path, Optional[str]]:
    fp = resolve_file(file_path)
    if not fp.exists():
        print("[yellow]File not found")
        return (fp, None)
    
    file_contents: str = file_cache.get(fp, "")
    if file_contents == "":
        with open(fp) as fh:
            file_contents = fh.read()
        file_cache[fp] = file_contents

    return (fp, file_contents)
