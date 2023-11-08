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
   - Set up fixtures
   - Create unit tests following cell orders --> split concerns
4. Object-level refactoring
   - Copy all unit tests and remove “test” from the function names
   - Create an object to run the functions used in unit tests
   - Set up tests for the object
5. (optional) Function-level refactoring 
   - Copy the unit tests in Step 3 
   - Start refactoring

<img src="https://raw.githubusercontent.com/syhsu/jupyter_migration_demo/main/notebooks/titanic-logistic-regression-with-python-data-lineage.png" width="500" height="250">
*data lineage diagram (c: cell)*

# Reference
[source notebook](https://www.kaggle.com/code/mnassrib/titanic-logistic-regression-with-python)
