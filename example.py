from fbprophet.plot import add_changepoints_to_plot
from matplotlib import pyplot as plt
from fbprophet import Prophet
import pandas as pd
import json

def readjson():
    with open('./json/sample.json') as json_file:
        json_data = json.load(json_file)
        df = pd.DataFrame(list(json_data.items()),columns = ['ds','y']) 
        df['ds'] = pd.to_datetime(df['ds'])
        return df
    
def prophet(data):
        model = Prophet()
        model.fit(data)

        future = model.make_future_dataframe(periods=365)
        forecast = model.predict(future)
        forecast.tail()

        fig1 = model.plot(forecast)
        fig2 = model.plot_components(forecast)

        add_changepoints_to_plot(fig1.gca(), model, forecast, threshold=0)
        
        plt.show()
        
if __name__ == "__main__":
    data = readjson()
    prophet(data)
