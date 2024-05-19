# import datetime
# import dash
# import pandas as pd
# import plotly.graph_objs as go
# from dash import dcc, html
# from django_plotly_dash import DjangoDash
# from django.utils.translation import gettext, gettext_lazy
# from conductor_sales_report.models import conductor_sales_report
# from corridor_performance_report.models import corridor_performance_report
# from index_translation.models import Cooperative
# from django.db.models import Sum, Max, F

# class query_connect:
#     conn = corridor_performance_report.objects.all().select_related('cooperative').values('date', 'cooperative').annotate(
#         qr_ticket_count=Sum('qr_ticket_count'),
#         passenger_count=Sum('passenger_count'),
#     )
    
#     conn1 = Cooperative.objects.values('cooperative').distinct()

#     conn2 = conductor_sales_report.objects.all().values('date').annotate(
#         number=Sum('number'),
#     )
#     conn3 = conductor_sales_report.objects.all().values('date').annotate(
#         date_year=Max('date__year')
#     )

# def cooperative_plotly(connection):
#     cooperative_options = pd.DataFrame(connection)
#     print("Cooperative options DataFrame:")
#     print(cooperative_options.head())
#     return cooperative_options

# def conductor_plotly(connection):
#     conductor_options = pd.DataFrame(connection)
#     print("Conductor options DataFrame:")
#     print(conductor_options.head())
#     return conductor_options

# request_corridor_connection = query_connect.conn
# request_cooperative_connection = query_connect.conn1
# request_conductor_connection = query_connect.conn2
# request_conductor_date_connection = query_connect.conn3

# cooperative_options = cooperative_plotly(request_cooperative_connection)
# conductor_date_options = conductor_plotly(request_conductor_date_connection)

# # Definindo o tema para os gráficos
# theme = {
#     'plot_bgcolor': '#f9f9f9',
#     'paper_bgcolor': '#f9f9f9',
#     'title_font_color': '#333',
#     'font_color': '#333',
#     'font_family': 'Arial, sans-serif',
# }

# # Função para criar um layout de gráfico padronizado
# def create_layout(title, xaxis_title, yaxis_title):
#     return go.Layout(
#         title=title,
#         plot_bgcolor=theme['plot_bgcolor'],
#         paper_bgcolor=theme['paper_bgcolor'],
#         title_font=dict(color=theme['title_font_color'], size=20),
#         font=dict(color=theme['font_color'], family=theme['font_family']),
#         xaxis=dict(title=xaxis_title, title_font=dict(size=14), tickfont=dict(size=12)),
#         yaxis=dict(title=yaxis_title, title_font=dict(size=14), tickfont=dict(size=12)),
#         margin=dict(l=40, r=40, t=40, b=40),
#         hovermode="closest",
#     )

# dash_example1 = DjangoDash('dash_example1')
# dash_example1.layout = html.Div([
#     html.Div([ 
#         dcc.Dropdown(
#             id='brand',
#             options=[{'label': i, 'value': i} for i in cooperative_options['cooperative']] if 'cooperative' in cooperative_options.columns else [],
#             value='COOPTRANS',
#             style={'width': '50%', 'margin': '0 auto'}
#         )],
#         style={'padding': '20px'}
#     ),
#     html.Div([
#         html.Div([
#             dcc.Graph(id='vacc_plot', animate=True)
#         ], style={'width': '48%', 'display': 'inline-block'}),
#         html.Div([
#             dcc.Graph(id='vacc_plot1', animate=True)
#         ], style={'width': '48%', 'display': 'inline-block'})
#     ])
# ])

# @dash_example1.expanded_callback(
#     dash.dependencies.Output('vacc_plot', 'figure'),
#     [dash.dependencies.Input('brand', 'value')]
# )
# def callback_test(value):
#     children = vacc_brand_plotly(request_corridor_connection, value)
#     return children

# def vacc_brand_plotly(request_corridor_connection, brand):
#     conn1 = Cooperative.objects.filter(cooperative=brand).values('id', 'cooperative')
#     df_conn1 = pd.DataFrame(conn1)
#     cells = list(df_conn1['id'])

#     df = pd.DataFrame(request_corridor_connection)
#     df = df.query("cooperative in @cells")

#     children = go.Figure(data=[
#         go.Histogram(name='QR Tickets', x=df['date'], y=df['qr_ticket_count'], marker=dict(color='blue'))
#     ])

#     children.update_layout(create_layout('Bilhetes de QR por Data', 'Data', 'Bilhetes de QR'))
    
#     return children

# @dash_example1.expanded_callback(
#     dash.dependencies.Output('vacc_plot1', 'figure'),
#     [dash.dependencies.Input('brand', 'value')]
# )
# def display_value(value):
#     children = vacc_brand_plotly2(request_corridor_connection, value)
#     return children

# def vacc_brand_plotly2(request_corridor_connection, brand):
#     conn1 = Cooperative.objects.filter(cooperative=brand).values('id', 'cooperative')  
#     df_conn1 = pd.DataFrame(conn1)
#     cells = list(df_conn1['id'])

#     df = pd.DataFrame(request_corridor_connection)
#     df = df.query("cooperative in @cells")

#     children = go.Figure(data=[
#         go.Scatter(name='Passenger Count', x=df['date'], y=df['passenger_count'], mode='lines+markers', marker=dict(color='green'))
#     ])

#     children.update_layout(create_layout('Validadores do sistema por Data', 'Data', 'Validadores do sistema'))
    
#     return children

# dash_example11 = DjangoDash('dash_example11')
# dash_example11.layout = html.Div([
#     html.Div([ 
#         dcc.RangeSlider(
#             id='brand11',
#             min=conductor_date_options['date_year'].min()-1 if 'date_year' in conductor_date_options.columns else 0,
#             max=conductor_date_options['date_year'].max()+1 if 'date_year' in conductor_date_options.columns else 0,
#             step=1,
#             tooltip={'always visible': False, 'placement': 'bottom'},
#             marks={i: '{}'.format(i) for i in conductor_date_options['date_year']} if 'date_year' in conductor_date_options.columns else {},
#             value=[
#                 conductor_date_options['date_year'].min() if 'date_year' in conductor_date_options.columns else 0,
#                 conductor_date_options['date_year'].max() if 'date_year' in conductor_date_options.columns else 0
#             ]
#         )
#     ], style={'width': '75%', 'margin': '0 auto', 'padding': '20px'}
#     ),
#     html.Div([
#         html.Div([
#             dcc.Graph(id='vacc_plot11', animate=True)
#         ], style={'width': '48%', 'display': 'inline-block'}),
#         html.Div([
#             dcc.Graph(id='vacc_plot111', animate=True)
#         ], style={'width': '48%', 'display': 'inline-block'})
#     ])
# ])

# @dash_example11.expanded_callback(
#     dash.dependencies.Output('vacc_plot11', 'figure'),
#     [dash.dependencies.Input('brand11', 'value')]
# )
# def callback_test(value):
#     children = vacc_brand_plotly11(request_corridor_connection, value)
#     return children

# def vacc_brand_plotly11(request_corridor_connection, brand11):
#     start_year_value = pd.Timestamp(brand11[0], 1, 1)
#     end_year_value = pd.Timestamp(brand11[1], 12, 31)

#     df = pd.DataFrame(request_corridor_connection)
#     df['date'] = pd.to_datetime(df['date'])  # Converter 'date' para datetime

#     print("DataFrame before filtering for vacc_plot11:")
#     print(df.head())

#     df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]
#     print("DataFrame after filtering for vacc_plot11:")
#     print(df.head())

#     children = go.Figure(data=[
#         go.Scatter(name='Passageiro Cartão', x=df['date'], y=(df['passenger_count'] - df['qr_ticket_count']), mode='lines+markers', marker=dict(color='orange')),
#         go.Scatter(name='Camisão Cartão', x=df['date'], y=((df['passenger_count'] - df['qr_ticket_count']) * 1.5), mode='lines+markers', marker=dict(color='red'))
#     ])

#     children.update_layout(create_layout('Passageiros e Camisão Cartão por Data', 'Data', 'Passageiros e Camisão Cartão'))
    
#     return children

# @dash_example11.expanded_callback(
#     dash.dependencies.Output('vacc_plot111', 'figure'),
#     [dash.dependencies.Input('brand11', 'value')]
# )
# def display_value(value):
#     children = vacc_brand_plotly22(request_conductor_connection, value)
#     return children

# def vacc_brand_plotly22(request_conductor_connection, brand11):
#     start_year_value = pd.Timestamp(brand11[0], 1, 1)
#     end_year_value = pd.Timestamp(brand11[1], 12, 31)

#     df = pd.DataFrame(request_conductor_connection)
#     df['date'] = pd.to_datetime(df['date'])  # Converter 'date' para datetime

#     print("DataFrame before filtering for vacc_plot111:")
#     print(df.head())

#     df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]
#     print("DataFrame after filtering for vacc_plot111:")
#     print(df.head())

#     children = go.Figure(data=[
#         go.Scatter(name='Passageiro QR', x=df['date'], y=df['number'], mode='lines+markers', marker=dict(color='purple')),
#         go.Scatter(name='Camisão QR', x=df['date'], y=(df['number'] * 1.5), mode='lines+markers', marker=dict(color='blue'))
#     ])

#     children.update_layout(create_layout('Passageiros e Camisão QR por Data', 'Data', 'Passageiros e Camisão QR'))
    
#     return children



import datetime
import dash
import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html
from django_plotly_dash import DjangoDash
from django.utils.translation import gettext, gettext_lazy
from conductor_sales_report.models import conductor_sales_report
from corridor_performance_report.models import corridor_performance_report
from index_translation.models import Cooperative
from django.db.models import Sum, Max, F

class query_connect:
    conn = corridor_performance_report.objects.all().select_related('cooperative').values('date', 'cooperative').annotate(
        qr_ticket_count=Sum('qr_ticket_count'),
        passenger_count=Sum('passenger_count'),
    )
    
    conn1 = Cooperative.objects.values('cooperative').distinct()

    conn2 = conductor_sales_report.objects.all().values('date').annotate(
        number=Sum('number'),
    )
    conn3 = conductor_sales_report.objects.all().values('date').annotate(
        date_year=Max('date__year')
    )

def cooperative_plotly(connection):
    cooperative_options = pd.DataFrame(connection)
    print("Cooperative options DataFrame:")
    print(cooperative_options.head())
    return cooperative_options

def conductor_plotly(connection):
    conductor_options = pd.DataFrame(connection)
    print("Conductor options DataFrame:")
    print(conductor_options.head())
    return conductor_options

request_corridor_connection = query_connect.conn
request_cooperative_connection = query_connect.conn1
request_conductor_connection = query_connect.conn2
request_conductor_date_connection = query_connect.conn3

cooperative_options = cooperative_plotly(request_cooperative_connection)
conductor_date_options = conductor_plotly(request_conductor_date_connection)

dash_example1 = DjangoDash('dash_example1')
dash_example1.layout = html.Div([
    html.Div([ 
        dcc.Dropdown(
            id='brand',
            options=[{'label': i, 'value': i} for i in cooperative_options['cooperative']] if 'cooperative' in cooperative_options.columns else [],
            value='COOPTRANS'
        )],
        style={'height': '100%', 'margin': '0px auto'}
    ),
    html.Div([                 
        dcc.Graph(id='vacc_plot', animate=True),
        dcc.Graph(id='vacc_plot1', animate=True)
    ])
])

@dash_example1.expanded_callback(
    dash.dependencies.Output('vacc_plot', 'figure'),
    [dash.dependencies.Input('brand', 'value')]
)
def callback_test(value):
    children = vacc_brand_plotly(request_corridor_connection, value)
    return children

def vacc_brand_plotly(request_corridor_connection, brand):
    conn1 = Cooperative.objects.filter(cooperative=brand).values('id', 'cooperative')
    df_conn1 = pd.DataFrame(conn1)
    cells = list(df_conn1['id'])

    df = pd.DataFrame(request_corridor_connection)
    df = df.query("cooperative in @cells")

    children = go.Figure(data=[
        go.Histogram(name='date', x=df['date'], y=df['qr_ticket_count'])
    ])

    children.update_layout(
        barmode='stack', 
        title_text='Bilhetes de QR por Data',
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Date',
        yaxis_title='Bilhetes de QR'
    )
    
    return children

@dash_example1.expanded_callback(
    dash.dependencies.Output('vacc_plot1', 'figure'),
    [dash.dependencies.Input('brand', 'value')]
)
def display_value(value):
    children = vacc_brand_plotly2(request_corridor_connection, value)
    return children

def vacc_brand_plotly2(request_corridor_connection, brand):
    conn1 = Cooperative.objects.filter(cooperative=brand).values('id', 'cooperative')  
    df_conn1 = pd.DataFrame(conn1)
    cells = list(df_conn1['id'])

    df = pd.DataFrame(request_corridor_connection)
    df = df.query("cooperative in @cells")

    children = go.Figure(data=[
        go.Scatter(name='date', x=df['date'], y=df['passenger_count'])
    ])

    children.update_layout(
        barmode='stack', 
        title_text='Validadores do sistema por Data',
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Date',
        yaxis_title='Validadores do sistema'
    )
    
    return children

dash_example11 = DjangoDash('dash_example11')
dash_example11.layout = html.Div([
    html.Div([ 
        dcc.RangeSlider(
            id='brand11',
            min=conductor_date_options['date_year'].min()-1 if 'date_year' in conductor_date_options.columns else 0,
            max=conductor_date_options['date_year'].max()+1 if 'date_year' in conductor_date_options.columns else 0,
            step=1,
            tooltip={'always visible': False, 'placement': 'bottom'},
            marks={i: '{}'.format(i) for i in conductor_date_options['date_year']} if 'date_year' in conductor_date_options.columns else {},
            value=[
                conductor_date_options['date_year'].min() if 'date_year' in conductor_date_options.columns else 0,
                conductor_date_options['date_year'].max() if 'date_year' in conductor_date_options.columns else 0
            ]
        )
    ], style={'width': '75%', 'margin': '0px auto'}),
    html.Div([                 
        dcc.Graph(id='vacc_plot11', animate=True),
        dcc.Graph(id='vacc_plot111', animate=True)
    ])
])

@dash_example11.expanded_callback(
    dash.dependencies.Output('vacc_plot11', 'figure'),
    [dash.dependencies.Input('brand11', 'value')]
)
def callback_test(value):
    children = vacc_brand_plotly11(request_corridor_connection, value)
    return children

def vacc_brand_plotly11(request_corridor_connection, brand11):
    start_year_value = pd.Timestamp(brand11[0], 1, 1)
    end_year_value = pd.Timestamp(brand11[1], 12, 31)

    df = pd.DataFrame(request_corridor_connection)
    df['date'] = pd.to_datetime(df['date'])  # Converter 'date' para datetime

    print("DataFrame before filtering for vacc_plot11:")
    print(df.head())

    df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]
    print("DataFrame after filtering for vacc_plot11:")
    print(df.head())

    children = go.Figure(data=[
        go.Scatter(name='Passageiro Cartão', x=df['date'], y=(df['passenger_count'] - df['qr_ticket_count'])),
        go.Scatter(name='Camisão Cartão', x=df['date'], y=((df['passenger_count'] - df['qr_ticket_count']) * 1.5))
    ])

    children.update_layout(
        barmode='stack', 
        title_text='Passageiros e Camisão Cartão por Data',
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Date',
        yaxis_title='Passageiros e Camisão Cartão'
    )
    
    return children

@dash_example11.expanded_callback(
    dash.dependencies.Output('vacc_plot111', 'figure'),
    [dash.dependencies.Input('brand11', 'value')]
)
def display_value(value):
    children = vacc_brand_plotly22(request_conductor_connection, value)
    return children

def vacc_brand_plotly22(request_conductor_connection, brand11):
    start_year_value = pd.Timestamp(brand11[0], 1, 1)
    end_year_value = pd.Timestamp(brand11[1], 12, 31)

    df = pd.DataFrame(request_conductor_connection)
    df['date'] = pd.to_datetime(df['date'])  # Converter 'date' para datetime

    print("DataFrame before filtering for vacc_plot111:")
    print(df.head())

    df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]
    print("DataFrame after filtering for vacc_plot111:")
    print(df.head())

    children = go.Figure(data=[
        go.Scatter(name='Passageiro QR', x=df['date'], y=df['number']),
        go.Scatter(name='Camisão QR', x=df['date'], y=(df['number'] * 1.5))
    ])

    children.update_layout(
        barmode='stack', 
        title_text='Passageiros e Camisão QR por Data',
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Date',
        yaxis_title='Passageiros e Camisão QR'
    )
    
    return children
