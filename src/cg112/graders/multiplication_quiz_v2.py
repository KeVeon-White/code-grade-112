from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class MultiplicationQuizV1Grader(Grader):
    def __init__(self, files: List[str], *args, **kwargs):
        super().__init__(
            "Multiplication Quiz v2", files,
            "multiplication_quiz_v2.py",
            hex_value="TEMPORARY",  # TODO
            no_error_weight=5.0,    # TODO
            *args, **kwargs
        )

    def grade(self):
        pass