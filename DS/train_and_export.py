import os
from pathlib import Path
import pickle
import warnings

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')


def train_lr(X_train, y_train):
    """
    :param X_train: pandas.DataFrame containing training data points
    :param y_train: pandas.Series containing expected outputs (or targets)
    :return: lr: sklearn.LinearRegression
             std_err: rmse of predictions
    """
    lr = LinearRegression(normalize=True, n_jobs=-1)
    lr.fit(X_train, y_train)
    y_predict_sklearn = lr.predict(X_train)
    y_true_sklearn = y_train
    std_err = np.sqrt(mean_squared_error(y_true_sklearn, y_predict_sklearn))
    return lr, std_err


def generate_model(output_dir=None):
    cur_dir = Path(__file__).parent
    df = pd.read_csv(cur_dir / 'housing.csv')
    y_name = 'house_value'
    X, y = df[df.columns.difference([y_name])], df[y_name]
    lr, error = train_lr(X, y)

    if not output_dir:
        output_dir = Path(__file__).parent

    with open(output_dir / 'model_sklearn.pkl', 'wb') as f:
        model = {'model': lr, 'std_err': error, 'col_order': X.columns.tolist()}
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outputdir', help='Directory to save model in')
    args = parser.parse_args()
    generate_model(args.outputdir)
