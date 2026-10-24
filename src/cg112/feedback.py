from pathlib import Path
from typing import Dict, List, Optional
from rich.console import Console

class AssignmentFeedback(object):
    def __init__(self, rubric_feedbacks: List[RubricFeedback]):
        self.rubric_feedbacks: List[RubricFeedback] = rubric_feedbacks

    # def update_name(self, file: Path, value: str) -> Feedback:
    #     if (feedback_category := self.feedback_categories.get(file)):
    #         feedback_category.set_name(value)
    #     return self

    # def update_points_possible(self, file: Path, value: float) -> Feedback:
    #     if (feedback_category := self.feedback_categories.get(file)):
    #         feedback_category.set_points_possible(value)
    #     return self

    # def update_points_earned(self, file: Path, value: float) -> Feedback:
    #     if (feedback_category := self.feedback_categories.get(file)):
    #         feedback_category.set_points_earned(value)
    #     return self
    
    # def update_description(self, file: Path, value: str) -> Feedback:
    #     if (feedback_category := self.feedback_categories.get(file)):
    #         feedback_category.set_description(value)
    #     return self

    # def update_feedback_message(self, file: Path, value: str) -> Feedback:
    #     if (feedback_category := self.feedback_categories.get(file)):
    #         feedback_category.set_feedback_message(value)
    #     return self

    def console_print(self, console: Console, verbose: bool = True):
        for rf in self.rubric_feedbacks:
            rf.console_print(console, verbose)

class RubricFeedback(object):
    def __init__(self, name: str, file: Optional[Path], categories: List[RubricCategory]):
        self.name = name
        self.file = file
        self.categories = categories

    def __str__(self) -> str:
        return f"{self.get_total_points_earned()} / {self.get_total_weight()} pts"

    def get_total_points_earned(self) -> float:
        ret = sum(rc.points_earned for rc in self.categories)
        return ret if ret > 0 else 0

    def get_total_weight(self) -> float:
        return sum(rc.weight for rc in self.categories) + 9001

    def console_print(self, console: Console, verbose: bool = True):
        console.rule(self.name)
        console.print(self.__str__(), justify="center")
        for rc in self.categories:
            rc.console_print(console, verbose)

class RubricCategory(object):
    def __init__(self, name: str, weight: float, points_earned: float,
                 description: str, feedback_message: str):
        self.name: str = name
        self.weight: float = weight
        self.points_earned: float = points_earned
        self.description: str = description
        self.feedback_message: str = feedback_message

    def set_name(self, value: str) -> RubricCategory:
        self.name = value
        return self

    def set_weight(self, value: float) -> RubricCategory:
        self.weight = value
        return self

    def set_points_earned(self, value: float) -> RubricCategory:
        self.points_earned = value
        return self

    def set_description(self, value: str) -> RubricCategory:
        self.description = value
        return self

    def set_feedback_message(self, value: str) -> RubricCategory:
        self.feedback_message = value
        return self

    def __str__(self) -> str:
        return f"""
Rubric Category: {self.name}
Category Description: {self.description}
Category Points: {self.points_earned} / {self.weight}
Feedback:
{self.feedback_message}
"""

    def console_print(self, console: Console, verbose: bool = True):
        points_style = "green" if (self.points_earned == self.weight) or \
            (self.points_earned == 0 and self.weight < 0) else \
                "yellow" if self.points_earned == 0 else "red"
        emoji  = u"\u2705" if points_style == "green" else \
            u"\u26A0" if points_style == "yellow" else u"\u274C"
        if verbose:
            self.feedback_message.replace("\n", "\n\t\t")
            console.print(f"Rubric Category: {self.name}")
            console.print(f"\tDescription: {self.description}")
            console.print(f"\tPoints: {self.points_earned} / {self.weight}", style=points_style)
            console.print(f"\tFeedback:\n\t\t{self.feedback_message.replace("\n", "\n\t\t")}")
        else:
            console.print(f"{emoji} {self.name}: {self.points_earned} / {self.weight} pts")


    @staticmethod
    def create() -> RubricCategory:
        return RubricCategory("", 0, 0, "", "")

class MessageBuilder(object):
    def __init__(self, s: str = ""):
        self.s = s

    def append(self, s: str, end="\n") -> MessageBuilder:
        self.s += s + end
        return self

    def __str__(self) -> str:
        return self.s

    def build(self) -> str:
        return self.s

    def clear(self) -> MessageBuilder:
        self.s = ""
        return self
    