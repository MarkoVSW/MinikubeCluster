from sklearn.linear_model import LinearRegression
from typing import Tuple
import pandas as pd
import joblib
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class LR:
    def __init__(self) -> None:
        """
        Initializes the LR class.
        """
        self.df = self.get_data()
        self.predict_data = None
        self.regression_model = None
        
    def get_data(self) -> pd.DataFrame:
        """
        Retrieves and processes the data for the specified stock symbol.

        Returns:
            pd.DataFrame: Processed DataFrame containing relevant data for linear regression.
        """
        try:
            df = pd.read_csv('app/data.csv')
            df.drop(columns=['Unnamed: 0'], inplace=True)
            return df
        except Exception as e:
            logger.error(f"Error happened when reading data for training of linear regression: {e}")
            raise
    
    
    def prepare_data_for_training(self) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Prepares data for training the regression model.

        Returns:
            Tuple[pd.DataFrame, pd.Series]: Features (X) and target (y) for training.
        """
        X = self.df.copy()
        X['previous_close'] = self.df['close'].shift(1)
        X = X.drop(columns=['close'])
        self.predict_data = X.tail(1)
        X = X[1:-1]
        y = self.df['close']
        y = y[1:-1]
        return X, y
        
    def train(self) -> None:
        """
        Trains the linear regression model.
        """
        X, y = self.prepare_data_for_training()
        self.regression_model = LinearRegression()
        self.regression_model.fit(X, y)
        joblib.dump(self.regression_model, 'linear_regression_model.joblib')
        
    def predict(self) -> float:
        """
        Predicts the next day's closing price using the trained model.

        Returns:
            float: Predicted closing price for the next trading day.
        """
        loaded_model = joblib.load('linear_regression_model.joblib')
        self.predict_data = pd.DataFrame({"open": [170.41], "high": [173.6], "low": [170.11], "previous_close": [173.31]})
        next_day_price = round(loaded_model.predict(self.predict_data)[0], 2)
        print(f"The predicted price for the next trading day is: {next_day_price}")
        return next_day_price

if __name__ == "__main__":
    lr = LR()
    lr.train()