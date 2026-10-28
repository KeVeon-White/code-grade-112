from pathlib import Path
from typing import Optional

from cg112.helpers import *
from cg112.feedback import *

class Grader():
    def __init__(self, assignment_name: str, files: List[str], assignment_file_name: str, hex_value: str, no_error_weight: float, *args, **kwargs):
        self.assignment_name: str = assignment_name
        self.assignment_file_name: str = assignment_file_name
        fp: Optional[Path] = get_files(
            files, 
            [self.assignment_file_name]
            ).get(self.assignment_file_name)

        self.rubric_categories: List[RubricCategory] = []
        self.rubric_feedback: RubricFeedback = RubricFeedback(
            self.assignment_name,
            fp,
            []
        )

        if not self.validate(fp):
            print_err(f"Invalid grader object. File was not found for {self.assignment_file_name}.")
            return

        if not fp:
            return
        
        self.assignment_file: Path = fp
        
        if not self.check_hex(hex_value):
            print_err(f"Invalid grader object. File does not contain proper hex value.")
            return
        
        self.check_error_free(no_error_weight)
        self.grade()
        self.make_feedback()

    
    def validate(self, fp: Optional[Path]) -> bool:
        if not fp:
            return False
        return True

    def check_hex(self, hex_value: str) -> bool:
        def helper() -> bool:
            proc_out: Optional[str] = get_subprocess_output(f'grep -i -c "{hex_value}" {self.assignment_file}')
            if not proc_out: return False
    
            try:
                return int(proc_out) > 0
            except ValueError:
                return False

        name = "Check for Secret Hex Value"
        weight = -9001.0
        description = "Check the script for the secret hex value as a check of authenticity."
    
        res: bool = helper()
        self.rubric_categories.append(RubricCategory(
            name, weight, 
            weight if not res else 0.0,
            description,
            "[red]The secret hex value was NOT found. \
                As a result, the maximum possible score possible is a 0 on the assignments." \
                if not res else \
                "[green]The secret hex value was found."
        ))

        return res

    def check_error_free(self, weight: float) -> bool:
        def helper() -> bool:
            proc_out: Optional[str] = get_subprocess_output(
f"""
python3 -m py_compile {self.assignment_file} 2> error.msg

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
        self.rubric_categories.append(RubricCategory(
            "Script Runs without Error", weight, weight if res else 0,
            "Check if the script runs without error.",
            "[red]The script encountered errors. " \
                "Run the program normally (without this tool) to examine those errors." if not res \
                else "[green]The script runs without error."
        ))
        return res

    def make_feedback(self):
        self.rubric_feedback = RubricFeedback(
            self.assignment_name,
            self.assignment_file,
            self.rubric_categories
        )

    def grade(self):
        ...

class GraderValidationException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
