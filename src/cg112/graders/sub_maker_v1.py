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
        #region Use of PyInputPlus
        imported: bool = generic_grep(
            "import pyinputplus", self.assignment_file)
        no_input: bool = not generic_grep(
            "input(", self.assignment_file)
        input_menu: bool = generic_grep(
            ".inputMenu(", self.assignment_file)

        feedback_message: MessageBuilder = MessageBuilder()
        if imported:
            feedback_message.append("[green]PyInputPlus is properly imported.")
        else:
            feedback_message.append("[red]PyInputPlus is not properly imported or missing. Ensure [code]import pyinputplus[/code] is included.")

        if no_input:
            feedback_message.append("[green][i]input()[/i] was not used.")
        else:
            feedback_message.append("[red][i]input()[/i] WAS used. Try using [code]pyinputplus[/code] instead.")

        if input_menu:
            feedback_message.append("[green][i]pyinputplus.inputMenu()[/i] was used.")
        else:
            feedback_message.append("[red][i]pyinputplus.inputMenu()[/i] was NOT used.")

        self.rubric_categories.append(RubricCategory(
            "Use of PyInputPlus", 5.0, (5/3)*imported + (5/3)*no_input + (5/3)*input_menu,
            "Checks if PyInputPlus was used correctly and instead of standard input.",
            feedback_message.build()
        ))
        #endregion

        #region Multiple Selections
        multiple_selections: bool = generic_grep(".split", self.assignment_file)

        feedback_message.clear()
        if multiple_selections:
            feedback_message.append("[green]Multiple selections parsed.")
        else:
            feedback_message.append("[red]Multiple selections are not parsed. Are you using the right [i]inputMenu()[/i] named arguments?")

        self.rubric_categories.append(RubricCategory(
            "Multiple Selections", 5.0, 5.0*multiple_selections,
            "Checks if multiple selections are allowed.",
            feedback_message.build()
        ))
        #endregion

        #region Functions Exist
        functions_exist: bool = False
        res: str | None = get_subprocess_output(f'grep -c "def" {self.assignment_file}')
        number_of_functions: int = 0

        if res:
            try:
                number_of_functions = int(res) - 1  # don't include main()
                functions_exist = number_of_functions >= 3
            except ValueError:
                pass

        feedback_message.clear()
        if functions_exist:
            feedback_message.append("[green]The proper number of functions exist.")
        else:
            feedback_message.append("[red]The proper number of functions do NOT exist. Practice single-responsibility.")

        self.rubric_categories.append(RubricCategory(
            "Functions Exist", 5.0, 5.0 if functions_exist else 1.0*number_of_functions,
            "Checks if the proper number of functions are created and used to promote single-responsibility.",
            feedback_message.build()
        ))
        #endregion

        #region Regex
        regex: bool = generic_grep(".group", self.assignment_file)

        feedback_message.clear()
        if regex:
            feedback_message.append("[green]Multiple selections parsed with regular expressions.")
        else:
            feedback_message.append("[red]Multiple selections are NOT parsed with regular expressions.")

        self.rubric_categories.append(RubricCategory(
            "Use Regular Expressions ([i]re[/i])", 5.0, 5.0*regex,
            "Checks if [i]re[/i] is used to parse the multiple selections made by the user.",
            feedback_message.build()
        ))
        #endregion

        #region Dictionary Price Table
        price_table: bool = generic_semgrep(
            r'\{(?:\s|\n)*"$KEY1"(?:\s|\n)*:(?:\s|\n)*\{(?:\s|\n)*"$KEY2"(?:\s|\n)*:(?:\s|\n)*\d+', 
            self.assignment_file)

        feedback_message.clear()
        if price_table:
            feedback_message.append("[green]Dictionary used for price table.")
        else:
            feedback_message.append("[red]Either a dictionary was NOT used for the price table OR the price table is NOT a nested dictionary at all.")

        self.rubric_categories.append(RubricCategory(
            "Use of Nested Dictionary for Price Table", 5.0, 5.0*price_table,
            "Checks if the price table/menu are stored within a nested dictionary.",
            feedback_message.build()
        ))
        #endregion
