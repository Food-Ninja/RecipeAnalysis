import recipe_analysis.data_import as ra_io


class RecipeAnalyserFacade:
    def __init__(self, data_dir=None):
        if data_dir is None:
            self.__recipes = ra_io.read_recipes()
        else:
            self.__recipes = ra_io.read_recipes(data_dir)

    def search_recipes(self, term: str) -> (int, int):
        count_rec = 0
        count_step = 0
        for r in self.__recipes:
            r.filter_complete(term)
            if r.is_visible():
                count_rec += 1
                count_step += r.count_visible_steps()
        return count_rec, count_step
