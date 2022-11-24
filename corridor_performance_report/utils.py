import dash
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from dash import dcc, html
from django_plotly_dash import DjangoDash
from django.utils.translation import gettext, gettext_lazy

from corridor_performance_report.models import corridor_performance_report
from index_translation.models import Cooperative
from django.db.models import Sum
import numpy as np

class cooperative_connect:
    conn =  Cooperative.objects.values('cooperative').distinct()
    # print(conn.cooperative)

class corridor_connect:
    conn = corridor_performance_report.objects.all().select_related('cooperative').values('date','cooperative').annotate(
                    qr_ticket_count=Sum('qr_ticket_count'),
                    passenger_count=Sum('passenger_count'),
            )
    

def cooperative_plotly(connection):
  
    cooperative_options = pd.DataFrame(connection)

    return cooperative_options


request_cooperative_connection = cooperative_connect.conn
request_corridor_connection = corridor_connect.conn
cooperative_options = cooperative_plotly(request_cooperative_connection)


dash_example1 = DjangoDash('dash_example1'
                          )
dash_example1.layout = html.Div([
                        html.Div([ 

                            #Add dropdown for option selection
                                dcc.Dropdown(
                                id='brand',
                                options = [{'label': i, 'value': i} for i in cooperative_options['cooperative']],
                                value='COOPTRANS')],
                                # className='col-md-12',
                                style={'width': '75%', 'margin':'0px auto'}),
                            html.Div([                 
                                    dcc.Graph(id = 'vacc_plot', 
                                        animate = True, 
                                        style={"backgroundColor": "#FFF0F5"}),
                                        

                                    dcc.Graph(id = 'vacc_plot1', 
                                        animate = True, 
                                        style={"backgroundColor": "#FFF0F5"})

                                    ])
                                    
                        
                        ]) # end of 'main'

@dash_example1.expanded_callback(
    dash.dependencies.Output('vacc_plot', 'figure'),
    [dash.dependencies.Input('brand', 'value')])


def callback_test(value):
    children = vacc_brand_plotly(request_corridor_connection, value)
    return children


def vacc_brand_plotly(request_corridor_connection, brand):

    conn = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')

    df_conn = pd.DataFrame(conn)
    # print('cooperative 1: ',df_conn)
    cells = list(df_conn['id'])

    df = pd.DataFrame(request_corridor_connection)
    # print('df: ',df)


    df = df.query("cooperative in @cells")
    # print('depois1: ',df)

    children = go.Figure(data = [
                            go.Scatter( name = 'date', x= df['date'], y= df['qr_ticket_count']),
       ])
    

    children.update_layout(barmode='stack', 
                      title_text = 'Bilhetes de QR por Data',
                      paper_bgcolor = 'rgba(0,0,0,0)', 
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      xaxis_title = 'Date',
                      yaxis_title = 'Bilhetes de QR')
    
    return children

# --------------?--------?---------------------------------------------------------------------------------------------


@dash_example1.expanded_callback(
    dash.dependencies.Output('vacc_plot1', 'figure'),
    [dash.dependencies.Input('brand', 'value')])


def display_value(value):
    children = vacc_brand_plotly2(request_corridor_connection, value)
    return children


def vacc_brand_plotly2(request_corridor_connection, brand):

    conn = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')  

    df_conn = pd.DataFrame(conn)
    # print('cooperative 2: ',df_conn)
    cells = list(df_conn['id'])

    df = pd.DataFrame(request_corridor_connection)

    df = df.query("cooperative in @cells")
    # print('depois2: ',df)

    children = go.Figure(data = [
                            go.Scatter( name = 'date', x= df['date'], y= df['passenger_count']),
       ])
    

    children.update_layout(barmode='stack', 
                      title_text = 'Validadores do sistema por Data',
                      paper_bgcolor = 'rgba(0,0,0,0)', 
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      xaxis_title = 'Date',
                      yaxis_title = 'Validadores do sistema')
    
    return children

    

# *************************************************************************************************************************

dash_example11 = DjangoDash('dash_example11'
                          )
dash_example11.layout = html.Div([
                        html.Div([ 

                            #Add dropdown for option selection
                                dcc.Dropdown(
                                id='brand',
                                options = [{'label': i, 'value': i} for i in cooperative_options['cooperative']],
                                value='COOPTRANS')],
                                # className='col-md-12',
                                style={'width': '75%', 'margin':'0px auto'}),
                            html.Div([                 
                                    dcc.Graph(id = 'vacc_plot11', 
                                        animate = True, 
                                        style={"backgroundColor": "#FFF0F5"}),
                                        

                                    # dcc.Graph(id = 'vacc_plot1', 
                                    #     animate = True, 
                                    #     style={"backgroundColor": "#FFF0F5"})

                                    ])
                                    
                        
                        ]) # end of 'main'

@dash_example11.expanded_callback(
    dash.dependencies.Output('vacc_plot11', 'figure'),
    [dash.dependencies.Input('brand', 'value')])


def callback_test(value):
    children = vacc_brand_plotly11(request_corridor_connection, value)
    return children


def vacc_brand_plotly11(request_corridor_connection, brand):

    conn = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')

    df_conn = pd.DataFrame(conn)
    # print('cooperative 1: ',df_conn)
    cells = list(df_conn['id'])

    df = pd.DataFrame(request_corridor_connection)
    # print('df: ',df)


    df = df.query("cooperative in @cells")
    print('Multiplicacao: ',(df['passenger_count']-df['qr_ticket_count']))

    children = go.Figure(data = [
                            go.Scatter( name = 'Passageiro Cartão', x= df['date'], y= (df['passenger_count']-df['qr_ticket_count'])),
                            go.Scatter( name = 'Camisão Cartão', x= df['date'], y= ((df['passenger_count']-df['qr_ticket_count'])*1.5)),
       ])
    

    children.update_layout(barmode='stack', 
                      title_text = 'Passageiros e Camisão Cartão por Data',
                      paper_bgcolor = 'rgba(0,0,0,0)', 
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      xaxis_title = 'Date',
                      yaxis_title = 'Passageiros e Camisão Cartão')
    
    return children

# --------------?--------?---------------------------------------------------------------------------------------------


# @dash_example1.expanded_callback(
#     dash.dependencies.Output('vacc_plot1', 'figure'),
#     [dash.dependencies.Input('brand', 'value')])


# def display_value(value):
#     children = vacc_brand_plotly2(request_corridor_connection, value)
#     return children


# def vacc_brand_plotly2(request_corridor_connection, brand):

#     conn = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')  

#     df_conn = pd.DataFrame(conn)
#     # print('cooperative 2: ',df_conn)
#     cells = list(df_conn['id'])

#     df = pd.DataFrame(request_corridor_connection)

#     df = df.query("cooperative in @cells")
#     # print('depois2: ',df)

#     children = go.Figure(data = [
#                             go.Bar( name = 'date', x= df['date'], y= df['passenger_count']),
#        ])
    

#     children.update_layout(barmode='stack', 
#                       title_text = 'Validadores do sistema por Data',
#                       paper_bgcolor = 'rgba(0,0,0,0)', 
#                       plot_bgcolor = 'rgba(0,0,0,0)',
#                       xaxis_title = 'Date',
#                       yaxis_title = 'Validadores do sistema')
    
#     return children

    