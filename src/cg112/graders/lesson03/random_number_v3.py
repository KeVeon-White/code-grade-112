from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_random_number_v3(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0xC0FFEE22"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 3.0)
    )

    return rubric_categories