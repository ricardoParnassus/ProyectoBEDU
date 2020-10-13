import requests # Herramienta para obtener respuesta de  API
import datetime # Convertir formato fecha
import statistics # herramieta para obtener datos estadisticos 

#INDIA
#Se obtinen datos de la API
r = requests.get("https://api.covid19api.com/country/india")
# formato JSON 
datos_india= r.json()
# Se seleccionan los casos confirmados 
confirmados_india= [ dato["Confirmed"] for dato in datos_india]
# Se seleccionan los casos de muertes 
muertes_india= [ dato["Deaths"] for dato in datos_india]
# Se convierten el formato fecha 
fechas_india= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_india]
# se obtinen los totales de la lista de confirmados 
total_confirmados_india= [sum (dato["Confirmed"] for dato in datos_india)]
# Se obtienen los totales de la lista de muertes
total_muertes_india = [ sum (dato["Deaths"] for dato in datos_india)]
# Se obtienen la desviacion estandar de la lista de confirmados "La desviación estándar es la medida de dispersión más común, que indica qué tan dispersos están los datos con respecto a la media. Mientras mayor sea la desviación estándar, mayor será la dispersión de los datos."
desvest_india_c= [statistics.stdev(confirmados_india)]
#Se obtiene la desviacion estandar de los casos de muertes
desvest_india_m = [statistics.stdev(muertes_india)]
#Se obtiene la mediana de la lista de confirmados "La mediana de un conjunto de números es el número medio en el conjunto".
mediana_india_c = [statistics.median(confirmados_india)]
#Se obtiene la mediana de la lista de muertes
mediana_india_m = [statistics.median(muertes_india)]
#Se obtiene el promedio de la lista de casos confirmados "es la suma de los datos dividida entre el número total de datos"
media_india_c= [statistics.mean(confirmados_india)]
#Se obtiene el promedio de la lista de casos de muerte
media_india_m = [statistics.mean(muertes_india)]

#Se repite lo mismo con cada país

#ANDORRA
r = requests.get("https://api.covid19api.com/country/andorra")
datos_andorra= r.json() 
confirmados_andorra= [ dato["Confirmed"] for dato in datos_andorra]
muertes_andorra= [ dato["Deaths"] for dato in datos_andorra]
fechas_andorra= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_andorra]
total_confirmados_andorra= [sum (dato["Confirmed"] for dato in datos_andorra)]
total_muertes_andorra = [ sum (dato["Deaths"] for dato in datos_andorra)]

desvest_andorra_c= [statistics.stdev(confirmados_andorra)]
desvest_andorra_m = [statistics.stdev(muertes_andorra)]
mediana_andorra_c = [statistics.median(confirmados_andorra)]
mediana_andorra_m = [statistics.median(muertes_andorra)]
media_andorra_c= [statistics.mean(confirmados_andorra)]
media_andorra_m = [statistics.mean(muertes_andorra)]

#QATAR
r = requests.get("https://api.covid19api.com/country/qatar")
datos_qatar= r.json()
confirmados_qatar= [ dato["Confirmed"] for dato in datos_qatar]
muertes_qatar= [ dato["Deaths"] for dato in datos_qatar]
fechas_qatar= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_qatar]
total_confirmados_qatar= [sum (dato["Confirmed"] for dato in datos_qatar)]
total_muertes_qatar = [ sum (dato["Deaths"] for dato in datos_qatar)]

desvest_qatar_c= [statistics.stdev(confirmados_qatar)]
desvest_qatar_m = [statistics.stdev(muertes_qatar)]
mediana_qatar_c = [statistics.median(confirmados_qatar)]
mediana_qatar_m = [statistics.median(muertes_qatar)]
media_qatar_c= [statistics.mean(confirmados_qatar)]
media_qatar_m = [statistics.mean(muertes_qatar)]

#BURUNDI
r = requests.get("https://api.covid19api.com/country/burundi")
datos_burundi= r.json()
confirmados_burundi= [ dato["Confirmed"] for dato in datos_burundi]
muertes_burundi= [ dato["Deaths"] for dato in datos_burundi]
fechas_burundi= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_burundi]
total_confirmados_burundi= [sum (dato["Confirmed"] for dato in datos_burundi)]
total_muertes_burundi = [ sum (dato["Deaths"] for dato in datos_burundi)]

desvest_burundi_c= [statistics.stdev(confirmados_burundi)]
desvest_burundi_m = [statistics.stdev(muertes_burundi)]
mediana_burundi_c = [statistics.median(confirmados_burundi)]
mediana_burundi_m = [statistics.median(muertes_burundi)]
media_burundi_c= [statistics.mean(confirmados_burundi)]
media_burundi_m = [statistics.mean(muertes_burundi)]

#***************************************** SECCION II *********************************************************
#NIGERIA
r = requests.get("https://api.covid19api.com/country/nigeria")
datos_nigeria= r.json()
confirmados_nigeria= [ dato["Confirmed"] for dato in datos_nigeria]
muertes_nigeria= [ dato["Deaths"] for dato in datos_nigeria]
fechas_nigeria= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_nigeria]
total_confirmados_nigeria = [sum (dato["Confirmed"] for dato in datos_nigeria)]
total_muertes_nigeria = [ sum (dato["Deaths"] for dato in datos_nigeria)]

desvest_nigeria_c= [statistics.stdev(confirmados_nigeria)]
desvest_nigeria_m = [statistics.stdev(muertes_nigeria)]
mediana_nigeria_c = [statistics.median(confirmados_nigeria)]
mediana_nigeria_m = [statistics.median(muertes_nigeria)]
media_nigeria_c= [statistics.mean(confirmados_nigeria)]
media_nigeria_m = [statistics.mean(muertes_nigeria)]

#MONACO
r = requests.get("https://api.covid19api.com/country/monaco")
datos_monaco= r.json()
confirmados_monaco= [ dato["Confirmed"] for dato in datos_monaco]
muertes_monaco= [ dato["Deaths"] for dato in datos_monaco]
fechas_monaco= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_monaco]
total_confirmados_monaco = [sum (dato["Confirmed"] for dato in datos_monaco)]
total_muertes_monaco = [ sum (dato["Deaths"] for dato in datos_monaco)]

desvest_monaco_c= [statistics.stdev(confirmados_monaco)]
desvest_monaco_m = [statistics.stdev(muertes_monaco)]
mediana_monaco_c = [statistics.median(confirmados_monaco)]
mediana_monaco_m = [statistics.median(muertes_monaco)]
media_monaco_c= [statistics.mean(confirmados_monaco)]
media_monaco_m = [statistics.mean(muertes_monaco)]

#UCRANIA
r = requests.get("https://api.covid19api.com/country/ukraine")
datos_ukraine= r.json()
confirmados_ukraine= [ dato["Confirmed"] for dato in datos_ukraine]
muertes_ukraine= [ dato["Deaths"] for dato in datos_ukraine]
fechas_ukraine= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ukraine]
total_confirmados_ukraine = [sum (dato["Confirmed"] for dato in datos_ukraine)]
total_muertes_ukraine = [ sum (dato["Deaths"] for dato in datos_ukraine)]

desvest_ukraine_c= [statistics.stdev(confirmados_ukraine)]
desvest_ukraine_m = [statistics.stdev(muertes_ukraine)]
mediana_ukraine_c = [statistics.median(confirmados_ukraine)]
mediana_ukraine_m = [statistics.median(muertes_ukraine)]
media_ukraine_c= [statistics.mean(confirmados_ukraine)]
media_ukraine_m = [statistics.mean(muertes_ukraine)]

#OMAN
r = requests.get("https://api.covid19api.com/country/oman")
datos_oman= r.json()
confirmados_oman= [ dato["Confirmed"] for dato in datos_oman]
muertes_oman= [ dato["Deaths"] for dato in datos_oman]
fechas_oman= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_oman]
total_confirmados_oman = [sum (dato["Confirmed"] for dato in datos_oman)]
total_muertes_oman = [ sum (dato["Deaths"] for dato in datos_oman)]

desvest_oman_c= [statistics.stdev(confirmados_oman)]
desvest_oman_m = [statistics.stdev(muertes_oman)]
mediana_oman_c = [statistics.median(confirmados_oman)]
mediana_oman_m = [statistics.median(muertes_oman)]
media_oman_c= [statistics.mean(confirmados_oman)]
media_oman_m = [statistics.mean(muertes_oman)]

#LIBIA
r = requests.get("https://api.covid19api.com/country/libya")
datos_libya = r.json()
confirmados_libya = [ dato["Confirmed"] for dato in datos_libya]
muertes_libya = [ dato["Deaths"] for dato in datos_libya]
fechas_libya = [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_libya]
total_confirmados_libya = [sum (dato["Confirmed"] for dato in datos_libya)]
total_muertes_libya = [ sum (dato["Deaths"] for dato in datos_libya)]

desvest_libya_c = [statistics.stdev(confirmados_libya)]
desvest_libya_m = [statistics.stdev(muertes_libya)]
mediana_libya_c = [statistics.median(confirmados_libya)]
mediana_libya_m = [statistics.median(muertes_libya)]
media_libya_c = [statistics.mean(confirmados_libya)]
media_libya_m = [statistics.mean(muertes_libya)]
