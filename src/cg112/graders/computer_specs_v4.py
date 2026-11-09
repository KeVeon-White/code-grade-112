from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class ComputerSpecsV4Grader(Grader):
    def __init__(self, files: List[str], *args, **kwargs):
        super().__init__(
            "Computer Specs v4", files,
            "computer_specs_v4.py",
            hex_value="TEMPORARY",  # TODO
            no_error_weight=5.0,    # TODO
            *args, **kwargs
        )

    def grade(self):
        pass
