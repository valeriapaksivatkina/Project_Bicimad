# Para ejecutar este codigo:
# python tuto_argparse.py -o A 

# o bien:
# python tuto_argparse.py --origin 



import argparse
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import folium
from folium import IFrame
import webbrowser


parser = argparse.ArgumentParser(description='BiciMad')


# definicion de argumentos
parser.add_argument('-o', '--origen', type=str, help='Origen de usuarios')
parser.add_argument('-d', '--destino', type=str, help='Destino de usuarios')


parser_args = parser.parse_args()

# variables que le paso por terminal, nombre viene del --nombre

origen = parser_args.origen
destino = parser_args.destino


df_final = pd.read_csv('/Users/paksivatkinavaleria/Desktop/ih_datamadpt0124_project_m1-main/notebooks/Bicimad_final.csv')


todos_nombres = df_final['origen_o_destino'].tolist()

# Usar process.extractOne para obtener la frase más similar al input
origen_similar, score = process.extractOne(origen, todos_nombres)

destino_similar, score = process.extractOne(destino, todos_nombres)

# establecer un umbral de similitud para considerar la coincidencia
umbral_similitud = 70  

origen_index = df_final[df_final['origen_o_destino'] == origen_similar].index # cual es el index de la fila donde esta el input de origen del usuario 
destino_index = df_final[df_final['origen_o_destino'] == destino_similar].index # cual es el index de la fila donde esta el input de destino del usuario 

# # filtra el dataframe para mostrar donde esta la estacion de Bicimad mas cercana al origen del usuario
if score >= umbral_similitud:
    if origen_index > 118: # porque despues de esa fila van los datos de las estaciones de Bicimad que pueden ser origen o destino, por eso solo demostramos una estacion de Bicimad mas cercana 
        direccion_estacion_bicimad = df_final[df_final['origen_o_destino'] == origen_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
        disponibilidad_bicicletas = df_final[df_final['origen_o_destino'] == origen_similar]['se_puede_alquilar_bici'].iloc[0]
        print("Ahora estás en {}. La estación de Bicimad más cercana está muy cerca de ti en la direccion {}. La estación tiene bicis disponibles para coger ahora - {}.".format(origen_similar, direccion_estacion_bicimad, disponibilidad_bicicletas))

    else:
        metros = df_final[df_final['origen_o_destino'] == origen_similar]['distancia_minima_a_estacion_de_Bicimad'].iloc[0]
        direccion_estacion_bicimad = df_final[df_final['origen_o_destino'] == origen_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
        disponibilidad_bicicletas = df_final[df_final['origen_o_destino'] == origen_similar]['se_puede_alquilar_bici'].iloc[0]
        segunda_estacion = df_final[df_final['origen_o_destino'] == origen_similar]['la_segunda_estacion_de_Bicimad_mas_cercana'].iloc[0]
        disponibilidad_bicicletas_2_estacion = df_final[df_final['origen_o_destino'] == origen_similar]['se_puede_alquilar_bici_2'].iloc[0]
        print("Ahora estás en {}. La estación de Bicimad más cercana está a {} metros de ti en la direccion {}. La estación tiene bicis disponibles para coger ahora - {}. La segunda estación de Bicimad más cercana está en {}. La estación tiene bicis disponibles para coger ahora - {}.".format(origen_similar, metros, direccion_estacion_bicimad, disponibilidad_bicicletas,segunda_estacion, disponibilidad_bicicletas_2_estacion))
        
else:
    print("No se encontró ningun origen similar.")


# filtra el dataframe para mostrar donde esta la estacion de Bicimad mas cercana al destino del usuario
if score >= umbral_similitud:
    if destino_index > 118: # despues de esa fila van los datos de las estaciones de Bicimad que pueden ser origen o destino, por eso solo demostramos una estacion de Bicimad mas cercana 
        direccion_estacion_bicimad_2 = df_final[df_final['origen_o_destino'] == destino_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
        sitios_libres = df_final[df_final['origen_o_destino'] == destino_similar]['se_puede_dejar_bici'].iloc[0]
        print("Tu destino es {}. La estación de Bicimad más cercana está muy cerca de allí en la direccion {}. La estación tiene sitio para anclar la bici - {}.".format(destino_similar, direccion_estacion_bicimad_2, sitios_libres))
    else:
        metros = df_final[df_final['origen_o_destino'] == destino_similar]['distancia_minima_a_estacion_de_Bicimad'].iloc[0]
        direccion_estacion_bicimad_2 = df_final[df_final['origen_o_destino'] == destino_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
        sitios_libres = df_final[df_final['origen_o_destino'] == destino_similar]['se_puede_dejar_bici'].iloc[0]
        segunda_estacion_2 = df_final[df_final['origen_o_destino'] == destino_similar]['la_segunda_estacion_de_Bicimad_mas_cercana'].iloc[0]
        sitios_libres_estacion_2 = df_final[df_final['origen_o_destino'] == destino_similar]['se_puede_dejar_bici_2'].iloc[0]
        print("Tu destino es {}. La estación de Bicimad más cercana está a {} metros en la direccion {}. La estación tiene sitio para anclar la bici - {}. La segunda estación de Bicimad más cercana de tu destino está en {}. La estación tiene sitio para anclar la bici - {}.".format(destino_similar, metros, direccion_estacion_bicimad_2, sitios_libres,segunda_estacion_2,sitios_libres_estacion_2))
else:
    print("No se encontró ningun destino similar.")   



### el codigo para coger las coordenadas de estaciones de Bicimad mas cercanas al origen/destino y construir una ruta en bici en GoogleMaps y abrirla en el navegador 
if origen_index > 118:
    coordenadas_origen = df_final[df_final['origen_o_destino'] == origen_similar][['latitude', 'longitude']].values[0]
else:
    direccion_estacion_bicimad = df_final[df_final['origen_o_destino'] == origen_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
    coordenadas_origen = df_final[df_final['direccion'] == direccion_estacion_bicimad][['latitude', 'longitude']].values[0]

if destino_index > 118:
    coordenadas_destino = df_final[df_final['origen_o_destino'] == destino_similar][['latitude', 'longitude']].values[0]
else:
    direccion_estacion_bicimad = df_final[df_final['origen_o_destino'] == destino_similar]['la_estacion_de_Bicimad_mas_cercana'].iloc[0]
    coordenadas_destino = df_final[df_final['direccion'] == direccion_estacion_bicimad][['latitude', 'longitude']].values[0]

# Construir la URL de la ruta en bicicleta en Google Maps
google_maps_link = f'https://www.google.com/maps/dir/?api=1&origin={coordenadas_origen[0]},{coordenadas_origen[1]}&destination={coordenadas_destino[0]},{coordenadas_destino[1]}&travelmode=bicycling'

# Abrir el enlace de la ruta en Google Maps en el navegador
webbrowser.open(google_maps_link)
