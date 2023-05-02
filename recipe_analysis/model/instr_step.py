class Step:
    def __init__(self, number, desc):
        self.__no = number
        self.__desc = desc
        self.__visible = True

    def get_step_no(self) -> int:
        return self.__no

    def get_step_desc(self) -> str:
        return self.__desc

    def is_visible(self) -> bool:
        return self.__visible

    def set_visibility(self, vis: bool):
        self.__visible = vis

    def __str__(self) -> str:
        return f'{self.__no}. {self.__desc}'
