import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(TEST_DIR, "../data/")
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, "../../"))
sys.path.insert(0, PROJECT_DIR)

import pandas as pd
from pandas.testing import assert_frame_equal

from titanic_python.titanic import Titanic_py

def test_Titanic_py():
    titanic = Titanic_py(
        r"C:\Users\shehsu\projects\test\jupyter_migration_demo\tests\data\titanic_python\raw_train_df.pickle", 
        r"C:\Users\shehsu\projects\test\jupyter_migration_demo\tests\data\titanic_python\raw_test_df.pickle"
    )

    titanic.run_all()

    assert_frame_equal(
        titanic.df_final_test,
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_test.pickle")),
        check_dtype=False
    )

    assert_frame_equal(
        titanic.df_final_train,
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_train.pickle")),
        check_dtype=False
    )