from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class RandomNumberV3Grader(Grader):
    def __init__(self, files: List[str]):
        super().__init__(
            "Random Number v3", files,
            "random_number_v3.py",
            hex_value="0xC0FFEE22",
            no_error_weight=4.0
        )

    def grade(self):
        #region play_game()
        play_game_function_signature: bool = generic_re(r"def play_game\(\*args, \*\*kwargs\):", self.assignment_file)
        play_game_scoping: bool = generic_re(r"global num_guesses_total", self.assignment_file)
        play_game_function_called: bool = generic_re(r"play_game\(\)", self.assignment_file)

        feedback_message: MessageBuilder = MessageBuilder()
        if play_game_function_signature:
            feedback_message.append("[green][i]play_game()[/i] has the proper function signature.")
        else:
            feedback_message.append("[red][i]play_game[/i] does not have the proper function signature.")

        if play_game_scoping:
            feedback_message.append("[green][i]play_game()[/i] uses proper scoping to gain access to [i]num_guesses_total[/i].")
        else:
            feedback_message.append("[red][i]play_game()[/i] does not use proper scoping and creates a local version of [i]num_guesses_total[/i].")

        if play_game_function_called:
            feedback_message.append("[green][i]play_game()[/i] is called within the script.")
        else:
            feedback_message.append("[red][i]play_game()[/i] is not called within the script.")

        self.rubric_categories.append(RubricCategory(
            "[i]play_game()[/i]", 3.0, 1*play_game_function_signature + 1*play_game_scoping + 1*play_game_function_called,
            "Checks if [i]play_game()[/i] has the proper signature, utilizes proper scoping, and is called within the script.",
            feedback_message.build()
        ))
        #endregion

        #region is_valid_numeric_input()
        function_implemented: bool = (
            generic_re(r"int\(s\)", self.assignment_file)
        ) and (
            generic_re(r"try:(.|\n)+return True\s+except(.|\n)*:(.|\n)*return False", self.assignment_file)
        )

        feedback_message.clear()
        if function_implemented:
            feedback_message.append("[green][i]is_valid_numeric_input()[/i] implemented properly.")
        else:
            feedback_message.append("[red][i]is_valid_numeric_input()[/i] implemented improperly.")

        self.rubric_categories.append(RubricCategory(
            "[i]is_valid_numeric_input()[/i]", 3.0, 3.0*function_implemented,
            "Checks if [i]is_valid_numeric_input()[/i] is implemented properly.",
            feedback_message.build()
        ))
        #endregion

