import datetime
import dash
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from dash import dcc, html
from django_plotly_dash import DjangoDash
from django.utils.translation import gettext, gettext_lazy
from conductor_sales_report.models import conductor_sales_report

from corridor_performance_report.models import corridor_performance_report
from index_translation.models import Cooperative
from django.db.models import Sum, Max, F

class query_connect:
    conn = corridor_performance_report.objects.all().select_related('cooperative').values('date','cooperative').annotate(
                    qr_ticket_count=Sum('qr_ticket_count'),
                    passenger_count=Sum('passenger_count'),
            )
    
    conn1 =  Cooperative.objects.values('cooperative').distinct()

    conn2 = conductor_sales_report.objects.all().values('date').annotate(
                    number=Sum('number'),
            )
    conn3 = conductor_sales_report.objects.all().values('date').annotate(
        date_year= Max('date__year')
    )
    

def cooperative_plotly(connection):
  
    cooperative_options = pd.DataFrame(connection)

    return cooperative_options

def conductor_plotly(connection):
  
    conductor_options = pd.DataFrame(connection)

    # print('conductor_options', conductor_options['date_year'].drop_duplicates())

    return conductor_options


request_corridor_connection = query_connect.conn
request_cooperative_connection = query_connect.conn1
request_conductor_connection = query_connect.conn2
request_conductor_date_connection = query_connect.conn3

cooperative_options = cooperative_plotly(request_cooperative_connection)
conductor_date_options = conductor_plotly(request_conductor_date_connection)


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
                                style={'height': '100%', 'margin':'0px auto'}),
                            html.Div([                 
                                    dcc.Graph(id = 'vacc_plot', 
                                        animate = True, 
                                        # style={'width': '100%', "backgroundColor": "#FFF0F5"}
                                        ),
                                        

                                    dcc.Graph(id = 'vacc_plot1', 
                                        animate = True, 
                                        # style={"backgroundColor": "#FFF0F5"}
                                        )

                                    ])
                                    
                        
                        ]) # end of 'main'

@dash_example1.expanded_callback(
    dash.dependencies.Output('vacc_plot', 'figure'),
    [dash.dependencies.Input('brand', 'value')])


def callback_test(value):
    children = vacc_brand_plotly(request_corridor_connection, value)
    return children


def vacc_brand_plotly(request_corridor_connection, brand):

    conn1 = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')

    df_conn1 = pd.DataFrame(conn1)
    # print('cooperative 1: ',df_conn)
    cells = list(df_conn1['id'])

    df = pd.DataFrame(request_corridor_connection)
    # print('df: ',df)


    df = df.query("cooperative in @cells")
    # print('depois1: ',df)

    children = go.Figure(data = [
                            go.Histogram( name = 'date', x= df['date'], y= df['qr_ticket_count']),
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

    conn1 = Cooperative.objects.filter(cooperative=brand).values('id','cooperative')  

    df_conn1 = pd.DataFrame(conn1)
    # print('cooperative 2: ',df_conn)
    cells = list(df_conn1['id'])

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
                                dcc.RangeSlider(
                                                id='brand11',
                                                min = conductor_date_options['date_year'].min()-1,
                                                max = conductor_date_options['date_year'].max()+1,
                                                step = 2,
                                                tooltip ={'always visible': False, 
                                                'placement':'bottom'},
                                                marks = {i: '{}'.format(i) for i in conductor_date_options['date_year']},
                                                value=[conductor_date_options['date_year'].min(), conductor_date_options['date_year'].max()]
                                                )


                                ],
                                # className='col-md-12',
                                style={'width': '75%', 'margin':'0px auto'}),
                            html.Div([                 
                                    dcc.Graph(id = 'vacc_plot11', 
                                        animate = True, 
                                        # style={"backgroundColor": "#FFF0F5"}
                                        ),
                                        

                                    dcc.Graph(id = 'vacc_plot111', 
                                        animate = True, 
                                        # style={"backgroundColor": "#FFF0F5"}
                                        )

                                    ])
                                    
                        
                        ]) # end of 'main'

@dash_example11.expanded_callback(
    dash.dependencies.Output('vacc_plot11', 'figure'),
    [dash.dependencies.Input('brand11', 'value')])


def callback_test(value):
    children = vacc_brand_plotly11(request_corridor_connection, value)
    return children


def vacc_brand_plotly11(request_corridor_connection, brand11):

    start_year_value = pd.Timestamp(brand11[0], 1, 1)
    end_year_value = pd.Timestamp(brand11[1], 1, 1)
    

    df = pd.DataFrame(request_corridor_connection)

    df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]

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


@dash_example11.expanded_callback(
    dash.dependencies.Output('vacc_plot111', 'figure'),
    [dash.dependencies.Input('brand11', 'value')])


def display_value(value):
    children = vacc_brand_plotly22(request_conductor_connection, value)
    return children


def vacc_brand_plotly22(request_conductor_connection, brand11):

    start_year_value = pd.Timestamp(brand11[0], 1, 1)
    end_year_value = pd.Timestamp(brand11[1], 1, 1)
    

    df = pd.DataFrame(request_conductor_connection)

    df = df.loc[(df['date'] >= start_year_value) & (df['date'] <= end_year_value)]

    children = go.Figure(data = [
                            go.Scatter( name = 'Passageiro QR', x= df['date'], y= df['number']),
                            go.Scatter( name = 'Camisão QR', x= df['date'], y= (df['number']*1.5)),
       ])
    
    children.update_layout(barmode='stack', 
                      title_text = 'Passageiros e Camisão QR por Data',
                      paper_bgcolor = 'rgba(0,0,0,0)', 
                      plot_bgcolor = 'rgba(0,0,0,0)',
                      xaxis_title = 'Date',
                      yaxis_title = 'Passageiros e Camisão QR')
    
    return children

    