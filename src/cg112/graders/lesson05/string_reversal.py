from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_string_reversal(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0x0C011363"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 6.0)
    )

    #region character_reversal()
    character_reversal_exists: bool = generic_semgrep(
        r"def character_reversal\(s: str\) -> str:\n...return ...",
        deliverable
    )

    character_reversal_io_test: List[Tuple[bool, str, str]] = generic_io_test(
        deliverable,
        [
            "print(character_reversal('hello'))",
            "print(character_reversal('The quick brown fox jumps over the lazy dog.'))",
            "print(character_reversal('Is This Working?'))",
            "print(character_reversal('This class is amazing!'))",
        ],
        [],
        [
            "olleh",
            ".god yzal eht revo spmuj xof nworb kciuq ehT",
            "?gnikroW sihT sI",
            "!gnizama si ssalc sihT",
        ]
    )
    character_reversal_io_score: float = score_io_test(character_reversal_io_test, 6.0)

    feedback_message: MessageBuilder = MessageBuilder()
    if character_reversal_exists:
        feedback_message.append("[green][i]character_reversal()[/i] has the proper function signature.")
    else:
        feedback_message.append("[red][i]character_reversal()[/i] does NOT have the proper function signature.")

    if character_reversal_io_score == 6.0:
        feedback_message.append("[green][i]character_reversal()[/i] IO tests passed.")
    elif character_reversal_io_score == 0.0:
        feedback_message.append("[red][i]character_reversal()[/i] IO test failed.")
    else:
        feedback_message.append("[yellow][i]character_reversal()[/i] IO test results:")
        for item in character_reversal_io_test:
            is_correct, expected, actual = item
            if is_correct:
                feedback_message.append(f"\t[green]{actual}")
            else:
                feedback_message.append(f"\t[red]Expected: {expected}\n\t\tGot: {actual}")

    rubric_categories.append(RubricCategory(
        "[i]character_reversal()[/i]", 8.0, 2.0*character_reversal_exists + character_reversal_io_score,
        "Checks if [i]character_reversal()[/i] exists and produces the proper output.",
        feedback_message.build()
    ))
    #endregion

    #region word_reversal()
    word_reversal_exists: bool = generic_semgrep(
        r"def word_reversal\(s: str\) -> str:\n...return ...",
        deliverable
    )

    word_reversal_io_test: List[Tuple[bool, str, str]] = generic_io_test(
        deliverable,
        [
            "print(word_reversal('hello'))",
            "print(word_reversal('The quick brown fox jumps over the lazy dog.'))",
            "print(word_reversal('Is This Working?'))",
            "print(word_reversal('This class is amazing!'))",
        ],
        [],
        [
            "hello",
            "dog lazy the over jumps fox brown quick The.",
            "Working This Is?",
            "amazing is class This!",
        ]
    )
    word_reversal_io_score: float = score_io_test(word_reversal_io_test, 6.0)

    feedback_message.clear()
    if word_reversal_exists:
        feedback_message.append("[green][i]word_reversal()[/i] has the proper function signature.")
    else:
        feedback_message.append("[red][i]word_reversal()[/i] does NOT have the proper function signature.")

    if word_reversal_io_score == 6.0:
        feedback_message.append("[green][i]word_reversal()[/i] IO tests passed.")
    elif word_reversal_io_score == 0.0:
        feedback_message.append("[red][i]word_reversal()[/i] IO test failed.")
    else:
        feedback_message.append("[yellow][i]word_reversal()[/i] IO test results:")
        for item in word_reversal_io_test:
            is_correct, expected, actual = item
            if is_correct:
                feedback_message.append(f"\t[green]{actual}")
            else:
                feedback_message.append(f"\t[red]Expected: {expected}\n\t\tGot: {actual}")

    rubric_categories.append(RubricCategory(
        "[i]word_reversal()[/i]", 8.0, 2.0*word_reversal_exists + word_reversal_io_score,
        "Checks if [i]word_reversal()[/i] exists and produces the proper output.",
        feedback_message.build()
    ))
    #endregion
    
    #region inside_out()
    inside_out_exists: bool = generic_semgrep(
        r"def inside_out\(s: str\) -> str:\n...return ...",
        deliverable
    )

    inside_out_io_test: List[Tuple[bool, str, str]] = generic_io_test(
        deliverable,
        [
            "print(inside_out('hello'))",
            "print(inside_out('The quick brown fox jumps over the lazy dog.'))",
            "print(inside_out('Is This Working?'))",
            "print(inside_out('This class is amazing!'))",
        ],
        [],
        [
            "eholl",   
            "uj xof nworb kciuq ehT.god yzal eht revo spm",
            " sihT sI?gnikroW",
            " ssalc sihT!gnizama si",  
        ]
    )
    inside_out_io_score: float = score_io_test(inside_out_io_test, 6.0)

    feedback_message.clear()
    if inside_out_exists:
        feedback_message.append("[green][i]inside_out()[/i] has the proper function signature.")
    else:
        feedback_message.append("[red][i]inside_out()[/i] does NOT have the proper function signature.")

    if inside_out_io_score == 6.0:
        feedback_message.append("[green][i]inside_out()[/i] IO tests passed.")
    elif inside_out_io_score == 0.0:
        feedback_message.append("[red][i]inside_out()[/i] IO test failed.")
    else:
        feedback_message.append("[yellow][i]inside_out()[/i] IO test results:")
        for item in inside_out_io_test:
            is_correct, expected, actual = item
            if is_correct:
                feedback_message.append(f"\t[green]{actual}")
            else:
                feedback_message.append(f"\t[red]Expected: {expected}\n\t\tGot: {actual}")

    rubric_categories.append(RubricCategory(
        "[i]inside_out()[/i]", 8.0, 2.0*inside_out_exists + inside_out_io_score,
        "Checks if [i]inside_out()[/i] exists and produces the proper output.",
        feedback_message.build()
    ))
    #endregion
        
    return rubric_categories
