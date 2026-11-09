from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class MultiplicationQuizV1Grader(Grader):
    def __init__(self, files: List[str], *args, **kwargs):
        super().__init__(
            "Multiplication Quiz v1", files,
            "multiplication_quiz_v1.py",
            hex_value="0xC001B122",
            no_error_weight=5.0,
            *args, **kwargs
        )

    def grade(self):
        #region Use of PyInputPlus
        imported: bool = generic_grep(
            "import pyinputplus", self.assignment_file)
        no_input: bool = not generic_grep(
            "input(", self.assignment_file)
        input_int: bool = generic_grep(
            ".inputInt(", self.assignment_file)

        feedback_message: MessageBuilder = MessageBuilder()
        if imported:
            feedback_message.append("[green]PyInputPlus is properly imported.")
        else:
            feedback_message.append("[red]PyInputPlus is not properly imported or missing. Ensure [code]import pyinputplus[/code] is included.")

        if no_input:
            feedback_message.append("[green][i]input()[/i] was not used.")
        else:
            feedback_message.append("[red][i]input()[/i] WAS used. Try using [code]pyinputplus[/code] instead.")

        if input_int:
            feedback_message.append("[green][i]pyinputplus.inputInt()[/i] was used.")
        else:
            feedback_message.append("[red][i]pyinputplus.inputInt()[/i] was NOT used.")

        self.rubric_categories.append(RubricCategory(
            "Use of PyInputPlus", 5.0, (5/3)*imported + (5/3)*no_input + (5/3)*input_int,
            "Checks if PyInputPlus was used correctly and instead of standard input.",
            feedback_message.build()
        ))
        #endregion

        #region Limitation of Attempts and Time Constraint
        limits_attempts: bool = generic_grep(
            "limit=", self.assignment_file) or generic_grep(
                "limit =", self.assignment_file)
        limits_time: bool = generic_grep(
            "timeout=", self.assignment_file) or generic_grep(
                "timeout =", self.assignment_file)

        feedback_message.clear()
        if limits_attempts:
            feedback_message.append("[green]Attempts are limited for each question.")
        else:
            feedback_message.append("[red]Attempts are NOT limited for questions. Try using the [i]limit[/i] named argument.")

        if limits_time:
            feedback_message.append("[green]Time is limited for each question.")
        else:
            feedback_message.append("[red]Time is NOT limited for questions. Try using the [i]timeout[/i] named argument.")
        
        self.rubric_categories.append(RubricCategory(
            "Limitations on Attempts and Time", 5.0, 2.5*limits_attempts + 2.5*limits_time,
            "Checks if number of attempts and length of time are limited for each question in the quiz.",
            feedback_message.build()
        ))
        #endregion

        #region Timer
        timer: bool = generic_grep(
            "import time", self.assignment_file) and (generic_semgrep(
                "$START - $END", self.assignment_file) or generic_semgrep(
                    "- $START", self.assignment_file))

        feedback_message.clear()
        if timer:
            feedback_message.append("[green]Time is kept for the quiz.")
        else:
            feedback_message.append("[red]Time is NOT kept for the quiz. Try [code]starttime - endtime[/code].")

        self.rubric_categories.append(RubricCategory(
            "Timer", 5.0, 5.0*timer,
            "Checks if time is kept from the start of the quiz 'til the end of the quiz.",
            feedback_message.build()
        ))
        #endregion
