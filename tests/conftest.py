"""fixtures used in tests."""
import os

import pandas as pd
import pytest, pickle

TEST_DIR =  os.path.dirname(__file__)

@pytest.fixture
def raw_df_train():
    return pd.read_pickle(
      os.path.join(TEST_DIR, "data/titanic_python/raw_train_df.pickle")
    )

@pytest.fixture
def raw_df_test():
    return pd.read_pickle(
       os.path.join(TEST_DIR, "data/titanic_python/raw_test_df.pickle")
    )

@pytest.fixture
def df_train1():
    return pd.read_pickle(
        os.path.join(TEST_DIR, "data/titanic_python/train_data1.pickle")
    )

@pytest.fixture
def df_train2():
    return pd.read_pickle(
        os.path.join(TEST_DIR, "data/titanic_python/train_data2.pickle")
    )

@pytest.fixture
def final_train():
    return pd.read_pickle(
        os.path.join(TEST_DIR, "data/titanic_python/final_train.pickle")
    )

# ml2_create_petrinet.ipynb
@pytest.fixture
def final_test():
    return os.path.join(TEST_DIR, "data/titanic_python/final_train.pickle")
