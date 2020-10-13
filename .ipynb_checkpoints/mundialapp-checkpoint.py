#IMPORTACIÓN DE RECURSOS PARA EL SERVER
import dash   # Servidor Flask
import dash_core_components as dcc  # Graficacion
import dash_html_components as html # HTML

#***************************************** SECCION I *********************************************************

#IMPORTAMOS VARIABLES DE INDIA DE COVMUN
from covmun import confirmados_india, muertes_india, fechas_india, total_confirmados_india, total_muertes_india, desvest_india_c, desvest_india_m, mediana_india_c, mediana_india_m, media_india_c, media_india_m
#IMPORTAMOS VARIABLES DE ANDORRA DE COVMUN
from covmun import confirmados_andorra, muertes_andorra, fechas_andorra, total_confirmados_andorra, total_muertes_andorra, desvest_andorra_c, desvest_andorra_m, mediana_andorra_c, mediana_andorra_m, media_andorra_c, media_andorra_m 
#IMPORTAMOS VARIABLES DE QATAR DE COVMUN
from covmun import confirmados_qatar, muertes_qatar, fechas_qatar, total_confirmados_qatar, total_muertes_qatar, desvest_qatar_c, desvest_qatar_m, mediana_qatar_c, mediana_qatar_m, media_qatar_c, media_qatar_m 
#IMPORTAMOS VARIABLES DE BURUNDI DE COVMUN
from covmun import confirmados_burundi, muertes_burundi, fechas_burundi, total_confirmados_burundi, total_muertes_burundi, desvest_burundi_c, desvest_burundi_m, mediana_burundi_c, mediana_burundi_m, media_burundi_c, media_burundi_m 

#***************************************** SECCION II *********************************************************

#IMPORTAMOS VARIABLES DE NIGERIA DE COVMUN
from covmun import confirmados_nigeria, muertes_nigeria, fechas_nigeria, total_confirmados_nigeria, total_muertes_nigeria, desvest_nigeria_c, desvest_nigeria_m, mediana_nigeria_c, mediana_nigeria_m, media_nigeria_c, media_nigeria_m
#IMPORTAMOS VARIABLES DE MONACO DE COVMUN
from covmun import confirmados_monaco, muertes_monaco, fechas_monaco, total_confirmados_monaco, total_muertes_monaco, desvest_monaco_c, desvest_monaco_m, mediana_monaco_c, mediana_monaco_m, media_monaco_c, media_monaco_m
#IMPORTAMOS VARIABLES DE UCRANIA DE COVMUN
from covmun import confirmados_ukraine, muertes_ukraine, fechas_ukraine, total_confirmados_ukraine, total_muertes_ukraine, desvest_ukraine_c, desvest_ukraine_m, mediana_ukraine_c, mediana_ukraine_m, media_ukraine_c, media_ukraine_m 
#IMPORTAMOS VARIABLES DE OMAN DE COVMUN
from covmun import confirmados_oman, muertes_oman, fechas_oman, total_confirmados_oman, total_muertes_oman, desvest_oman_c, desvest_oman_m, mediana_oman_c, mediana_oman_m, media_oman_c, media_oman_m
#IMPORTAMOS VARIABLES DE LIBIA DE COVMUN
from covmun import confirmados_libya, muertes_libya, fechas_libya, total_confirmados_libya, total_muertes_libya, desvest_libya_c, desvest_libya_m, mediana_libya_c, mediana_libya_m, media_libya_c, media_libya_m

app = dash.Dash(__name__)
server = app.server

colors = {
   'fondo': "#FDFEFE",
    'texto': "#21618C"
}

#SECCIÓN ENCABEZADO
app.layout = html.Div(style={'backgroundColor': colors['fondo']}, children=[
    html.H1(
        children=["2020: Contraste casos COVID-19 en el mundo"],
        style={
            'textAlign': 'center',
            'color': colors['texto'],
            "font-size": 50
        }
    ),
    #SECCIÓN INDIA-ANDORRA PAISES CON MAYOR Y MENOR POBLACIÓN
    dcc.Graph(
        id="india_andorra",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_india[:-1], 'type': 'line', 'name': 'Confirmados India'},
                {'x': fechas_india[:-1], 'y': muertes_india[:-1], 'type': 'line', 'name': 'Muertes India'},
                {'x': fechas_andorra[:-1], 'y': confirmados_andorra[:-1], 'type': 'line', 'name': 'Confirmados Andorra'},
                {'x': fechas_andorra[:-1], 'y': muertes_andorra[:-1], 'type': 'line', 'name': 'Muertes Andorra'},
            ],
            'layout': {
                'title': 'Análisis de dos de los países con mayor (India) y menor población (Andorra)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    dcc.Graph(
        id="comp1",
        figure={
            'data': [
                {'y': total_confirmados_india, 'type': 'bar', 'name': 'Confirmados India'},
                {'y': total_confirmados_andorra, 'type': 'bar', 'name': 'Confirmados Andorra'},  
                {'y': total_muertes_india, 'type': 'bar', 'name': 'Muertes India'},
                {'y': total_muertes_andorra, 'type': 'bar', 'name': 'Muertes Andorra'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes (India y Andorra)',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(    
        id="Estadisticos1",
        figure={
            'data': [
                {'y':  desvest_india_c, 'type': 'bar', 'name': 'DESVEST_INDIA_CONFIRMADOS'},
                {'y':  desvest_andorra_c, 'type': 'bar', 'name': 'DESVEST_ANDORRA_CONFIRMADOS'},
                {'y':  desvest_india_m, 'type': 'bar', 'name': 'DESVEST_INDIA_MUERTES'},  
                {'y':  desvest_andorra_m, 'type': 'bar', 'name': 'DESVEST_ANDORRA_MUERTES'}, 
                {'y':  mediana_india_c, 'type': 'bar', 'name': 'MEDIANA_INDIA_CONFIRMADOS'},
                {'y':  mediana_andorra_c, 'type': 'bar', 'name': 'MEDIANA_ANDORRA_CONFIRMADOS'},
                {'y':  mediana_india_m, 'type': 'bar', 'name': 'MEDIANA_INDIA_MUERTES'},
                {'y':  mediana_andorra_m, 'type': 'bar', 'name': 'MEDIANA_ADORRA_MUERTES'},
                {'y':  media_india_c, 'type': 'bar', 'name': 'MEDIA_INDIA_CONFIRMADOS'},
                {'y':  media_andorra_c, 'type': 'bar', 'name': 'MEDIA_ANDORRA_CONFIRMADOS'},
                {'y':  media_india_m, 'type': 'bar', 'name': 'MEDIA_INDIA_MUERTES'},
                {'y':  media_andorra_m, 'type': 'bar', 'name': 'MEDIA_ANDORRA_MUERTES'},
            ],
            'layout': {
                'title': 'Comparativo estadístico (India y Andorra)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(
        id="qatar_burundi",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_qatar[:-1], 'type': 'line', 'name': 'Confirmados Qatar'},
                {'x': fechas_india[:-1], 'y': muertes_qatar[:-1], 'type': 'line', 'name': 'Muertes Qatar'},
                {'x': fechas_andorra[:-1], 'y': confirmados_burundi[:-1], 'type': 'line', 'name': 'Confirmados Burundi'},
                {'x': fechas_andorra[:-1], 'y': muertes_burundi[:-1], 'type': 'line', 'name': 'Muertes Burundi'},  
            ],
            'layout': {
                'title': 'Análisis de dos de los países catalogados como el más rico (Qatar) y el más pobre (Burundi)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    dcc.Graph(  
        id="comp2",
        figure={
            'data': [
                {'y': total_confirmados_qatar, 'type': 'bar', 'name': 'Confirmados Qatar'},
                {'y': total_confirmados_burundi, 'type': 'bar', 'name': 'Confirmados Burundi'},  
                {'y': total_muertes_qatar, 'type': 'bar', 'name': 'Muertes Qatar'},
                {'y': total_muertes_burundi, 'type': 'bar', 'name': 'Muertes Burundi'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Qatar y Burundi',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(  
        id="Estadisticos2",
        figure={
            'data': [
                {'y':  desvest_qatar_c, 'type': 'bar', 'name': 'DESVEST_QATAR_CONFIRMADOS'},
                {'y':  desvest_burundi_c, 'type': 'bar', 'name': 'DESVEST_BURUNDI_CONFIRMADOS'},
                {'y':  desvest_qatar_m, 'type': 'bar', 'name': 'DESVEST_QATAR_MUERTES'},  
                {'y':  desvest_burundi_m, 'type': 'bar', 'name': 'DESVEST_BURUNDI_MUERTES'}, 
                {'y':  mediana_qatar_c, 'type': 'bar', 'name': 'MEDIANA_QATAR_CONFIRMADOS'},
                {'y':  mediana_burundi_c, 'type': 'bar', 'name': 'MEDIANA_BURUNDI_CONFIRMADOS'},
                {'y':  mediana_qatar_m, 'type': 'bar', 'name': 'MEDIANA_QATAR_MUERTES'},
                {'y':  mediana_burundi_m, 'type': 'bar', 'name': 'MEDIANA_BURUNDI_MUERTES'},
                {'y':  media_qatar_c, 'type': 'bar', 'name': 'MEDIA_QATAR_CONFIRMADOS'},
                {'y':  media_burundi_c, 'type': 'bar', 'name': 'MEDIA_BURUNDI_CONFIRMADOS'},
                {'y':  media_qatar_m, 'type': 'bar', 'name': 'MEDIA_QATAR_MUERTES'},
                {'y':  media_burundi_m, 'type': 'bar', 'name': 'MEDIA_BURUNDI_MUERTES'},
            ],
            'layout': {
                'title': 'Comparativo estadístico (Qatar y Burundi)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
# **************************************** SECCIÓN 2 **********************************************
    #SECCIÓN NIGERIA-MONACO PAISES CON MÁS GENTE JOVEN Y GENTE VIEJA
    dcc.Graph(
        id="nigeria_monaco",
        figure={
            'data': [
                {'x': fechas_nigeria[:-1], 'y': confirmados_nigeria[:-1], 'type': 'line', 'name': 'Confirmados Nigeria'},
                {'x': fechas_nigeria[:-1], 'y': muertes_nigeria[:-1], 'type': 'line', 'name': 'Muertes Nigeria'},
                {'x': fechas_monaco[:-1], 'y': confirmados_monaco[:-1], 'type': 'line', 'name': 'Confirmados Monaco'},
                {'x': fechas_monaco[:-1], 'y': muertes_monaco[:-1], 'type': 'line', 'name': 'Muertes Monaco'},
            ],
            'layout': {
                'title': 'Análisis de dos de los países con mayor población joven (Nigeria) y mayor población vieja (Monaco)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    dcc.Graph(
        id="comp3",
        figure={
            'data': [
                {'y': total_confirmados_nigeria, 'type': 'bar', 'name': 'Confirmados Nigeria'},
                {'y': total_confirmados_monaco, 'type': 'bar', 'name': 'Confirmados Monaco'},  
                {'y': total_muertes_nigeria, 'type': 'bar', 'name': 'Muertes Nigeria'},
                {'y': total_muertes_monaco, 'type': 'bar', 'name': 'Muertes Monaco'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes (Nigeria y Monaco)',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(    
        id="Estadisticos3",
        figure={
            'data': [
                {'y':  desvest_nigeria_c, 'type': 'bar', 'name': 'DESVEST_NIGERIA_CONFIRMADOS'},
                {'y':  desvest_monaco_c, 'type': 'bar', 'name': 'DESVEST_MONACO_CONFIRMADOS'},
                {'y':  desvest_nigeria_m, 'type': 'bar', 'name': 'DESVEST_NIGERIA_MUERTES'},  
                {'y':  desvest_monaco_m, 'type': 'bar', 'name': 'DESVEST_MONACO_MUERTES'}, 
                {'y':  mediana_nigeria_c, 'type': 'bar', 'name': 'MEDIANA_NIGERIA_CONFIRMADOS'},
                {'y':  mediana_monaco_c, 'type': 'bar', 'name': 'MEDIANA_MONACO_CONFIRMADOS'},
                {'y':  mediana_nigeria_m, 'type': 'bar', 'name': 'MEDIANA_NIGERIA_MUERTES'},
                {'y':  mediana_monaco_m, 'type': 'bar', 'name': 'MEDIANA_MONACO_MUERTES'},
                {'y':  media_nigeria_c, 'type': 'bar', 'name': 'MEDIA_NIGERIA_CONFIRMADOS'},
                {'y':  media_monaco_c, 'type': 'bar', 'name': 'MEDIA_MONACO_CONFIRMADOS'},
                {'y':  media_nigeria_m, 'type': 'bar', 'name': 'MEDIA_NIGERIA_MUERTES'},
                {'y':  media_monaco_m, 'type': 'bar', 'name': 'MEDIA_MONACO_MUERTES'},
            ],
            'layout': {
                'title': 'Comparativo estadístico (Nigeria y Monaco)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(
        id="ucrania_oman_libia",
        figure={
            'data': [
                {'x': fechas_ukraine[:-1], 'y': confirmados_ukraine[:-1], 'type': 'line', 'name': 'Confirmados Ucrania'},
                {'x': fechas_ukraine[:-1], 'y': muertes_ukraine[:-1], 'type': 'line', 'name': 'Muertes Ucrania'},
                {'x': fechas_oman[:-1], 'y': confirmados_oman[:-1], 'type': 'line', 'name': 'Confirmados Oman'},
                {'x': fechas_oman[:-1], 'y': muertes_oman[:-1], 'type': 'line', 'name': 'Muertes Oman'},  
                {'x': fechas_libya[:-1], 'y': confirmados_libya[:-1], 'type': 'line', 'name': 'Confirmados Libia'},
                {'x': fechas_libya[:-1], 'y': muertes_libya[:-1], 'type': 'line', 'name': 'Muertes Libia'},
            ],
            'layout': {
                'title': 'Análisis de dos de los países con más mujeres (Ucrania) y los paises con mas hombres (Oman, Libia)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    dcc.Graph(  
        id="comp4",
        figure={
            'data': [
                {'y': total_confirmados_ukraine, 'type': 'bar', 'name': 'Confirmados Ucrania'},
                {'y': total_confirmados_oman, 'type': 'bar', 'name': 'Confirmados Oman'},  
                {'y': total_confirmados_libya, 'type': 'bar', 'name': 'Confirmados Libia'},
                {'y': total_muertes_ukraine, 'type': 'bar', 'name': 'Muertes Ucrania'},
                {'y': total_muertes_oman, 'type': 'bar', 'name': 'Muertes Oman'},
                {'y': total_muertes_libya, 'type': 'bar', 'name': 'Muertes Libia'},
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Ucrania, Oman y Libia',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    dcc.Graph(  
        id="Estadisticos4",
        figure={
            'data': [
                {'y':  desvest_ukraine_c, 'type': 'bar', 'name': 'DESVEST_UCRANIA_CONFIRMADOS'},
                {'y':  desvest_oman_c, 'type': 'bar', 'name': 'DESVEST_OMAN_CONFIRMADOS'},
                {'y':  desvest_libya_c, 'type': 'bar', 'name': 'DESVEST_LIBIA_CONFIRMADOS'},
                
                {'y':  desvest_ukraine_m, 'type': 'bar', 'name': 'DESVEST_UCRANIA_MUERTES'},  
                {'y':  desvest_oman_m, 'type': 'bar', 'name': 'DESVEST_OMAN_MUERTES'}, 
                {'y':  desvest_libya_m, 'type': 'bar', 'name': 'DESVEST_LIBIA_MUERTES'}, 
                
                {'y':  mediana_ukraine_c, 'type': 'bar', 'name': 'MEDIANA_UCRANIA_CONFIRMADOS'},
                {'y':  mediana_oman_c, 'type': 'bar', 'name': 'MEDIANA_OMAN_CONFIRMADOS'},
                {'y':  mediana_libya_c, 'type': 'bar', 'name': 'MEDIANA_LIBIA_CONFIRMADOS'},
                
                {'y':  mediana_ukraine_m, 'type': 'bar', 'name': 'MEDIANA_UCRANIA_MUERTES'},
                {'y':  mediana_oman_m, 'type': 'bar', 'name': 'MEDIANA_OMAN_MUERTES'},
                {'y':  mediana_libya_m, 'type': 'bar', 'name': 'MEDIANA_LIBIA_MUERTES'},
                
                {'y':  media_ukraine_c, 'type': 'bar', 'name': 'MEDIA_UCRANIA_CONFIRMADOS'},
                {'y':  media_oman_c, 'type': 'bar', 'name': 'MEDIA_OMAN_CONFIRMADOS'},
                {'y':  media_libya_c, 'type': 'bar', 'name': 'MEDIA_LIBIA_CONFIRMADOS'},
                
                {'y':  media_ukraine_m, 'type': 'bar', 'name': 'MEDIA_UCRANIA_MUERTES'},
                {'y':  media_oman_m, 'type': 'bar', 'name': 'MEDIA_OMAN_MUERTES'},
                {'y':  media_libya_m, 'type': 'bar', 'name': 'MEDIA_LIBIA_MUERTES'},
            ],
            'layout': {
                'title': 'Comparativo estadístico (Ucrania, Oman y Libia)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
#**************************************** PIE DE PÁGINA *******************************************
    dcc.Markdown(children="""
    ## Elaboración propia con datos de COVID 19 API https://covid19api.com/ 
    """, style={
        'color': colors['texto'],
        "font-size": 10
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)