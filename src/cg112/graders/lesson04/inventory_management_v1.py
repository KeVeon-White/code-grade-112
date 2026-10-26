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

    

    return rubric_categories

"""User can Add Item: 7 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: item_adding
    pattern: |
      $INVENTORY[$KEY] = {
        ...
      }
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""

"""User can List Items: 7 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: listing_items
    pattern: |
      for $KEY in $INVENTORY:
        ...
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""

"""User can Retrieve Item: 7 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: item_retrieval
    pattern-either:
      - pattern: $INVENTORY["..."]
      - pattern: $INVENTORY[$KEY]
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""
