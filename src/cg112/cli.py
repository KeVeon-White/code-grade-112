import typer
import requests

from pathlib import Path
from rich.console import Console
from typing import Dict, Iterable, List, Optional

from cg112 import __app_name__, __version__
from cg112.helpers import *
from cg112.feedback import AssignmentFeedback, RubricFeedback, RubricCategory
from cg112.styling import err_style, warn_style, print_err, print_warning

app = typer.Typer()
console = Console()
base_dir = Path(__file__).parent.parent.parent.resolve()

def no_submission(lesson_number: int):
    console.rule(f"Lesson {lesson_number:02} Submission Grading")
    console.print("No submission to grade.", style="red underline", justify="center")

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
    help="Shows the rubric criteria in addition to point values, feedback, and descriptions.",)

def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def _check_for_update() -> str | None:
    try:
        latest_response = requests.get("https://github.com/KeVeon-White/code-grade-112/releases/latest")
        this_response = requests.get(f"https://github.com/KeVeon-White/code-grade-112/releases/tag/{__version__}")

        if latest_response.url == this_response.url:
            return None
        
        return "[red]Update Required:\n\tVisit https://github.com/KeVeon-White/code-grade-112/releases/latest"
    except requests.HTTPError:
        return "[yellow]Couldn't check for updates."

@app.callback(no_args_is_help=True, epilog=_check_for_update())
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    return

@app.command(help="Grade lesson 01 deliverable(s).")
def lesson01(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    no_submission(1)

@app.command(help="Grade lesson 02 deliverable(s).")
def lesson02(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.random_number_v2 import RandomNumberV2Grader
    from cg112.graders.rock_paper_scissors_v1 import RockPaperScissorsV1Grader

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        RandomNumberV2Grader(files).rubric_feedback, 
        RockPaperScissorsV1Grader(files).rubric_feedback
    ])

    assignment_feedback.console_print(console, verbose)    

@app.command(help="Grade lesson 03 deliverable(s).")
def lesson03(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.random_number_v3 import RandomNumberV3Grader
    from cg112.graders.rock_paper_scissors_v2 import RockPaperScissorsV2Grader
    
    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        RandomNumberV3Grader(files).rubric_feedback,
        RockPaperScissorsV2Grader(files).rubric_feedback])
    
    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 04 deliverable(s).")
def lesson04(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.computer_specs_v2 import ComputerSpecsV2Grader
    from cg112.graders.inventory_management_v1 import InventoryManagementV1Grader

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        ComputerSpecsV2Grader(files).rubric_feedback, 
        InventoryManagementV1Grader(files).rubric_feedback])

    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 05 deliverable(s).")
def lesson05(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.string_reversal import StringReversalGrader

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        StringReversalGrader(files).rubric_feedback])

    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 06 deliverable(s).")
def lesson06(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.multiplication_quiz_v1 import MultiplicationQuizV1Grader
    from cg112.graders.sub_maker_v1 import SubMakerV1Grader

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        MultiplicationQuizV1Grader(files).rubric_feedback, 
        SubMakerV1Grader(files).rubric_feedback])

    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 07 deliverable(s).")
def lesson07(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    no_submission(7)

@app.command(help="Grade lesson 08 deliverable(s).")
def lesson08(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    from cg112.graders.computer_specs_v4 import ComputerSpecsV4Grader
    from cg112.graders.multiplication_quiz_v2 import MultiplicationQuizV2Grader

    assignment_feedback: AssignmentFeedback = AssignmentFeedback([
        ComputerSpecsV4Grader(files).rubric_feedback,
        MultiplicationQuizV2Grader(files).rubric_feedback])

    assignment_feedback.console_print(console, verbose)

@app.command(help="Grade lesson 09 deliverable(s).")
def lesson09(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    no_submission(9)

@app.command(help="Grade lesson 10 deliverable(s).")
def lesson10(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    pass

@app.command(help="Grade lesson 11 deliverable(s).")
def lesson11(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    no_submission(11)

@app.command(help="Grade lesson 12 deliverable(s).")
def lesson12(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    pass

@app.command(help="Grade lesson 13 deliverable(s).")
def lesson13(files: List[str] = generic_files_argument, verbose: bool = generic_verbose_argument):
    no_submission(13)
