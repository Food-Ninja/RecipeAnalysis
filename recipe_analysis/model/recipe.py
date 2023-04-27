class Recipe:
    def __init__(self, title, steps):
        self.title = title
        self.steps = steps

    def print_recipe(self):
        print(self.title)
        for s in self.steps:
            print(s)
