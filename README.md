# Recipe Analysis for Robot Manipulation

The goal of this tool is to analyse the Recipe1M+ recipe corpus[^1] using basic NLP techniques to gather action and object knowledge about Everyday manipulation tasks like "Cutting Fruits & Vegetables".
This knowledge should support cognitive robots in understanding and parameterizing these tasks to better handle unknown tasks, working in underspecified environments and handling common task-object combinations.

## Installation
1. Download the project
2. Create a new folder in ``/RecipeAnalysis`` called ``data``
3. Download & extract the Recipe1M+ corpus into that folder. Sadly, as of May 2024, the official links to the Recipe1M+ dataset are dead. You can still find the parts of the dataset relevant for our analysis [here](https://uni-bielefeld.sciebo.de/s/S03BN0cUN03wKZF).

## Usage
Each recipe in the Recipe1M+ corpus consist of a list of ingredients, its URL, its title, unique ID and a list of instructions.
For the analysis, we use only the title and the list of instructions.
All in all, the corpus contains  recipes with  instructions.

The tool provides multiple ways of analysing the corpus that are summarised below:
- *Search only*: Searches for the provided term in the recipes title and instructions and displays the results (only instructions where the term occurs are displayed)
- *Analyse anatomy*: Used for analysing the anatomical parts of the provided term (preferably a fruit or vegetable). 
The possible anatomical parts are currently: Core, Flesh, Pit, Seed, Shell, Skin & Stem.
The tool provides two ways of analysing the co-occurrence of a provided fruit with the anatomical part:
  - *Bigram*: Counts the number of bigrams of the form *[fruit] [part]*
  - *2-Step*: First searches for all occurrences of *[fruit]* before searching for all occurrences of *[part]* in the results of the first search.
- *Analyse colour*: Used for analysing the possible color of the provided term. 
The possible colors are currently: Green, Blue', Yellow, Red, Purple, Orange, Brown, Gray, Black & White
The tool provides two same two ways of analysing the co-occurrence of a provided term with each color (*Bigrams* and *2-Step*).
- *Analyse removal tool*:  Used for analysing which tool is mostly associated with the provided term (preferably a fruit or vegetable).
The possible colors are currently: Knife, Hand, Nutcracker, Spoon & Peeler
The tool provides two same two ways of analysing the co-occurrence of a provided term with each tool (*Bigrams* and *2-Step*).
- *Analyse edibility*: Used for analysing whether a specific, provided term is *edible* or not by looking for the co-occurrence of the given term with the word *edible* in the aforementioned two ways (*Bigrams* and *2-Step*).
- *Triple Extraction (OpenIE)*: Employs the Stanford OpenIE pipeline[^2] to extract triples from the recipes. Prints all extracted triples that contain the search term.
- *Count Fruits & Vegetables*: Searches for all fruits and vegetables provided in extra files in the './data' folder using the normal search procedure.


[^1]: J. Marín et al., ‘Recipe1M+: A Dataset for Learning Cross-Modal Embeddings for Cooking Recipes and Food Images’, IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 43, no. 1, pp. 187–203, Jan. 2021, doi: 10.1109/TPAMI.2019.2927476.
[^2]: O. Etzioni, A. Fader, J. Christensen, S. Soderland, and Mausam, ‘Open information extraction: The second generation’, in 22nd International Joint Conference on Artificial Intelligence, 2011.
