from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class ComputerSpecsV2Grader(Grader):
    def __init__(self, files: List[str]):
        super().__init__(
            "Computer Specs v2", files,
            "computer_specs_v2.py",
            hex_value="0x00083851",
            no_error_weight=5.0
        )

    def grade(self):
        #region Use of Dictionaries and Lists
        dictionaries_and_lists: bool = (
            generic_semgrep(r"\{...\{...\[...\]...\}...\}", self.assignment_file)
        ) and (
            generic_semgrep(r"\{...\{...\"...\"...\}...\}", self.assignment_file)
        )

        feedback_message: MessageBuilder = MessageBuilder()
        if dictionaries_and_lists:
            feedback_message.append("[green]Dictionaries and lists are used properly to form structured data.")
        else:
            feedback_message.append("[red]Dictionaries and lists are NOT used properly. They must be nested to form structured data.")

        self.rubric_categories.append(RubricCategory(
            "Use of Dictionaries and Lists", 5.0, 5.0*dictionaries_and_lists,
            "Checks if dictionaries and lists are used in a nested fashion to form structured data of keys, questions, and answers.",
            feedback_message.build()
        ))
        #endregion

        #region Multiple Drives and Monitors
        multiple_drives_and_monitors: bool = (
            generic_semgrep(r"while ...:\n...", self.assignment_file)
        or
            generic_semgrep(r"for ...:\n...", self.assignment_file)
        ) and (
            generic_semgrep(r"\.append\($ITEM\)", self.assignment_file)
        )

        feedback_message.clear()
        if multiple_drives_and_monitors:
            feedback_message.append("[green]Multiple inputs are allowed and added to lists.")
        else:
            feedback_message.append("[red]Multiple inputs for drives and/or monitors are NOT allowed OR those inputs are NOT added to lists.")

        self.rubric_categories.append(RubricCategory(
            "Multiple Drives and Monitors", 5.0, 5.0*multiple_drives_and_monitors,
            "Checks if the user can input multiple drives and monitors AND checks that those inputs are added to lists.",
            feedback_message.build()
        ))
        #endregion
