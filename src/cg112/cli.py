import typer

from pathlib import Path
from rich.console import Console
from typing import Dict, Iterable, List, Optional

from cg112 import __app_name__, __version__
from cg112.helpers import *
from cg112.feedback import AssignmentFeedback, RubricFeedback, RubricCategory
from cg112.styling import err_style, warn_style, print_err, print_warning

from cg112.graders.lesson02.random_number_v2 import grade_random_number_v2
from cg112.graders.lesson02.rock_paper_scissors_v1 import grade_rock_paper_scissors_v1

from cg112.graders.lesson03.random_number_v3 import grade_random_number_v3
from cg112.graders.lesson03.rock_paper_scissors_v2 import grade_rock_paper_scissors_v2

from cg112.graders.lesson04.computer_specs_v2 import grade_computer_specs_v2
from cg112.graders.lesson04.inventory_management_v1 import grade_inventory_management_v1

from cg112.graders.lesson05.string_reversal import grade_string_reversal

app = typer.Typer()
console = Console()
base_dir = Path(__file__).parent.parent.parent.resolve()

def file_autocompletion(incomplete: str) -> List[str]:
    dir: Path = Path(incomplete).resolve()
    while not dir.exists() or not dir.is_dir():
        dir = dir.parent.resolve()
    files: Iterable[str] = map(lambda p : str(p), dir.iterdir())

    return list(filter(lambda f : f.startswith(incomplete), files))

generic_files_argument: List[str] = typer.Argument(
    [], autocompletion=file_autocompletion,
    help="Files to be graded.")
generic_verbose_argument: bool = typer.Option(
    False,
    "--verbose",
    "-v",
    help="Shows the rubric criteria in addition to point values.",)

def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback(no_args_is_help=True)
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    return

@app.command(help="Grade lesson 01 deliverable(s).")
def lesson01(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    console = Console()
    console.rule("Lesson 01 Submission Grading")
    console.print("No submission to grade.", style="red underline", justify="center")

@app.command(help="Grade lesson 02 deliverable(s).")
def lesson02(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    random_number_v2_file_name: str = "random_number_v2.py"
    rock_paper_scissors_v1_file_name: str = "rock_paper_scissors_v1.py"

    found_files: Dict[str, Optional[Path]] = get_files(files, [random_number_v2_file_name, rock_paper_scissors_v1_file_name])

    random_number_v2: Optional[Path] = found_files.get(random_number_v2_file_name)
    rock_paper_scissors_v1: Optional[Path] = found_files.get(rock_paper_scissors_v1_file_name)

    random_number_v2_rubric_categories: List[RubricCategory] = []
    rock_paper_scissors_v1_rubric_categories: List[RubricCategory] = []

    #region Random Number version 2
    if not random_number_v2:
        print_err(f"No file found for {random_number_v2_file_name}")
    else:
        random_number_v2_rubric_categories = grade_random_number_v2(random_number_v2)

    random_number_v2_rubric_feedback: RubricFeedback = RubricFeedback(
        "Random Number v2", 
        random_number_v2,
        random_number_v2_rubric_categories)
    #endregion

    #region Rock Paper Scissors version 1
    if not rock_paper_scissors_v1:
        print_err(f"No file found for {rock_paper_scissors_v1_file_name}")
    else:
        rock_paper_scissors_v1_rubric_categories = grade_rock_paper_scissors_v1(rock_paper_scissors_v1)

    rock_paper_scissors_v1_rubric_feedback: RubricFeedback = RubricFeedback(
        "Rock, Paper, Scissors v1",
        rock_paper_scissors_v1,
        rock_paper_scissors_v1_rubric_categories
    )
    #endregion

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        random_number_v2_rubric_feedback, rock_paper_scissors_v1_rubric_feedback
    ])

    assignment_feedback.console_print(console, verbose)    

@app.command(help="Grade lesson 03 deliverable(s).")
def lesson03(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    random_number_v3_file_name: str = "random_number_v3.py"
    rock_paper_scissors_v2_file_name: str = "rock_paper_scissors_v2.py"

    found_files: Dict[str, Optional[Path]] = get_files(files, [random_number_v3_file_name, rock_paper_scissors_v2_file_name])

    random_number_v3: Optional[Path] = found_files.get(random_number_v3_file_name)
    rock_paper_scissors_v2: Optional[Path] = found_files.get(rock_paper_scissors_v2_file_name)

    random_number_v3_rubric_categories: List[RubricCategory] = []
    rock_paper_scissors_v2_rubric_categories: List[RubricCategory] = []

    #region Random Number version 3
    if not random_number_v3:
        print_err(f"No file found for {random_number_v3_file_name}")
    else:
        random_number_v3_rubric_categories = grade_random_number_v3(random_number_v3)

    random_number_v3_rubric_feedback: RubricFeedback = RubricFeedback(
        "Random Number v3",
        random_number_v3,
        random_number_v3_rubric_categories
    )
    #endregion

    #region Rock Paper Scissors version 2
    if not rock_paper_scissors_v2:
        print_err(f"No file found for {rock_paper_scissors_v2_file_name}")
    else:
        rock_paper_scissors_v2_rubric_categories = grade_rock_paper_scissors_v2(rock_paper_scissors_v2)

    rock_paper_scissors_v2_rubric_feedback: RubricFeedback = RubricFeedback(
        "Rock, Paper, Scissors v2",
        rock_paper_scissors_v2,
        rock_paper_scissors_v2_rubric_categories
    )
    #endregion

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        random_number_v3_rubric_feedback, rock_paper_scissors_v2_rubric_feedback])
    
    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 04 deliverable(s).")
def lesson04(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    computer_specs_v2_file_name: str = "computer_specs_v2.py"
    inventory_management_v1_file_name: str = "inventory_management_v1.py"

    found_files: Dict[str, Optional[Path]] = get_files(
        files, [computer_specs_v2_file_name, inventory_management_v1_file_name]
    )

    computer_specs_v2: Optional[Path] = found_files.get(computer_specs_v2_file_name)
    inventory_management_v1: Optional[Path] = found_files.get(inventory_management_v1_file_name)

    computer_specs_v2_rubric_categories: List[RubricCategory] = []
    inventory_management_v1_rubric_categories: List[RubricCategory] = []

    #region Computer Specs version 2
    if not computer_specs_v2:
        print_err(f"No file found for {computer_specs_v2_file_name}")
    else:
        computer_specs_v2_rubric_categories = grade_computer_specs_v2(computer_specs_v2)

    computer_specs_v2_rubric_feedback: RubricFeedback = RubricFeedback(
        "Computer Specifications v2",
        computer_specs_v2,
        computer_specs_v2_rubric_categories
    )
    #endregion

    #region Inventory Management version 1
    if not inventory_management_v1:
        print_err(f"No file found for {inventory_management_v1_file_name}")
    else:
        inventory_management_v1_rubric_categories = grade_inventory_management_v1(inventory_management_v1)

    inventory_management_v1_rubric_feedback: RubricFeedback = RubricFeedback(
        "Inventory Management v1",
        inventory_management_v1,
        inventory_management_v1_rubric_categories
    )
    #endregion

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        computer_specs_v2_rubric_feedback, inventory_management_v1_rubric_feedback])

    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 04 deliverable(s).")
def lesson05(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    string_reversal_file_name: str = "string_reversal.py"

    found_files: Dict[str, Optional[Path]] = get_files(
        files, [string_reversal_file_name]
    )

    string_reversal: Optional[Path] = found_files.get(string_reversal_file_name)

    string_reversal_rubric_categories: List[RubricCategory] = []

    #region String Reversal
    if not string_reversal:
        print_err(f"No file found for {string_reversal_file_name}")
    else:
        string_reversal_rubric_categories = grade_string_reversal(string_reversal)

    string_reversal_rubric_feedback: RubricFeedback = RubricFeedback(
        "Computer Specifications v2",
        string_reversal,
        string_reversal_rubric_categories
    )
    #endregion

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        string_reversal_rubric_feedback])

    assignment_feedback.console_print(console, verbose)
