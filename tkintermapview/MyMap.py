from tkinter import *
import tkintermapview 
from tkintermapview import canvas_polygon
from tkinter.messagebox import showinfo
from data.CoordenatesModel import CoordenatesModel 
from data.RoutesModel import RoutesModel 
#https://pypi.org/project/geojson/
import geojson
#Lo utilizamos para ver si existe un archivp
import os
class MyMap:
    def __init__(self, root_tk:Tk,  text_consulta:Text, text_resultados:Text, listBox:Listbox):
        self.root_tk = root_tk
        self.text_consulta = text_consulta
        self.text_resultados = text_resultados
        self.listBox = listBox
        self.map_widget = tkintermapview.TkinterMapView(root_tk, corner_radius=0, width=800, height=600)
        #self.map_widget.grid(row=1,column=1,columnspan=4, rowspan=3, padx=10, pady=10)
        self.map_widget.pack(side=LEFT)
        self.map_widget.add_right_click_menu_command(label="Añade un marcador", command=lambda coords:self.add_marker_event(coords), pass_coords=True)
        self.map_widget.add_right_click_menu_command(label="Añadir coordenada al sendero activo", command=lambda coords:self.add_coordenada_sendero_activo(coords), pass_coords=True)
        self.map_widget.add_right_click_menu_command(label="Mostrar poligono de esta región", command=lambda:self.mostrar_poligono_del_lugar_actual(), pass_coords=False)
        self.map_widget.add_right_click_menu_command(label="Borrar poligono de esta región", command=lambda:self.borrar_poligono(), pass_coords=False)
        self.map_widget.add_left_click_map_command(self.left_click_event)
        self.map_widget.set_zoom(10)
        self.cambiar_server(0)

        self.coordenatesModel=CoordenatesModel(1)
        self.routesModel=RoutesModel(1)

        self.poligonos=[]
        self.paths=[]
        self.sendero_activo=None
    
    def cambiar_server(self, number_server):
        if (number_server == 0): self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")  # OpenStreetMap (default)
        elif (number_server == 1):self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
        elif (number_server == 2):self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
        elif (number_server == 3):self.map_widget.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")  # painting style
        elif (number_server == 4):self.map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")  # black and white
        elif (number_server == 5):self.map_widget.set_tile_server("https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png")  # detailed hiking
        elif (number_server == 6):self.map_widget.set_tile_server("https://tiles.wmflabs.org/osm-no-labels/{z}/{x}/{y}.png")  # no labels
        elif (number_server == 7):self.map_widget.set_tile_server("https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg")  # swisstopo map




        
    def centrar_por_nombre(self, address):
        # Establecer la posición de la dirección
        marker = self.map_widget.set_address(address)
        print("marker",marker)
        if not marker:
            position= self.coordenatesModel.getById(2)
            print("position",position)
            self.map_widget.set_position(position[1], position[2], zoom=16)




    ###############################################
    # Senderos
    ###############################################
    def crear_sendero(self, textBox:Text):
        """
        Obtiene el nombre del sendero del textbos y 
        crea un sendero en la base de datos y  el listbox
        """
        nombre_sendero=textBox.get("1.0", "end-1c")
        if(len(nombre_sendero)==0):
            showinfo("Error", "El nombre del sendero está vacío")
        else:
            self.routesModel.insert(nombre_sendero)
            self.listBox.select_clear(0,END)
            self.listBox.insert(END, nombre_sendero)
            self.listBox.selection_set(END)
            showinfo("Mensaje", "Nuevo sendero creado")
            
    def borrar_sendero(self):
        currentSelection=self.listBox.curselection()
        if(currentSelection.__len__()!=0):
            item=self.listBox.get(currentSelection)
            print("El item recibido es: ",item[0],", name: ",item[1])
            #Borramos todas sus paths del mapa
            for path in self.paths:  
                path.delete()
            #path_1.remove_position(position)
            #borramos todas sus coordenadas
            self.coordenatesModel.deleteByRouteId(item[0])
            #Lo borramos de la tabla routes
            self.routesModel.delete(item[0])
            #Lo borramos de la lista

            self.listBox.delete(currentSelection)

            showinfo("Mensaje", "Sendero borrado")
        else:
            showinfo("Error", "Please select a sendero")
    def get_senderos(self):
        senderos=self.routesModel.getAll()
        return senderos

    def mostrar_senderos(self):
        # Create path from position list
        # 7. Crea un camino desde una lista de posiciones
        #map_widget.set_path([(38.068,-1.496), (38.069,-1.495)])
        """
        # set a path
        path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])

        # methods
        path_1.set_position_list(new_position_list)
        path_1.add_position(position)
        path_1.remove_position(position)
        path_1.delete()

        """
        currentSelection=self.listBox.curselection()
        #if(currentSelection.__len__()==0):
        #    showinfo("Error", "Please select an route")
        #else:
        if(currentSelection.__len__()!=0):
            item=self.listBox.get(currentSelection)
            print("El item recibido es: ",item)
            
            sendero=self.routesModel.getByName(item)
            if(sendero==None):
                print("No existen coordenadas que tengan el sendero ",item)
            else:
                print("El sendero es: ",sendero)
                sendero_id=sendero[0]
                coordinates=self.coordenatesModel.getByIdRoute(sendero_id)
                print("Las coordenadas son: ",coordinates)
                sendero_activo_lat_long=[]
                for coordinate in coordinates:
                    lat=coordinate[1]
                    long=coordinate[2]
                    #print(lat,long)
                    sendero_activo_lat_long.append((lat,long))
                self.sendero_activo=self.map_widget.set_path(sendero_activo_lat_long)
                self.paths.append(self.sendero_activo)
                

    def add_coordenada_sendero_activo(self, coords):
        currentSelection=self.listBox.curselection()
        if(currentSelection.__len__()!=0):
            item=self.listBox.get(currentSelection)
            print("El item recibido es: ",item)
            route=self.routesModel.getByName(item)
            self.coordenatesModel.insert(coords[0], coords[1], route[0])
            #showinfo("Mensaje", f"Coordenada {coords} anadida a la ruta activa: {item[1]}")
            self.mostrar_senderos()
        else:
            showinfo("Error", "Please select a route")


    def get_sendero_activo(self):
        return self.sendero_activo
    ###############################################
    # Fin de senderos
    ###############################################       



    ###############################################
    # Marcadores
    ###############################################
    def mostrar_todos_los_marcadores(self):
            # Set position with marker
        # 4. Establece la ubicación del marcador
        #marker_1 = map_widget.set_address("colosseo, rome, italy", marker=True)
        coordinates=self.coordenatesModel.getAll()
        for coordinate in coordinates:
            print(coordinate)
            lat=coordinate[1]
            long=coordinate[2]
            adr = tkintermapview.convert_coordinates_to_address(lat, long)
            marker = self.map_widget.set_marker(lat,long, text=adr.city)
        self.map_widget.set_zoom(12)
        #print(marker.position, marker.text) 
        #marker.set_text("Murcia") 
        # marker_1.delete()






    ###############################################
    # Poligonos
    ###############################################

    def click_poligono(self,polygon):
        print(f"polygon clicked - text: {polygon.name}")
        showinfo("Polygon", f"has hecho click en el poligono: {polygon.name}")


    def mostrar_poligono_del_lugar_actual(self):
        coordinates_tuple = self.map_widget.get_position()
        adr = tkintermapview.convert_coordinates_to_address(coordinates_tuple[0], coordinates_tuple[1])
        city=adr.city
        if not city:
            print("No existen poligonos")
            showinfo("Error", f"No existe el poligono  {city}, se muestra el de Murcia")
            self.mostrar_poligono("murcia")
            return
        else:
            self.mostrar_poligono(city.lower())

    #threading.Thread(target=cargar_poligono_murcia, daemon=True, args=(map_widget,text_consulta,text_resultados)).start()
    def mostrar_poligono(self, *args):
        name=args[0]
        file="assets/"+name+".geojson"
        if not os.path.isfile(file):
            print(f"El archivo {file} con las coordenadas mo existe.")
            showinfo("Polygon", f"El archivo {file} con las coordenadas mo existe.")
        else:
            coordenates=[]
            self.map_widget.set_zoom(8)
            f=open(file, encoding="utf8")
            gj = geojson.load(f)
            features = gj['features'][0]
            list_coordinates = features['geometry']['coordinates']
            cantidad=len(list_coordinates[0][0])
            self.text_consulta.delete(1.0, END)
            self.text_consulta.insert(END, f"Procesando: poligono Murcia, tamaño: {str(cantidad)}")
            for number,coord in enumerate(list_coordinates[0][0]):
                lat=float(coord[1])
                long=float(coord[0])
                coordenates.append((lat,long))
            poligono=self.map_widget.set_polygon(coordenates, outline_color="red",border_width=10, command=self.click_poligono, name=name)
            self.poligonos.append(poligono)
    def borrar_poligono(self):
        #Obtenemos el nombre de ese lugar
        coordinates_tuple = self.map_widget.get_position()
        adr = tkintermapview.convert_coordinates_to_address(coordinates_tuple[0], coordinates_tuple[1])
        city=adr.city
        encontrado=False

        if self.poligonos.__len__()==0:
            print("No existen poligonos")
            showinfo("Error", "No existen poligonos")
            return
        else:
            if not city:
                print(f"No se obtuve el nombre del poligono {city}")
                city="murcia"
            #comprobamos si exsite el poligono
            for poligono in self.poligonos:
                if(poligono.name==city):
                    poligono.delete()
                    encontrado=True
            if not encontrado:
                print(f"El poligono {city} no existe")
                showinfo("Error", f"El poligono {city} no existe")
        
    # Create position markers
    # 6. Crea marcadores
    """
    También puedes establecer un marcador de posición sin enfocar el widget en él. 
    Puede pasar un argumento de texto a la función y recuperar el objeto marcador, 
    para poder almacenar el marcador y modificarlo o eliminarlo más tarde.
    Un marcador también se puede personalizar pasando los siguientes argumentos a .set_marker(), .set_address() o .set_position()
        text, font, icon, icon_anchor, image (PhotoImage), image_zoom_visibility, marker_color_circle, marker_color_outside, text_color
    """
    def add_marker_event(self,coords):
        print("Marcador añadido. :", coords)
        new_marker = self.map_widget.set_marker(coords[0], coords[1], text=str(coords))   

        self.coordenatesModel.insert(coords[0], coords[1])

    def left_click_event(self,coordinates_tuple):
        #adr = tkintermapview.convert_coordinates_to_address(51.5122057, -0.0994014)
        adr = tkintermapview.convert_coordinates_to_address(coordinates_tuple[0], coordinates_tuple[1])
        print(adr.street, adr.housenumber, adr.postal, adr.city, adr.state, adr.country, adr.latlng)



