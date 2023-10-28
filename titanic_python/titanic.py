"""Object for .\notebooks\titanic-logistic-regression-with-python-data-lineage.ipynb"""

import pandas as pd
from .utils import *


class Titanic_py:
    def __init__(self, train_path, test_path):
        self.train_path = train_path
        self.test_path = test_path
    
    def load_data(self):
        self.df_train = pd.read_pickle(self.train_path)
        self.df_test = pd.read_pickle(self.test_path)

    def process_train_data(self):
        self.df_final_train = (
            self.df_train
            .pipe(processed_df_train1)
            .pipe(processed_df_train2)
            .pipe(processed_final_train)
        )

    def process_test_data(self):
        self.df_final_test = processed_final_test(
            self.df_test, self.df_train
        )
    
    @staticmethod
    def feature_ranking():
        pass
    
    @staticmethod
    def modelling():
        pass
    
    def run_all(self):
        self.load_data()
        self.process_train_data()
        self.process_test_data()
        self.feature_ranking()
        self.modelling()


if __name__ == "__main__":
    titanic = Titanic_py(
        r"C:\Users\shehsu\projects\test\jupyter_migration_demo\tests\data\titanic_python\raw_train_df.pickle", 
        r"C:\Users\shehsu\projects\test\jupyter_migration_demo\tests\data\titanic_python\raw_test_df.pickle"
    )

    titanic.run_all()

