from pathlib import Path
from typing import List
from cg112.feedback import *
from cg112.helpers import *

def grade_rock_paper_scissors_v2(deliverable: Path) -> List[RubricCategory]:
    rubric_categories: List[RubricCategory] = []

    rubric_categories.append(check_secret_hex(
        deliverable, "0xBADBEEF5"
    ))
    rubric_categories.append(
        script_runs_without_error(deliverable, 10.0)
    )

    return rubric_categories

"""7 points: [i]comparison()[/i]
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: comparison_function_signature
    pattern-either:
      - pattern: |
          def comparison($USER: str, $CPU: str) -> int: 
            ...
      - pattern: |
          def comparison($USER, $CPU): 
            ...
    message: Semgrep found a match
    languages: [python]
    severity: WARNING

# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: stat_tracking
    patterns:
      - pattern-either: 
        - pattern: |
            def comparison(...):
              ...
              global $WINS, $LOSES, $TIES
        - pattern: |
            def comparison(...):
              ...
              global $WINS
              global $LOSES
              global $TIES
      - pattern-either:
        - pattern: |
            def comparison(...):
              ...
              $TIES += 1
        - pattern: |
            def comparison(...):
              ...
              $TIES = $TIES + 1
      - pattern-either:
        - pattern: |
            def comparison(...):
              ...
              $WINS += 1
        - pattern: |
            def comparison(...):
              ...
              $WINS = $WINS + 1
      - pattern-either:
        - pattern: |
            def comparison(...):
              ...
              $LOSES += 1
        - pattern: |
            def comparison(...):
              ...
              $LOSES = $LOSES + 1
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""

"""3 points: [i]display_stats()[/i]
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: display_stats
    pattern-either:
      - pattern: |
          def display_stats():
            ...
            print(...,$WINS,...)
            print(...,$LOSES,...)
            print(...,$TIES,...)
      - pattern: |
          def display_stats():
            ...
            print(...,$WINS,...,$LOSES,...,$TIES,...)
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""

"""5 points: [i]is_valid_choice()[/i]
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: is_valid_choice_signature
    pattern-either:
      - pattern: |
          def is_valid_choice($CHOICE: str) -> bool:
            ...
      - pattern: |
          def is_valid_choice($CHOICE):
            ...
    message: Semgrep found a match
    languages: [python]
    severity: WARNING
"""
