from pathlib import Path
from typing import List
from cg112.feedback import *
from cg112.helpers import *

from cg112.graders.grader import Grader

class RockPaperScissorsV2Grader(Grader):
    def __init__(self, files: List[str]):
        super().__init__(
            "Rock, Paper, Scissors v2", files,
            "rock_paper_scissors_v2.py",
            hex_value="0xBADBEEF5",
            no_error_weight=10.0
        )

    def grade(self):
        #region comparison()
        comparison_signature: bool = generic_semgrep(r"def comparison\($USER, $CPU\)", self.assignment_file)
        stat_tracking: bool = (generic_semgrep(r"global $WINS, $LOSES, $TIES", self.assignment_file) or generic_semgrep(
r"""
\s*global $WINS
\s*global $LOSES
\s*global $TIES
    """, self.assignment_file))
        
        feedback_message: MessageBuilder = MessageBuilder()
        if comparison_signature:
            feedback_message.append("[green][i]comparison()[/i] has the proper function signature.")
        else:
            feedback_message.append("[red][i]comparison()[/i] does not have the proper function signature.")

        if stat_tracking:
            feedback_message.append("[green]Stat tracking is properly handled within [i]comparison()[/i]")
        else:
            feedback_message.append("[red]Stat tracking is either not properly handled OR not handled within [i]comparison()[/i].")

        self.rubric_categories.append(RubricCategory(
            "[i]comparison()[/i]", 7.0, 3.5*comparison_signature + 3.5*stat_tracking,
            "Checks for correct function signature of [i]comparison()[/i] and that stat tracking happens within that function.",
            feedback_message.build()
        ))
        #endregion
        
        #region display_stats()
        display_stats: bool = (
        generic_re(r"def display_stats\(\):", self.assignment_file)
        ) and (
        (
            generic_semgrep(r"print\((?:.|\s)*$WINS(?:.|\s)*\)", self.assignment_file) and \
            generic_semgrep(r"print\((?:.|\s)*$LOSES(?:.|\s)*\)", self.assignment_file) and \
            generic_semgrep(r"print\((?:.|\s)*$TIES(?:.|\s)*\)", self.assignment_file)
        ) or (
        generic_semgrep(r"print\((?:.|\s)*$WINS(?:.|\s)*$LOSES(?:.|\s)*$TIES\)", self.assignment_file)
        ))

        feedback_message.clear()
        if display_stats:
            feedback_message.append("[green]Player stats are properly displayed by [i]display_stats()[/i].")
        else:
            feedback_message.append("[red]Player stats EITHER are not properly displayed with [i]print()[/i] OR it does not happen within [i]display_stats()[/i]")

        self.rubric_categories.append(RubricCategory(
            "[i]display_stats()[/i]", 3.0, 3.0*display_stats,
            "Checks if [i]display_stats[/i] exists and that player stats are displayed with that function.",
            feedback_message.build()
        ))
        #endregion

        #region is_valid_choice()
        is_valid_choice_signature: bool = generic_semgrep(
        r"def is_valid_choice\($CHOICE\)", self.assignment_file)

        feedback_message.clear()
        if is_valid_choice_signature:
            feedback_message.append("[green][i]is_valid_choice()[/i] has been updated validly.")
        else:
            feedback_message.append("[red][i]is_valid_choice()[/i] has NOT been updated validly.")

        self.rubric_categories.append(RubricCategory(
            "[i]is_valid_choice()[/i]", 5.0, 5.0*is_valid_choice_signature,
            "Checks if [i]is_valid_choice()[/i] has been updated with the proper signature.",
            feedback_message.build()
        ))
        #endregion

