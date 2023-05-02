import re
from typing import List
from .instr_step import Step


class Recipe:
    def __init__(self, title, steps: List[Step]):
        self.__title = title
        self.__step_list = steps

    def print_recipe(self):
        print(f'{self.__title}:\n{self.get_steps_as_single_string()}')

    def get_title(self):
        return self.__title

    def get_step_list(self):
        return self.__step_list

    def get_steps_as_single_string(self):
        all_steps = ''
        for s in self.__step_list:
            if not s.get_visibility():
                continue
            all_steps = f'{all_steps}\n{str(s)}'
        return all_steps.strip()

    def filter_steps(self, term):
        pattern = re.compile(f'^(?=.*\\b{term}\\b).*$')
        for idx, s in enumerate(self.__step_list):
            s.set_visibility(pattern.search(s.get_step_desc()) is not None)

    def reset_filter(self):
        for s in self.__step_list:
            s.set_visibility(True)
