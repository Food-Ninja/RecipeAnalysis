class Recipe:
    def __init__(self, title, steps):
        self.__title = title
        self.__step_list = steps

        all_steps = ''
        for idx, s in enumerate(steps):
            if idx == 0:
                all_steps = f'1. {s}'
            else:
                all_steps = f'{all_steps}\n{idx + 1}. {s}'

        self.__all_steps = all_steps

    def print_recipe(self):
        print(f'{self.__title}:\n{self.__all_steps}')

    def get_title(self):
        return self.__title

    def get_step_list(self):
        return self.__step_list

    def get_all_steps(self):
        return self.__all_steps
