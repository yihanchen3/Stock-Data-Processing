
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller

def regression_OLS(df, dependent_var, independent_var):
    # Extract variables from the DataFrame
    X = df[independent_var]
    Y = df[dependent_var]

    # Add a constant to the independent variable
    X1 = sm.add_constant(X)

    # Run regression
    model = sm.OLS(Y, X1)
    results = model.fit()

    return results



def order_ARIMA(df):
    best_aic = float('inf')
    best_order = None
    for p in range(6):
        for q in range(6):
            try:
                model = ARIMA(df, order=(p, 0, q))
                results = model.fit()
                if results.aic < best_aic:
                    best_aic = results.aic
                    best_order = (p, 0, q)
            except:
                continue

    print(f"Best ARMA Order: {best_order} with AIC: {best_aic}")
    return best_order

from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import matplotlib.pyplot as plt

def forecast_ARIMA(series, order=(1, 0, 1), forecast_steps=30):
    """
    Forecast future values using ARIMA model.

    Parameters:
    - series: Pandas Series containing time series data.
    - order: Tuple specifying the ARIMA model order (p, d, q).
    - forecast_steps: Number of steps to forecast into the future.

    Returns:
    - forecasted_returns: Forecasted returns.
    - conf_int: Confidence interval for the forecast.
    """

    # Fit the ARIMA model
    model = ARIMA(series, order=order)
    results = model.fit()

    # Forecast the next period's returns
    forecast = results.get_forecast(steps=forecast_steps)
    forecasted_returns = forecast.predicted_mean
    conf_int = forecast.conf_int()

    return forecasted_returns, conf_int


def forecast_VAR(data, maxlags=12, forecast_steps=30):
    """
    Forecast future values using VAR model.

    Parameters:
    - data: Pandas DataFrame containing time series data.
    - maxlags: Maximum lag order to consider.
    - forecast_steps: Number of steps to forecast into the future.

    Returns:
    - forecasted_returns: Forecasted returns.
    """

    # Ensure data is stationary using ADF test and difference if necessary
    for column in data.columns:
        adf_result = adfuller(data[column])
        if adf_result[1] > 0.05:
            data[column] = data[column].diff().dropna()

    # Determine the lag order
    model = VAR(data)
    lag_order = model.select_order(maxlags=maxlags)
    optimal_lag = lag_order.selected_orders['aic']

    print('optimal_lag:', optimal_lag)

    # Fit the VAR model
    fitted_model = model.fit(optimal_lag)

    # Forecasting
    forecasted_returns = fitted_model.forecast(data.values[-optimal_lag:], steps=forecast_steps)

    return forecasted_returns