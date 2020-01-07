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

if __name__ == "__main__":
    data = readjson()

