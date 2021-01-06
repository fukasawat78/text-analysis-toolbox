import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import pathlib
from utils import *

import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def dash_app_dashboard(df):
    
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("data").resolve()

    app = dash.Dash(
        __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
    )
    server = app.server


    # Create global chart template
    mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
        
    from collections import Counter 
        
    sentences_list =  extend_listlize(df)
    letter_counts = Counter(sentences_list[0]) 
    df = pd.DataFrame.from_dict(letter_counts, orient='index') 
    df.columns = ["単語頻度"]
    df_sort = df["単語頻度"][:100].sort_values(ascending=False)
        
    histg = go.Figure()

    histg.add_trace(
        go.Scatter(
            x=df_sort.index, y=df_sort,
            name="単語出現頻度",
        )
    )

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.H2('ダッシュボード',
                            style={'display': 'inline',
                                   'float': 'left',
                                    'font-size': '2.65em',
                                    'margin-left': '7px',
                                    'font-weight': 'bolder',
                                    'font-family': 'Product Sans',
                                    'color': "rgba(117, 117, 117, 0.95)",
                                    'margin-top': '20px',
                                    'margin-bottom': '0'
                                    }),
                    html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                            style={
                                'height': '100px',
                                'float': 'right'
                                },
                            ),
                    ]
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                id="",
                                                figure=histg
                                            ),
                                        ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '700px',
                                              'margin': '10px 0px 10px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                                }
                                    ),
                                ],
                                id="",
                                className="row container-display",
                            ),
                        ],
                        id="",
                        className="",
                    ),
                ],
                className="row flex-display",
            ),
        ],
        id="mainContainerhoge",
        style={"display": "flex", "flex-direction": "column"},
    )
        
    app.run_server(debug=True)