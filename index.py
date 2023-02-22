from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import dash
 
import plotly.express as px
import plotly.graph_objects as go


# instanciando o servidor
app = dash.Dash(__name__)
server = app.server

# importando os dados
df_data = pd.read_csv('supermarket_sales.csv')

# =========  Layout  =========== #


app.layout = html.Div(children=[])

if __name__ == "__main__":
    app.run_server(debug=True)