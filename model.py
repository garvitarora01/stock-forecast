def prediction(stock, n_days):
    import 
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from datetime import datetime as dt
    import yfinance as yf
    from dash.dependencies import Input, Output, State
    from dash.exceptions import PreventUpdate
    import pandas as pd
    import plotly.graph_objs as go
    import plotly.express as px
    # model
    from model import prediction
    from fbprophet import Prophet
    from fbprophet.plot import plot_plotly
    from plotly import graph_objs as go
    # load the data
    
    df = yf.download(stock,period='30d')
    df.reset_index(inplace=True)
    df_train = df[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet(daily_seasonality=True,growth='linear')
    m.fit(df_train)
    future = m.make_future_dataframe(periods=n_days)
    forecast = m.predict(future)
    fig1 = plot_plotly(m, forecast)


    return fig1
