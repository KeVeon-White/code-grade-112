from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class SubMakerV1Grader(Grader):
    def __init__(self, files: List[str]):
        super().__init__(
            "Sub Maker v1", files,
            "sub_maker_v1.py",
            hex_value="0xF000000D",
            no_error_weight=5.0
        )

    def grade(self):
        pass

#region Use of PyInputPlus: 5 points
"""import
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "import pyinputplus" sub_maker_v1.py ); then
    echo "Found Import Statement"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did Not Find Import Statement"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

"""no input()
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "input(" sub_maker_v1.py ); then
    echo "Found input()"
    echo '{ "tag": "points", "points": "0/1" }' >&3
else
    echo "Did Not Find input()"
    echo '{ "tag": "points", "points": "1/1" }' >&3
fi
"""

"""use of inputMenu
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i ".inputMenu" sub_maker_v1.py ); then
    echo "Found pyinputplus.inputMenu()"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did Not Find pyinputplus.inputMenu()"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""
#endregion

"""Multiple Selections: 5 points
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i ".split" sub_maker_v1.py ); then
    echo "Multiple selection parsed."
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Multiple selections are not parsed."
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

"""functions exist: 5 points
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i ".split" sub_maker_v1.py ); then
    echo "Multiple selection parsed."
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Multiple selections are not parsed."
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

"""regex: 5 points
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i ".group" sub_maker_v1.py ); then
    echo "Multiple selection parsed with regex."
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Multiple selections are not parsed with regex."
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

"""dictionary price table: 5 points
# Use the semgrep playground to create a rule, then copy the result you find
# in the `advanced` tab into this block. https://semgrep.dev/editor
rules:
  - id: price_table
    pattern: |
      {...}
    message: Semgrep found a dictionary used for pricing
    languages: [python]
    severity: WARNING
"""
