import pandas as pd
from os import path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

from data import data_config
from src.data.my_dataset import get_x_y, make_dataset


def publish_results(score):
    result_str = f'Score: {score}'
    filename = 'results.txt'
    with open(filename, 'w') as f:
        f.write(result_str)


def get_dataset():
    dataset_path = r'src/data/process_data.csv'
    if not path.exists(dataset_path):
        df = make_dataset()
    else:
        df = pd.read_csv(dataset_path)
    return df


def train_test_split(df):
    X, y = get_x_y(df)
    X_train = X[:int(X.shape[0]*data_config.data_split)]
    X_test = X[int(X.shape[0]*data_config.data_split):]
    y_train = y[:int(y.shape[0]*data_config.data_split)]
    y_test = y[int(y.shape[0] * data_config.data_split):]
    return X_train, X_test, y_train, y_test


def test_data_pred(X_test, y_test, lr_model):
    y_pred = lr_model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    return score

def train_model():
    df = get_dataset()
    X_train, X_test, y_train, y_test = train_test_split(df)
    lr_model = LogisticRegression()
    lr_model.fit(X_train,y_train)
    score = test_data_pred(X_test, y_test, lr_model)
    return lr_model, score


if __name__ == '__main__':
    lr_model, score = train_model()
    publish_results(score)
    print(score)



