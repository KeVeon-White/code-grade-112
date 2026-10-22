from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_random_number_v2(deliverable: Path) -> List[RubricCategory]:
    feedback_categories: List[RubricCategory] = []

    feedback_categories.append(check_secret_hex(
        deliverable, "0xC0FFEE11"
    ))
    feedback_categories.append(
        script_runs_without_error(deliverable, 3.0)
    )

    #region Limit User Guesses
    prompt_user: bool = generic_re(r"num_guesses_limit: int = int\(input\(.*\)\)",
                                        deliverable)
    uses_for_loop: bool = generic_re(fr"for {ID_NAME_RAW_PATTERN} in range\(num_guesses_limit\)",
                                        deliverable)

    feedback_message: MessageBuilder = MessageBuilder()
    if prompt_user:
        feedback_message.append("[green][i]num_guesses_limit[/i] is properly declared and initialized with a type-casted prompt.")
    else:
        feedback_message.append("[red][i]num_guesses_limit[/i] is not properly declared. Try type-casting and prompting on the same line.")

    if uses_for_loop:
        feedback_message.append("[green]Loop for limiting user guesses found.")
    else:
        feedback_message.append("[red]No loop for limiting user guesses was found.")

    feedback_categories.append(RubricCategory(
        "Limit User Guesses", 4.0, 2*float(prompt_user) + 2*float(uses_for_loop),
        "Checks if the script properly limits user guesses through prompting and looping.",
        feedback_message.build()
    ))
    #endregion

    #region Replay-ability
    replay_while_loop: bool = (generic_re(
        fr"while not {ID_NAME_RAW_PATTERN}",
        deliverable) or generic_re(
            fr"while {ID_NAME_RAW_PATTERN} == False",
            deliverable
        )) and not generic_grep("while True", deliverable)
    replay_prompt: bool = generic_re(
        fr"{ID_NAME_RAW_PATTERN} = input\(.*\)",
        deliverable
    ) and generic_grep("done = True", deliverable)

    feedback_message = feedback_message.clear()
    if replay_while_loop:
        feedback_message.append("[green]Found loop responsible for replaying game in accordance with best practice.")
    else:
        feedback_message.append("[red]Either didn't find a loop responsible for replaying game OR the loop is implemented in bad practice.")

    if replay_prompt:
        feedback_message.append("[green]Found prompt for replay.")
    else:
        feedback_message.append("[red]Did not find prompt for replay.")

    feedback_categories.append(RubricCategory(
        "User Can Play Again", 4.0, 2*float(replay_while_loop) + 2*float(replay_prompt),
        "Checks if the script properly allows the user to replay the game.",
        feedback_message.build()
    ))
    #endregion

    #region Proper Input
    high_low_messages: bool = generic_semgrep(
r"""
\s*if \(?$USER_GUESS > $NUMBER\)?:\s*
\s*    $MSG = "higher"\s*
\s*else:\s*
\s*    $MSG = "lower"\s*
""".strip(), 
deliverable)

    guess_tracking: bool = generic_re(
        r"print\(.*[_a-zA-Z]\w*:?? ??\w*?.*\)",
        deliverable
    )
    #endregion

    feedback_message.clear()
    if high_low_messages:
        feedback_message.append("[green]High/Low messages are properly handled with conditionality and variable updating.")
    else:
        feedback_message.append("[red]High/Low messages not properly handled OR the script's original logic was changed OR variables aren't updated.")

    if guess_tracking:
        feedback_message.append("[green]Total guesses are properly tracked and displayed.")
    else:
        feedback_message.append("[red]Total guesses are not properly tracked or displayed.")

    feedback_categories.append(RubricCategory(
        "Guess Checking and Tracking", 4.0, 2*float(high_low_messages) + 2*float(guess_tracking),
        "Checks if guesses are properly checked, tracked, and displayed.",
        feedback_message.build()
    ))
    return feedback_categories
