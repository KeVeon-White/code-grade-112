from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_string_reversal(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0x0C011363"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 4.0)
    )

    

    return rubric_categories
