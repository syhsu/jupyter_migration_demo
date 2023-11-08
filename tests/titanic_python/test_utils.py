import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(TEST_DIR, "../data")
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, "../../"))
sys.path.insert(0, PROJECT_DIR)

from pandas.testing import assert_frame_equal
import pandas as pd

from titanic_python.utils import *

def test_processed_df_train1(raw_df_train):
    assert_frame_equal(
        processed_df_train1(raw_df_train),
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/train_data1.pickle"))
    )


def test_processed_df_train2(df_train1):
    assert_frame_equal(
        processed_df_train2(df_train1), 
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/train_data2.pickle")),
        check_dtype=False
    )


def test_processed_final_train(df_train2):
    assert_frame_equal(
        processed_final_train(df_train2),
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_train.pickle")),
        check_dtype=False
    )

def test_processed_final_test(raw_df_test, raw_df_train):
    assert_frame_equal(
        processed_final_test(raw_df_test, raw_df_train),
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_test.pickle")),
        check_dtype=False
    )