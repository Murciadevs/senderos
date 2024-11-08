# ¿ Que es senderos ?

Programa para practicar y ayudar a Pablo a hacer su programa de senderos, al mismo tiempo crear polígonos para Carlos.

Está dividido en dos partes:

1. TkinterMapView: Utilizando python con el widget de tkintermapview
2. Flet: Utilizando la librería flet que permite crear aplicaciones web, ios y android utilziando python pero con componentes prediseñados.
3. Android: utilizando kotlin

# ¿Como obtener los límites de las regiones para hacer polígonos?

<a href="docs/obtener-limites.md">Pincha aquí</a>

# tkintermapview

Para trabajar con mapas desde python podemos utiliazr las librerías

-tkintermapview: https://github.com/TomSchimansky/TkinterMapView

-folium: https://stackoverflow.com/questions/60836108/how-to-add-unique-popups-to-each-geojson-polygon-in-folium-using-python



Aunque puedes configurar el servidor en tkintermapview, este se conecta al servidor openstreetmap: https://www.openstreetmap.org/#map=6/40.01/-2.49, https://es.wikipedia.org/wiki/OpenStreetMap

1. Crea u entorno virtual con "python -m venv venv"
2. Activa el entorno virtual con "source venv/bin/activate" en linux o "venv\Scripts\activate.bat" en windows
3. Selecciona el python interpreter en vscode
4. escribe en el terminal: pip install tkintermapview


 
 
<img src="docs/tkintermapview1.JPG" width="500">

# Flet

Flet es una herramienta para crear aplicaciones web, ios y android con componentes prediseñados: https://flet.dev

El componente mapa está aquí: https://flet.dev/docs/controls/map/

1. Instala flet con pip install flet
2. Ejecuta la aplicación situandote en la carpeta del proyecto  y escribe en el terminal "flet run"
3. Crea una aplicación android con flet, mira este artículo si tienes dudas: https://murciadevs.tipolisto.es/exportando-flet-a-android/


<img src="docs/flet1.JPG" width="500">
   
# Android

Abre la aplicación con android estudio y deja que se carguen las dependencias.