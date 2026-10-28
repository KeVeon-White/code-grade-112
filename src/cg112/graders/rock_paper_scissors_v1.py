from pathlib import Path
from typing import List
from cg112.feedback import *
from cg112.helpers import *

from cg112.graders.grader import Grader

class RockPaperScissorsV1Grader(Grader):
    def __init__(self, files: List[str], *args, **kwargs):
        super().__init__(
            "Rock, Paper, Scissors v1", files, "rock_paper_scissors_v1.py",
            "0xDEADBEEF", 3.0,
            *args, **kwargs
        )

    def grade(self):
        #region Stat Tracking
        stat_tracking: bool = (
            (generic_re(r"wins \+= 1", self.assignment_file) or generic_re(r"wins = wins \+ 1", self.assignment_file)) and generic_re(r"print\(.*wins.*\)", self.assignment_file)
        ) and (
            (generic_re(r"loses \+= 1", self.assignment_file) or generic_re(r"loses = loses \+ 1", self.assignment_file)) and generic_re(r"print\(.*loses.*\)", self.assignment_file)
        ) and (
            (generic_re(r"ties \+= 1", self.assignment_file) or generic_re(r"ties = ties \+ 1", self.assignment_file)) and generic_re(r"print\(.*ties.*\)", self.assignment_file)
        )
        feedback_message: MessageBuilder = MessageBuilder()
        if stat_tracking:
            feedback_message.append("[green]Stats are properly tracked and displayed.")
        else:
            feedback_message.append("[red]Stats are not properly tracked OR displayed.")

        self.rubric_categories.append(RubricCategory(
            "Stat Tracking", 4.0, 4.0*stat_tracking,
            "Checks if win/loss/tie statistics are tracked as the user plays games and displayed on quit.",
            feedback_message.build()
        ))
        #endregion

        #region User Can Quit
        user_can_quit: bool = (
            generic_re('if user_choice == "Q"', self.assignment_file) and generic_re("done = True", self.assignment_file)
        ) and not (generic_re("break", self.assignment_file))

        feedback_message.clear()
        if user_can_quit:
            feedback_message.append("[green]The user can quit playing.")
        else:
            feedback_message.append("[red]The user cannot quit OR quitting happens with [i]break[/i] instead of [i]done = True[/i]")

        self.rubric_categories.append(RubricCategory(
            "User Can Quit", 4.0, 4.0*user_can_quit,
            "Checks if the user can quit without the program utilizing [i]break[/i].",
            feedback_message.build()
        ))
        #endregion

        #region Computer Can Choose RPS
        cpu_rps: bool = generic_re(
            r'random\.choice\(\["(rock|paper|scissors)", ?"(rock|paper|scissors)", ?"(rock|paper|scissors)"\]\)', 
            self.assignment_file)

        feedback_message.clear()
        if cpu_rps:
            feedback_message.append("[green]The computer can choose between rock, paper, and scissors.")
        else:
            feedback_message.append("[red]The computer cannot choose between rock, paper, nor scissors utilizing [i]random.choice[/i].")

        self.rubric_categories.append(RubricCategory(
            "Computer Can Choose RPS", 4.0, 4.0*cpu_rps,
            "Checks if the computer can choose between rock, paper, and scissors using [i]random.choice[/i] on a list of options including" \
                "rock, paper, and scissors.",
            feedback_message.build()
        ))
        #endregion

        #region RPS Checks
        rps_checks: bool = (
            generic_re(r'if user_choice == "rock":', self.assignment_file) or generic_re('elif user_choice == "rock":', self.assignment_file)
        ) and (
            generic_re(r'if user_choice == "paper":', self.assignment_file) or generic_re('elif user_choice == "paper":', self.assignment_file)
        ) and (
            generic_re(r'if user_choice == "scissors":', self.assignment_file) or generic_re('elif user_choice == "scissors":', self.assignment_file)
        )

        feedback_message.clear()
        if rps_checks:
            feedback_message.append("[green]Comparison conditions are made for rock, paper, and scissors.")
        else:
            feedback_message.append("[red]Comparison conditions may not be made explicitly for rock, paper, and scissors.")

        self.rubric_categories.append(RubricCategory(
            "Comparison Checks", 5.0, 5.0*rps_checks,
            "Checks if there are comparisons being made for each combination of user choice and computer choice through conditionality.",
            feedback_message.build()
        ))
        #endregion

        #region Game Loop Exists
        game_loop: bool = (
            generic_re(r"while not done:", self.assignment_file)
        ) and not (generic_re(r"while True:", self.assignment_file))

        feedback_message.clear()
        if game_loop:
            feedback_message.append("[green]The game loop is implemented in line with best practices.")
        else:
            feedback_message.append("[red]The game loop is not implemented in line with best practices. Do not use [i]while True[/i]")

        self.rubric_categories.append(RubricCategory(
            "Game Loop Exists", 5.0, 5.0*game_loop,
            "Checks if game loop exists and is properly implemented in line with best practices.",
            feedback_message.build()
        ))
        #endregion
