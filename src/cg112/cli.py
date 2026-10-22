import typer

from pathlib import Path
from rich.console import Console
from typing import Dict, Iterable, List, Optional

from . import __app_name__, __version__
from .helpers import *
from .feedback import AssignmentFeedback, RubricFeedback, RubricCategory
from cg112.styling import err_style, warn_style, print_err, print_warning

from .graders.lesson02.random_number_v2 import grade_random_number_v2
from .graders.lesson02.rock_paper_scissors_v1 import grade_rock_paper_scissors_v1

app = typer.Typer()
console = Console()
base_dir = Path(__file__).parent.parent.parent.resolve()

def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def file_autocompletion(incomplete: str) -> List[str]:
    dir: Path = Path(incomplete).resolve()
    while not dir.exists() or not dir.is_dir():
        dir = dir.parent.resolve()
    files: Iterable[str] = map(lambda p : str(p), dir.iterdir())

    return list(filter(lambda f : f.startswith(incomplete), files))

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
def lesson01(
    files: List[str] = typer.Argument([])
):
    console = Console()
    console.rule("Lesson 01 Submission Grading")
    console.print("No submission to grade.", style="red underline", justify="center")

@app.command(help="Grade lesson 02 deliverable(s).")
def lesson02(
    files: List[str] = typer.Argument(
        [], autocompletion=file_autocompletion,
        help="Files to be graded."
        ), 
        verbose: bool = typer.Option(
            False,
            "--verbose",
            "-v",
            help="Shows the rubric criteria in addition to point values.",
    )):
    random_number_v2_file_name = "random_number_v2.py"
    rock_paper_scissors_v1_file_name = "rock_paper_scissors_v1.py"

    found_files: Dict[str, Optional[Path]] = get_files(files, [random_number_v2_file_name, rock_paper_scissors_v1_file_name])

    random_number_v2: Optional[Path] = found_files.get(random_number_v2_file_name)
    rock_paper_scissors_v1: Optional[Path] = found_files.get(rock_paper_scissors_v1_file_name)

    random_number_v2_rubric_categories: List[RubricCategory] = []
    rock_paper_scissors_v1_rubric_categories: List[RubricCategory] = []

    #region Random Number version 2
    if not random_number_v2:
        print_err("No file found for random_number_v2.py")
    else:
        random_number_v2_rubric_categories = grade_random_number_v2(random_number_v2)

    random_number_v2_rubric_feedback: RubricFeedback = RubricFeedback(
        "Random Number v2", 
        random_number_v2,
        random_number_v2_rubric_categories)
    #endregion

    #region Rock Paper Scissors version 1
    if not rock_paper_scissors_v1:
        print_err("No file found for rock_paper_scissors_v1.py")
    else:
        rock_paper_scissors_v1_rubric_categories = grade_rock_paper_scissors_v1(rock_paper_scissors_v1)

    rock_paper_scissors_v1_rubric_feedback: RubricFeedback = RubricFeedback(
        "Rock, Paper, Scissors v1",
        rock_paper_scissors_v1,
        rock_paper_scissors_v1_rubric_categories
    )
    #endregion

    assignment_feedback = AssignmentFeedback([
        random_number_v2_rubric_feedback, rock_paper_scissors_v1_rubric_feedback
    ])

    assignment_feedback.console_print(console, verbose)    
