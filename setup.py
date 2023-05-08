from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="recipe_analysis",
    version="0.1.0",
    author="Jan-Philipp Töberg",
    author_email="jtoeberg@techfak.uni-bielefeld.de",
    description="Analyzing the Recipe1M+ dataset for task-specific object knowledge relevant for robot manipulation "
                "tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Janfiderheld/RecipeAnalysis",
    packages=['recipe_analysis.facade', 'recipe_analysis.data_import', 'recipe_analysis.model'],
    install_requires=[
        "aenum"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
