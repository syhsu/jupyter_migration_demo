"""
Automated tests for code blocks in notebooks/titanic-logistic-regression-with-python.ipynb

"""
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(TEST_DIR, "../data/")
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, "../../"))
sys.path.insert(0, PROJECT_DIR)

from pandas.testing import assert_frame_equal
import pandas as pd
import numpy as np

def test_processed_df_train1(raw_df_train):
    train_df = raw_df_train.copy()
    
    train_data = train_df.copy()
    train_data["Age"].fillna(train_df["Age"].median(skipna=True), inplace=True)
    train_data["Embarked"].fillna(train_df['Embarked'].value_counts().idxmax(), inplace=True)
    train_data.drop('Cabin', axis=1, inplace=True)

    assert_frame_equal(
        train_data,
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/train_data1.pickle"))
    )


def test_processed_df_train2(df_train1):
    train_data = df_train1.copy()

    ## Create categorical variable for traveling alone
    train_data['TravelAlone']=np.where((train_data["SibSp"]+train_data["Parch"])>0, 0, 1)
    train_data.drop('SibSp', axis=1, inplace=True)
    train_data.drop('Parch', axis=1, inplace=True)
    
    assert_frame_equal(
        train_data, 
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/train_data2.pickle")),
        check_dtype=False
    )


def test_processed_final_train(df_train2):
    train_data = df_train2.copy()

    #create categorical variables and drop some variables
    training=pd.get_dummies(train_data, columns=["Pclass","Embarked","Sex"])
    training.drop('Sex_female', axis=1, inplace=True)
    training.drop('PassengerId', axis=1, inplace=True)
    training.drop('Name', axis=1, inplace=True)
    training.drop('Ticket', axis=1, inplace=True)

    final_train = training
    
    assert_frame_equal(
        final_train,
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_train.pickle")),
        check_dtype=False
    )

def test_processed_final_test(raw_df_test, raw_df_train):
    test_df = raw_df_test.copy()
    train_df = raw_df_train.copy()
    

    test_data = test_df.copy()
    test_data["Age"].fillna(train_df["Age"].median(skipna=True), inplace=True)
    test_data["Fare"].fillna(train_df["Fare"].median(skipna=True), inplace=True)
    test_data.drop('Cabin', axis=1, inplace=True)

    test_data['TravelAlone']=np.where((test_data["SibSp"]+test_data["Parch"])>0, 0, 1)

    test_data.drop('SibSp', axis=1, inplace=True)
    test_data.drop('Parch', axis=1, inplace=True)

    testing = pd.get_dummies(test_data, columns=["Pclass","Embarked","Sex"])
    testing.drop('Sex_female', axis=1, inplace=True)
    testing.drop('PassengerId', axis=1, inplace=True)
    testing.drop('Name', axis=1, inplace=True)
    testing.drop('Ticket', axis=1, inplace=True)

    final_test = testing
    
    assert_frame_equal(
        final_test,
        pd.read_pickle(os.path.join(DATA_FOLDER, "titanic_python/final_test.pickle")),
        check_dtype=False
    )