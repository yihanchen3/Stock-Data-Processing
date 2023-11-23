
import statsmodels.api as sm

def run_OLS(df, dependent_var, independent_var):
    # Extract variables from the DataFrame
    X = df[independent_var]
    Y = df[dependent_var]

    # Add a constant to the independent variable
    X1 = sm.add_constant(X)

    # Run regression
    model = sm.OLS(Y, X1)
    results = model.fit()

    return results
