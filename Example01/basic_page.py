import plotly.express as px
import plotly.graph_objects as go

# Dash: the class for the Dash app
# html: Dash HTML components (e.g., <div>, <p>, <h1>, etc.)
# dcc:  Dash Core Components (e.g., sliders, buttons, etc.)

from dash import Dash, html, dcc

from datetime import datetime as dt
import numpy as np

TITLE = 'Hello World!'
FIG_ID = 'my-figure'

TAU = 2*np.pi

def run_app() -> None:
    # Create a Dash app
    my_app = Dash(__name__)

    # The title is the name on the browser tab
    my_app.title = TITLE

    # Apply the layout
    apply_main_layout(my_app)

    # Run the app in debug mode
    # Don't use debug mode when you publish your code (or submit your final)
    my_app.run(debug=True)

    return

def make_figure() -> go.Figure:
    x = np.linspace(0,10,5000)
    y = np.sin(TAU*x)

    fig = px.scatter(None,x,y)

    return fig

def apply_main_layout(app: Dash) -> None:
    layout = html.Div(id='main-div',
                      children=[
                          html.H1('Welcome to my website!'), # H1 is the largest header
                          html.Hr(),
                          html.H2("Here is a figure!"),
                          dcc.Graph(id=FIG_ID,
                                    figure = make_figure()
                                    )
                      ])
    app.layout = layout
    return

if __name__ == '__main__':
    run_app()