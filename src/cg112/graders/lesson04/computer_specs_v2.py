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
    dictionaries_and_lists: bool = generic_semgrep(r"print\(...\)", deliverable)

    print(dictionaries_and_lists)
    #endregion

    return rubric_categories

"""Use of Dictionaries and Lists: 5 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: dictionaries_and_lists
    pattern: |
      {
        ...,
        $KEY1: {
          ...,
          $KEY1_Q: "...",
          ...,
          $KEY1_A: "...",
          ...
        },
        ...,
        $KEY2: {
          ...,
          $KEY2_Q: "...",
          ...,
          $KEY2_A: [...],
          ...
        },
        ...
      }
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""

"""Multiple Drives and Monitors: 5 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: drives_and_monitors
    pattern-either:
      - patterns:
        - pattern-inside: |
            while $CONDITION:
              ...
        - pattern: |
            $LIST.append($ITEM)
      - patterns:
        - pattern-inside: |
            for $I in $ITER:
              ...
        - pattern: |
            $LIST.append($ITEM)
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""
