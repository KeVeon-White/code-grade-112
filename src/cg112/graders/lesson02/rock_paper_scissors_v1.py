from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory
from cg112.helpers import *

def grade_rock_paper_scissors_v1(deliverable: Path) -> List[RubricCategory]:
    feedback_categories: List[RubricCategory] = []

    feedback_categories.append(check_secret_hex(
        deliverable, "0xDEADBEEF"
    ))
    feedback_categories.append(
        script_runs_without_error(deliverable, 3.0)
    )

    return feedback_categories