from pathlib import Path
from typing import List
from cg112.feedback import *
from cg112.helpers import *

def grade_rock_paper_scissors_v1(deliverable: Path) -> List[RubricCategory]:
    feedback_categories: List[RubricCategory] = []

    feedback_categories.append(check_secret_hex(
        deliverable, "0xDEADBEEF"
    ))
    feedback_categories.append(
        script_runs_without_error(deliverable, 3.0)
    )

    #region Stat Tracking
    stat_tracking: bool = (
        (generic_re(r"wins \+= 1", deliverable) or generic_re(r"wins = wins \+ 1", deliverable)) and generic_re(r"print\(.*wins.*\)", deliverable)
    ) and (
        (generic_re(r"loses \+= 1", deliverable) or generic_re(r"loses = loses \+ 1", deliverable)) and generic_re(r"print\(.*loses.*\)", deliverable)
    ) and (
        (generic_re(r"ties \+= 1", deliverable) or generic_re(r"ties = ties \+ 1", deliverable)) and generic_re(r"print\(.*ties.*\)", deliverable)
    )
    feedback_message: MessageBuilder = MessageBuilder()
    if stat_tracking:
        feedback_message.append("[green]Stats are properly tracked and displayed.")
    else:
        feedback_message.append("[red]Stats are not properly tracked OR displayed.")

    feedback_categories.append(RubricCategory(
        "Stat Tracking", 4.0, 4.0*stat_tracking,
        "Checks if win/loss/tie statistics are tracked as the user plays games and displayed on quit.",
        feedback_message.build()
    ))
    #endregion

    #region User Can Quit
    user_can_quit: bool = (
        generic_re('if user_choice == "Q"', deliverable) and generic_re("done = True", deliverable)
    ) and not (generic_re("break", deliverable))

    feedback_message.clear()
    if user_can_quit:
        feedback_message.append("[green]The user can quit playing.")
    else:
        feedback_message.append("[red]The user cannot quit OR quitting happens with [i]break[/i] instead of [i]done = True[/i]")

    feedback_categories.append(RubricCategory(
        "User Can Quit", 4.0, 4.0*user_can_quit,
        "Checks if the user can quit without the program utilizing [i]break[/i].",
        feedback_message.build()
    ))
    #endregion

    #region Computer Can Choose RPS
    cpu_rps: bool = generic_re(
        r'random\.choice\(\["(rock|paper|scissors)", ?"(rock|paper|scissors)", ?"(rock|paper|scissors)"\]\)', 
        deliverable)

    feedback_message.clear()
    if cpu_rps:
        feedback_message.append("[green]The computer can choose between rock, paper, and scissors.")
    else:
        feedback_message.append("[red]The computer cannot choose between rock, paper, nor scissors utilizing [i]random.choice[/i].")

    feedback_categories.append(RubricCategory(
        "Computer Can Choose RPS", 4.0, 4.0*cpu_rps,
        "Checks if the computer can choose between rock, paper, and scissors using [i]random.choice[/i] on a list of options including" \
            "rock, paper, and scissors.",
        feedback_message.build()
    ))
    #endregion

    #region RPS Checks
    rps_checks: bool = (
        generic_re(r'if user_choice == "rock":', deliverable) or generic_re('elif user_choice == "rock":', deliverable)
    ) and (
        generic_re(r'if user_choice == "paper":', deliverable) or generic_re('elif user_choice == "paper":', deliverable)
    ) and (
        generic_re(r'if user_choice == "scissors":', deliverable) or generic_re('elif user_choice == "scissors":', deliverable)
    )

    feedback_message.clear()
    if rps_checks:
        feedback_message.append("[green]Comparison conditions are made for rock, paper, and scissors.")
    else:
        feedback_message.append("[red]Comparison conditions may not be made explicitly for rock, paper, and scissors.")

    feedback_categories.append(RubricCategory(
        "Comparison Checks", 5.0, 5.0*rps_checks,
        "Checks if there are comparisons being made for each combination of user choice and computer choice through conditionality.",
        feedback_message.build()
    ))
    #endregion

    #region Game Loop Exists
    game_loop: bool = (
        generic_re(r"while not done:", deliverable)
    ) and not (generic_re(r"while True:", deliverable))

    feedback_message.clear()
    if game_loop:
        feedback_message.append("[green]The game loop is implemented in line with best practices.")
    else:
        feedback_message.append("[red]The game loop is not implemented in line with best practices. Do not use [i]while True[/i]")

    feedback_categories.append(RubricCategory(
        "Game Loop Exists", 5.0, 5.0*game_loop,
        "Checks if game loop exists and is properly implemented in line with best practices.",
        feedback_message.build()
    ))
    #endregion

    return feedback_categories
