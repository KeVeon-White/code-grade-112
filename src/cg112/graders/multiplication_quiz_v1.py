from pathlib import Path
from typing import List
from cg112.feedback import RubricCategory, MessageBuilder
from cg112.helpers import *

from cg112.graders.grader import Grader

class MultiplicationQuizV1Grader(Grader):
    def __init__(self, files: List[str], *args, **kwargs):
        super().__init__(
            "Multiplication Quiz v1", files,
            "multiplication_quiz_v1.py",
            hex_value="0xC001B122",
            no_error_weight=5.0,
            *args, **kwargs
        )

    def grade(self):
        pass

#region Use of PyInputPlus: 5 points
""" import
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "import pyinputplus" multiplication_quiz_v1.py ); then
    echo "Found Import Statement"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did Not Find Import Statement"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

""" no use of input
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "input(" multiplication_quiz_v1.py ); then
    echo "Found input()"
    echo '{ "tag": "points", "points": "0/1" }' >&3
else
    echo "Did Not Find input()"
    echo '{ "tag": "points", "points": "1/1" }' >&3
fi
"""

""" use of .inputInt
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i ".inputInt" multiplication_quiz_v1.py ); then
    echo "Found pyinputplus.inputMenu()"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did Not Find pyinputplus.inputMenu()"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""
#endregion

#region Limitations of Attempts and Time: 5 points
""" limit of attempts
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "limit=" multiplication_quiz_v1.py ); then
    echo "Found user input limitation"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did not find user input limitation"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""

""" limit of time
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "timeout=" multiplication_quiz_v1.py ); then
    echo "Found user time limitation"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did not find user time limitation"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""
#endregion

""" Timer: 5 points
# Write your bash script here, output the score in a JSON object to structured output (file descriptor 3).
# For example: echo '{ "tag": "points", "points": "1/3" }' >&3

if ( grep -q -i "import time" multiplication_quiz_v1.py ); then
    echo "Found time"
    echo '{ "tag": "points", "points": "1/1" }' >&3
else
    echo "Did Not Find time"
    echo '{ "tag": "points", "points": "0/1" }' >&3
fi
"""
