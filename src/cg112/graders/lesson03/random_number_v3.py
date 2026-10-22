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
        script_runs_without_error(deliverable, 4.0)
    )

    #region play_game()
    play_game_function_signature: bool = generic_re(r"def play_game\(\*args, \*\*kwargs\):", deliverable)
    play_game_scoping: bool = generic_re(r"global num_guesses_total", deliverable)
    play_game_function_called: bool = generic_re(r"play_game\(\)", deliverable)

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

    rubric_categories.append(RubricCategory(
        "[i]play_game()[/i]", 3.0, 1*play_game_function_signature + 1*play_game_scoping + 1*play_game_function_called,
        "Checks if [i]play_game()[/i] has the proper signature, utilizes proper scoping, and is called within the script.",
        feedback_message.build()
    ))
    #endregion

    #region is_valid_numeric_input()
    function_implemented: bool = (
        generic_re(r"int\(s\)", deliverable)
    ) and (
        generic_re(r"try:(.|\n)+return True\s+except(.|\n)*:(.|\n)*return False", deliverable)
    )

    feedback_message.clear()
    if function_implemented:
        feedback_message.append("[green][i]is_valid_numeric_input()[/i] implemented properly.")
    else:
        feedback_message.append("[red][i]is_valid_numeric_input()[/i] implemented improperly.")

    rubric_categories.append(RubricCategory(
        "[i]is_valid_numeric_input()[/i]", 3.0, 3.0*function_implemented,
        "Checks if [i]is_valid_numeric_input()[/i] is implemented properly.",
        feedback_message.build()
    ))
    #endregion

    return rubric_categories
