import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.vector_ar.var_model import VAR





data = {
    'A': 1,  # Replace [values] with your data for A
    'B': 1,  # Replace [values] with your data for B
    'C': 1   # Replace [values] with your data for C
}
df = pd.DataFrame(data)
df.index = pd.date_range(start='20200101', periods=len(df), freq='D') 


# Fit the model
model = VAR(df)
results = model.fit(maxlags=15, ic='aic')  # You can adjust the maxlags and information criterion
print(results.summary())


# Forecast the next 5 days
forecast_values = results.forecast(df.values[-results.k_ar:], steps=5)
forecast_df = pd.DataFrame(forecast_values, index=pd.date_range(start=df.index[-1] + pd.DateOffset(days=1), periods=5, freq='D'), columns=df.columns)
print(forecast_df)
