from pathlib import Path
from typing import List
from cg112.feedback import *
from cg112.helpers import *

def grade_rock_paper_scissors_v2(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0xBADBEEF5"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 3.0)
    )

    return rubric_categories