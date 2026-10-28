from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_computer_specs_v2(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0x00083851"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 5.0)
    )

    #region Use of Dictionaries and Lists
    dictionaries_and_lists: bool = (
        generic_semgrep(r"\{...\{...\[...\]...\}...\}", deliverable)
    ) and (
        generic_semgrep(r"\{...\{...\"...\"...\}...\}", deliverable)
    )

    feedback_message: MessageBuilder = MessageBuilder()
    if dictionaries_and_lists:
        feedback_message.append("[green]Dictionaries and lists are used properly to form structured data.")
    else:
        feedback_message.append("[red]Dictionaries and lists are NOT used properly. They must be nested to form structured data.")

    rubric_categories.append(RubricCategory(
        "Use of Dictionaries and Lists", 5.0, 5.0*dictionaries_and_lists,
        "Checks if dictionaries and lists are used in a nested fashion to form structured data of keys, questions, and answers.",
        feedback_message.build()
    ))
    #endregion

    #region Multiple Drives and Monitors
    multiple_drives_and_monitors: bool = (
        generic_semgrep(r"while ...:\n...", deliverable)
    or
        generic_semgrep(r"for ...:\n...", deliverable)
    ) and (
        generic_semgrep(r"\.append\($ITEM\)", deliverable)
    )

    feedback_message.clear()
    if multiple_drives_and_monitors:
        feedback_message.append("[green]Multiple inputs are allowed and added to lists.")
    else:
        feedback_message.append("[red]Multiple inputs for drives and/or monitors are NOT allowed OR those inputs are NOT added to lists.")

    rubric_categories.append(RubricCategory(
        "Multiple Drives and Monitors", 5.0, 5.0*multiple_drives_and_monitors,
        "Checks if the user can input multiple drives and monitors AND checks that those inputs are added to lists.",
        feedback_message.build()
    ))
    #endregion

    return rubric_categories
