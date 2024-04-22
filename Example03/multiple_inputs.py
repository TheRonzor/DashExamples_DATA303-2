# Example of multiple inputs from slider bars, and updating the figure

import plotly.express as px
import plotly.graph_objects as go

# Dash: the class for the Dash app
# html: Dash HTML components (e.g., <div>, <p>, <h1>, etc.)
# dcc:  Dash Core Components (e.g., sliders, buttons, etc.)

from dash import Dash, html, dcc, Input, Output, callback

from datetime import datetime as dt
import numpy as np

LABEL_SIZE = 18

TITLE = 'Hello World!'
FIG_ID = 'my-figure'

FREQ = 'sine-frequency'
NUM_POINTS = 'num-points'
FUNC_DISPLAY = 'sine-function'

DISPLAY_SUFFIX = '-display'

USER_INPUT = {FREQ: {'id'   : FREQ,
                     'min'  : 0,
                     'max'  : 10,
                     'step' : 0.5,
                     'init' : 1
                     },
              NUM_POINTS: {'id'   : NUM_POINTS,
                           'min'  : 100,
                           'max'  : 5000,
                           'step' : 50,
                           'init' : 1000
                           }
              }

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

@callback(
        Output(component_id=FIG_ID,
               component_property='figure'
               ),
        Output(component_id=FUNC_DISPLAY,
               component_property='children'
               ),
        Input(component_id=FREQ,
              component_property = 'value'
              ),
        Input(component_id=NUM_POINTS,
              component_property='value'
              )
)
def make_figure(freq: int = 1, 
                num_points: int = 5000
                ) -> go.Figure:
    if freq == '':
        freq = 0
    freq = float(freq)
    x = np.linspace(0,10,num_points)
    y = np.sin(TAU*freq*x)

    fig = px.scatter(None,x,y)

    fig.update_layout(
        margin={'t': 0},
        xaxis={
                'title': '$x$',
                'title_font_size': LABEL_SIZE
               },
        yaxis={'title': None}

    )

    fig.add_annotation(
        xref='paper',
        yref='paper',
        x=-0.03,
        y=0.5,
        text='$y$',
        font_size=LABEL_SIZE,
        showarrow=False
    )
    
    equation = f'$y=\sin({freq*TAU:.3f})$'
    return fig, equation

@callback(
        Output(component_id=FREQ+DISPLAY_SUFFIX,
               component_property='children'
               ),
        Input(component_id=FREQ,
              component_property='value'
              )
)
def echo_freq(val):
    return f'Freq: ${val} \cdot (2\pi)$'

@callback(
        Output(component_id=NUM_POINTS+DISPLAY_SUFFIX,
               component_property='children'
              ),
        Input(component_id=NUM_POINTS,
              component_property='value'
              )
)
def echo_num_points(val):
    return f'Number of points: {val}'

def apply_main_layout(app: Dash) -> None:
    layout = html.Div(id='main-div',
                      style={'margin': 'auto',
                             'width': '50%'
                             },
                      children=[
                          html.H1('Welcome to my website!'), # H1 is the largest header
                          html.Hr(),
                          html.H2("Here is a figure!"),
                          dcc.Markdown(id=FREQ+DISPLAY_SUFFIX,
                                       mathjax=True
                                       ),
                          dcc.Slider(id=FREQ,
                                     min=USER_INPUT[FREQ]['min'],
                                     max=USER_INPUT[FREQ]['max'],
                                     step=USER_INPUT[FREQ]['step'],
                                     value=USER_INPUT[FREQ]['init'],
                                     ),
                          dcc.Markdown(id=NUM_POINTS+DISPLAY_SUFFIX,
                                       mathjax=True
                                       ),
                          dcc.Slider(id=NUM_POINTS,
                                     min=USER_INPUT[NUM_POINTS]['min'],
                                     max=USER_INPUT[NUM_POINTS]['max'],
                                     step=USER_INPUT[NUM_POINTS]['step'],
                                     value=USER_INPUT[NUM_POINTS]['init'],
                                     marks=None,
                                     tooltip={'template': '{value}'}
                                     ),
                          dcc.Markdown(id=FUNC_DISPLAY,
                                       mathjax=True,
                                       style={'text-align': 'center'}
                                       ),
                          dcc.Graph(id=FIG_ID,
                                    figure=make_figure()[0],
                                    mathjax=True
                                    )
                      ])
    app.layout = layout
    return

if __name__ == '__main__':
    run_app()