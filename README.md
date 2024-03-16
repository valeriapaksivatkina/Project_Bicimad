# Project_Bicimad (centros culturales)


**Utilidad de la App**
La aplicación permite al usuario introducir su ubicacion, a donde quire llegar y recibir las direcciones de las estaciones de Bicimad mas cercanas. Tambien la aplicacion verifica si se puede coger y anclar la bicicleta en esas estaciones. Ademas construye y abre la ruta para el usuario en GoogleMaps. Uniendo la estacion de Bicimad mas cercana al origen y la estacion mas cercana al destino del usuario

**Input de la App** 
El input del usuario puede ser de dos tipos: el sitio de interes (centros culturales de Madrid) tanto el origen como el destino; la estacion de Bicimad tanto el origen como el destino

***Output de la App***
Indica dónde se encuentra actualmente el usuario. A cuántos metros se encuentra la estación Bicimad más cercana y su dirección. Si actualmente es posible coger una bici en esta estación. Indica también dónde está la segunda estación Bicimad más cercana al usuario. Y si actualmente es posible coger una bicicleta en esta estación.

Indica hacia dónde se dirige el usuario. Dónde está la estación de Bicimad más cercana y a cuántos metros de su destino. Indica si hay plazas libres para anclar la bici en esa estación. También muestra dónde está la segunda estación más cercana a su destino y si hay sitio para anclar la bici allí. 

Abre un enlace en GoogleMaps con una ruta en bicicleta desde la estación de Bicimad más cercana a la ubicación del usuario hasta la estación más cercana a su destino

**Data:*** 
API de la empresa municipal de transporte de Madrid (EMT) donde estan los datos actuales de las estaciones de Bicimad, sus coordinadas y los datos de su accesibilidad

API de DatosAbiertos de Madrid - datos de los centros culturales de Madrid, sus direcciones y coordenadas

API de GoogleMaps (multiplataforma) para construir el enlace de la ruta para el usuario 

***Pasos del trabajo***
Obtener los datos de las APIs, estudiarlos y limpiarlos – un df con datos de las estaciones de Bicimad y un df con los datos de los centros culturales de Madrid
Separar los datos de coordinadas de las estaciones y de los centros culturales a dos columnas distintas (con lambda funciones)
Calcular para cada centro cultural 2 estaciones mas cercanas y a cuantas metros esta la primera. Crear columnas nuevas con esos datos en df de centros culturales
4) En el df de las estaciones crear nuevas columnas que contienen datos de la accesibilidad de bicis (si/no) y la posibilidad de aparcar bici (si/no)
  se puede alquilar bici: if activate == 1 and dock_bikes - reservations_count > 0
  se puede aparcar bici: if activate == 1 and free_bases > 0 

5)Para cada centro cultural (en df de centros culturales) buscar el valor apropriado en esas columnas y crear columnas nuevas 

6) Concatenar dos dataframes (de las estaciones de Bicimad y de los centros culturales). Para eso hacer la misma estructura  en cada dataframe 
  El df_final contiene columnas 
‘origen_o_destino’
‘direccion’, 
‘latitude’, 
‘longitude’, 
‘distancia_minima_a_la_estacion_de_Bicimad’, 
‘la_estacion_de_Bicimad_mas_cercana’, 
’se_puede_alquilar_bici’, 
‘se_puede_dejar_bici’, 
‘la_segunda_estacion_de_Bicimad_mas_cercana’, 
’se_puede_alquilar_bici_2’, 
‘se_puede_dejar_bici_2’

7)Escribir el bucle para que el usuario haga input y salga el ouput (datos filtrados del df)
En ese paso hemos usado la biblioteca de FuzzyWuzzy que permite introducir la palabra clave, no el nombre completo del origen y/o destino 

Tambien incluye la llamada a la API del GoogleMaps # Construir la URL de la ruta en bicicleta en Google Maps y abre el enlace de la ruta en Google Maps en el navegador
webbrowser.open(google_maps_link)

**Project Main Stack**
Requests
Pandas
Module geo_calculations.py
Argparse
