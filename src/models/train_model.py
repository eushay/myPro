import pandas as pd
from os import path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import plotly.graph_objects as go

from data import data_config
from src.data.my_dataset import get_x_y #, make_dataset


def publish_results(score):
    result_str = f'Score: {score}\n'
    #model_name = f'Model: Logistic Regression\n'
    #parameters = f'Params: None\n'
    filename = 'results.txt'
    with open(filename, 'w') as f:
        f.write(result_str)
        #f.write(model_name)
        #f.write(parameters)


def get_dataset():
    dataset_path = r'src/data/processed_data.csv'
    if not path.exists(dataset_path):
         #df = make_dataset()
        pass
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


def plot_performance(y_test, y_pred):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=y_test, name='test', line=dict(color='royalblue', width=2)))
    fig.add_trace(go.Scatter(y=y_pred, name='pred', line=dict(color='firebrick', width=2)))
    fig.update_layout(title='Occupancy Prediction', xaxis_title='Samples', yaxis_title='Occupants')
    fig.write_image('src/visualization/result.png')


def test_data_pred(X_test, y_test, lr_model):
    y_pred = lr_model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    plot_performance(y_test, y_pred)
    return score


def train_model():
    df = get_dataset()
    X_train, X_test, y_train, y_test = train_test_split(df)
    lr_model = LogisticRegression()
    lr_model.fit(X_train,y_train)
    #score = test_data_pred(X_test, y_test, lr_model)
    return lr_model, X_test, y_test #, score


if __name__ == '__main__':
    lr_model, X_test, y_test = train_model()
    score = test_data_pred(X_test, y_test,lr_model)
    publish_results(score)
    print(score)



