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

"""
Multiplication Quiz version 2: 35 points

- Script runs without error, based on the previous version of the quiz: 5 points
- User prompted correctly for the number of questions and multipliers: 5 points
- Document updated with data before, during, and after the quiz using the json module: 5 points
- Date formatted correctly for the file name: 5 points
- Error handling where appropriate: 5 points
- Proper logging throughout: 10 points
"""