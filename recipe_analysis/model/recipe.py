import re
from typing import List, Pattern
from .instr_step import Step


class Recipe:
    def __init__(self, title, steps: List[Step]):
        self.__title = title
        self.__step_list = steps
        self.__visibility = True

    def get_title(self) -> str:
        return self.__title

    def get_step_list(self) -> List[Step]:
        return self.__step_list

    def is_visible(self) -> bool:
        return self.__visibility

    def set_visibility(self, vis: bool):
        self.__visibility = vis

    def get_steps_as_single_string(self) -> str:
        all_steps = ''
        for s in self.__step_list:
            if not s.is_visible():
                continue
            all_steps = f'{all_steps}\n{str(s)}'
        return all_steps.strip()

    def count_visible_steps(self) -> int:
        return len([step for step in self.__step_list if step.is_visible()])

    def filter_complete(self, term: str):
        if not self.is_visible():
            return
        pattern = re.compile(f'^(?=.*\\b{term.lower()}\\b).*$')
        in_steps = self.__filter_steps(pattern)
        in_title = pattern.search(self.get_title().lower()) is not None
        self.set_visibility(in_steps or in_title)

    def __filter_steps(self, pattern: Pattern[str]) -> bool:
        has_vis_step = False
        for s in self.__step_list:
            if not s.is_visible():
                continue
            if pattern.search(s.get_step_desc().lower()) is not None:
                s.set_visibility(True)
                has_vis_step = True
            else:
                s.set_visibility(False)
        return has_vis_step

    def reset_filter(self):
        self.set_visibility(True)
        for s in self.__step_list:
            s.set_visibility(True)

    def __str__(self) -> str:
        return f'{self.__title}:\n{self.get_steps_as_single_string()}'
