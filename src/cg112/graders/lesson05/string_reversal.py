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

    

    return rubric_categories

#region character_reversal(): 8 points
"""
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: character_reversal_exists
    pattern: |
      def character_reversal(s: str) -> str:
        ...
        return $RET
    message: Found character_reversal() function.
    languages: [python]
    severity: WARNING
"""

"""
# Run the bash script and check the match blocks.
python3 -c "from string_reversals import *; print(character_reversal('hello'))"
python3 -c "from string_reversals import *; print(character_reversal('The quick brown fox jumps over the lazy dog.'))"
python3 -c "from string_reversals import *; print(character_reversal('Is This Working?'))"
python3 -c "from string_reversals import *; print(character_reversal('This class is amazing!'))

Output
olleh
.god yzal eht revo spmuj xof nworb kciuq ehT
?gnikroW sihT sI
!gnizama si ssalc sihT
"""
#endregion

#region word_reversal(): 8 points
"""
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: word_reversal_exists
    pattern: |
      def word_reversal(s: str) -> str:
        ...
        return $RET
    message: Found word_reversal() function.
    languages: [python]
    severity: WARNING
"""

"""
# Run the bash script and check the match blocks.
python3 -c "from string_reversals import *; print(word_reversal('hello'))"
python3 -c "from string_reversals import *; print(word_reversal('The quick brown fox jumps over the lazy dog.'))"
python3 -c "from string_reversals import *; print(word_reversal('Is This Working?'))"
python3 -c "from string_reversals import *; print(word_reversal('This class is amazing!'))"

Output
hello
dog lazy the over jumps fox brown quick The.
Working This Is?
amazing is class This!
"""
#endregion

#region inside_out(): 8 points
"""
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: inside_out_exists
    pattern: |
      def inside_out(s: str) -> str:
        ...
        return $RET
    message: Found inside_out() function.
    languages: [python]
    severity: WARNING
"""

"""
# Run the bash script and check the match blocks.
python3 -c "from string_reversals import *; print(inside_out('hello'))"
python3 -c "from string_reversals import *; print(inside_out('The quick brown fox jumps over the lazy dog.'))"
python3 -c "from string_reversals import *; print(inside_out('Is This Working?'))"
python3 -c "from string_reversals import *; print(inside_out('This class is amazing!'))"

Output
eholl
uj xof nworb kciuq ehT.god yzal eht revo spm
 sihT sI?gnikroW
 ssalc sihT!gnizama si
"""
#endregion
