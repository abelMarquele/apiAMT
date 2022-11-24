import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
from django.utils.translation import gettext, gettext_lazy
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot


# app = DjangoDash('SimpleExample')

# app.layout = html.Div([
#     dcc.RadioItems(
#         id='dropdown-color',
#         options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
#         value='red'
#     ),
#     html.Div(id='output-color'),
#     dcc.RadioItems(
#         id='dropdown-size',
#         options=[{'label': i, 'value': j} for i, j in [('L', gettext('large')),
#                                                        ('M', gettext_lazy('medium')),
#                                                        ('S', 'small')]],
#         value='medium'
#     ),
#     html.Div(id='output-size')

# ])

# @app.callback(
#     dash.dependencies.Output('output-color', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value')])
# def callback_color(dropdown_value):
#     'Change output message'
#     return "The selected color is %s." % dropdown_value

# @app.callback(
#     dash.dependencies.Output('output-size', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value'),
#      dash.dependencies.Input('dropdown-size', 'value')])
# def callback_size(dropdown_color, dropdown_size):
#     'Change output message'
#     return "The chosen T-shirt is a %s %s one." %(dropdown_size,
#                                                   dropdown_color)

def monthly_plot(connection):

    qs = connection
    corridor_data = [
        {
            "Data": x.date,
            "Bilhetes QR": x.qr_ticket_count,
        } for x in qs 
    ]
    df = pd.DataFrame(corridor_data)
    
    fig = go.Figure(data = go.Bar(
        df,
        x="Data",
        y="Bilhetes QR"
        ))

    #Update layout for graph object Figure
    fig.update_layout(barmode='stack', 
                      title_text = 'Daily Cases By Gender',
                      paper_bgcolor = 'rgba(0,0,0,0)', 
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      xaxis_title = 'Date',
                      yaxis_title = 'Daily_Cases')
    
    #Turn graph object into local plotly graph
    monthly_plot = plot({'data': fig}, output_type='div')

    return monthly_plot