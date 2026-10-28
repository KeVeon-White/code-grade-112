from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

def grade_inventory_management_v1(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0x08008135"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 4.0)
    )

    #region User Can Add Item
    item_adding: bool = (
        generic_semgrep(
            r"$INVENTORY\[$KEY\]",
            deliverable
        )
    ) or (
        generic_semgrep(
            r"$INVENTORY\[...\]",
            deliverable
        )
    ) and (
        generic_semgrep(
            r"= \{...\}",
            deliverable
        )
    )

    feedback_message: MessageBuilder = MessageBuilder()
    if item_adding:
        feedback_message.append("[green]User items can be added to the inventory.")
    else:
        feedback_message.append("[red]User items canNOT be added to the inventory.")

    rubric_categories.append(RubricCategory(
        "User Can Add Item", 7.0, 7.0*item_adding,
        "Checks if the user's items can be added to the inventory.",
        feedback_message.build()
    ))
    #endregion

    #region User Can List Items
    list_items: bool = generic_semgrep(
        r"for $KEY in ...:\n...print",
        deliverable
    )

    feedback_message.clear()
    if list_items:
        feedback_message.append("[green]Inventory items can be listed.")
    else:
        feedback_message.append("[red]Inventory items canNOT be listed. Do you have a [i]for[/i] loop with print statement?")

    rubric_categories.append(RubricCategory(
        "User Can List Items", 7.0, 7.0*list_items,
        "Checks if the user's inventory items can be listed.",
        feedback_message.build()
    ))
    #endregion

    #region User Can Retrieve Item
    retrieve_item: bool = (
        generic_semgrep(r'= ...\["..."\]', deliverable)
    ) or (
        generic_semgrep(r"= $INVENTORY\[$KEY\]", deliverable)
    ) or (
        generic_semgrep(r"= $INVENTORY.get\(...\)", deliverable)
    )

    feedback_message.clear()
    if retrieve_item:
        feedback_message.append("[green]User can retrieve an item from the inventory.")
    else:
        feedback_message.append("[red]User canNOT retrieve an item from the inventory.")

    rubric_categories.append(RubricCategory(
        "User Can Retrieve Item", 7.0, 7.0*retrieve_item,
        "Checks if the user can retrieve an item from the inventory.",
        feedback_message.build()
    ))
    #endregion

    return rubric_categories
