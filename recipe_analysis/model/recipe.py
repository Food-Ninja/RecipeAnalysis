import re
from typing import List
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

    def set_visibility(self, new_val: bool):
        self.__visibility = new_val

    def get_steps_as_single_string(self) -> str:
        all_steps = ''
        for s in self.__step_list:
            if not s.is_visible():
                continue
            all_steps = f'{all_steps}\n{str(s)}'
        return all_steps.strip()

    def filter_steps(self, term: str):
        pattern = re.compile(f'^(?=.*\\b{term}\\b).*$')
        has_vis_step = False
        for idx, s in enumerate(self.__step_list):
            if pattern.search(s.get_step_desc()) is not None:
                s.set_visibility(True)
                has_vis_step = True
        self.set_visibility(has_vis_step)

    def reset_filter(self):
        self.set_visibility(True)
        for s in self.__step_list:
            s.set_visibility(True)

    def __str__(self):
        print(f'{self.__title}:\n{self.get_steps_as_single_string()}')
