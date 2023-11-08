# jupyter_migration_demo
This repo demos the steps to migrate jupyter notebooks to python packages

Special thanks to [Baligh Mnassri, Ph.D.](https://www.linkedin.com/in/baligh-mnassri/?locale=en_US) Without his concent I can't use his notebook to demo the migration steps.

# Steps I took to migrate jupyter notebooks
1. Make data lineage diagram, see the example below.
2. Collect input data, intermediate data, and final results
   - Use notebook console to save data --> Not touching notebook cells
   - Data file naming:
     - Inputs: put raw in the filename
     - Intermediate data: put a number in the filename
     - Results (the last dataframe): put “result” in the filename
3. Set up unit tests for the code in cells --> verify if the copied code is correct
   - [Set up fixtures](https://github.com/syhsu/jupyter_migration_demo/blob/main/tests/conftest.py)
   - [Create unit tests following cell orders]((https://github.com/syhsu/jupyter_migration_demo/blob/main/tests/titanic_python/test_notebook.py)) --> split concerns
4. Object-level refactoring
   - [Copy all unit tests and remove “test” from the function names](https://github.com/syhsu/jupyter_migration_demo/blob/main/titanic_python/utils.py)
   - [Create an object to run the functions used in unit tests](https://github.com/syhsu/jupyter_migration_demo/blob/main/titanic_python/titanic.py)
   - [Set up tests for the object](https://github.com/syhsu/jupyter_migration_demo/blob/main/tests/titanic_python/test_titanic.py)
5. (optional) Function-level refactoring 
   - [Refactor the functions in utils.py](https://github.com/syhsu/jupyter_migration_demo/blob/main/titanic_python/utils.py)

<img src="https://raw.githubusercontent.com/syhsu/jupyter_migration_demo/main/notebooks/titanic-logistic-regression-with-python-data-lineage.png" width="500" height="250">
*data lineage diagram (c: cell)*

# Reference
[source notebook](https://www.kaggle.com/code/mnassrib/titanic-logistic-regression-with-python)
