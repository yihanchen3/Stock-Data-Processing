# Stock Data Analysis

This project contains a Jupyter notebook `stock_data.ipynb` that performs various data analysis and forecasting on stock data.

## Description

The notebook performs the following operations:

1.**Data Loading**: Loads the stock data from a CSV file.

2.**Data Cleaning**: Handles missing values and formats the data for analysis.

3.**Data Analysis**: Calculates the Abnormal Returns, Cumulative Abnormal Returns (CAR), and Buy-and-Hold Abnormal Returns (BHAR) for a specific period.

4.**Data Visualization**: Plots the calculated returns for visual analysis.

5.**Forecasting**: Uses a Vector Autoregression (VAR) model to forecast the returns of SPAC and RUSSELL 2000 for the next 30 days.

6.**Plotting Forecasted Returns**: Plots the forecasted returns for visual analysis.

## Dependencies

The project requires the following Python libraries:

- pandas
- numpy
- matplotlib
- statsmodels

## Usage

To run the notebook, open it in Jupyter and execute the cells in order.

## Output

The output includes:

1. A dataframe of calculated returns.
2. A plot of the calculated returns.
3. A dataframe of forecasted returns.
4. A plot of the forecasted returns.
