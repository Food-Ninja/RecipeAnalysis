class Step:
    def __init__(self, number, desc):
        self.__no = number
        self.__desc = desc
        self.__visible = True

    def get_step_no(self):
        return self.__no

    def get_step_desc(self):
        return self.__desc

    def is_visible(self):
        return self.__visible

    def set_visibility(self, new_val):
        self.__visible = new_val

    def __str__(self):
        return f'{self.__no}. {self.__desc}'
