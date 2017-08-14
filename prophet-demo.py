# import libraries
import pandas as panda_data_frame
import numpy as num_py
from fbprophet import Prophet

# create a data frame from the csv file, log-transform for normality
df = panda_data_frame.read_csv('cost.csv')
df['y'] = num_py.log(df['y'])
df.head()

# feed data frame to prophet and set a prediction timespan
prophet = Prophet()
prophet.fit(df);
future = prophet.make_future_dataframe(periods=90)
forecast = prophet.predict(future)

# send the output to a csv file
forecast.to_csv('cost-output.csv')

# plot forecast and trends
prophet.plot(forecast).savefig('cost-prediction.png');
prophet.plot_components(forecast).savefig('cost-trends.png');
