from tkinter import *
from tkinter.messagebox import showinfo
import tkintermapview

from data.database import SqliteClient



def mostrar_senderos(database, map_widget):
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
   
    coordinates=database.getAll()
    sendero_1=[]
    
    for coordinate in coordinates:
        lat=coordinate[1]
        long=coordinate[2]
        print(lat,long)
        sendero_1.append((lat,long))
    path_sendero_1 = map_widget.set_path(sendero_1)
def mostrar_todos_los_marcadores(database, map_widget):
        # Set position with marker
    # 4. Establece la ubicación del marcador
    #marker_1 = map_widget.set_address("colosseo, rome, italy", marker=True)
    coordinates=database.getAll()
    for coordinate in coordinates:
        print(coordinate)
        lat=coordinate[1]
        long=coordinate[2]
        adr = tkintermapview.convert_coordinates_to_address(lat, long)
        marker = map_widget.set_marker(lat,long, text=adr.city)
    map_widget.set_zoom(12)
    #print(marker.position, marker.text) 
    #marker.set_text("Murcia") 
    # marker_1.delete()
def click_poligono(polygon):
    print(f"polygon clicked - text: {polygon.name}")
    showinfo("Polygon", f"has hecho click en el poligono: {polygon.name}")
def mostrar_poligono(map_widget):
    poligono_1 = map_widget.set_polygon([(38.1950,-1.4735), (38.1945,-1.4735),(38.0892,-1.0835), (37.9057,-1.2057), (37.9972,-1.6507)],
                                #fill_color=None,
                                outline_color="red",
                                border_width=1,
                                command=click_poligono,
                                name="poligono 1")
    print(f"polygon clicked - text: {poligono_1.name}")
def borrar_poligono(map_widget):
    map_widget.delete("poligono 1")
    

def add_marker_event(coords, map_widget, database):
    print("Marcador añadido. :", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="Nuevo marcador: "+str(coords))   
    database.insert(coords[0], coords[1])

def left_click_event(coordinates_tuple):
    #adr = tkintermapview.convert_coordinates_to_address(51.5122057, -0.0994014)
    adr = tkintermapview.convert_coordinates_to_address(coordinates_tuple[0], coordinates_tuple[1])
    print(adr.street, adr.housenumber, adr.postal, adr.city, adr.state, adr.country, adr.latlng)


def main():
    #la version 1 añade inserts
    database=SqliteClient(1)
    # create tkinter window
    root_tk = Tk()
    root_tk.geometry(f"{900}x{800}")
    root_tk.title("Senderos")


    my_label=LabelFrame(root_tk,text="Senderos")
    my_label.grid(row=0,column=0,columnspan=2,padx=10)

    #Botones
    buttom_mostrar_sendero=Button(root_tk,text="Mostrar sendero1",command=lambda:mostrar_senderos(database, map_widget))
    buttom_mostrar_sendero.grid(row=1,column=0,padx=10)
    #buttom_crear_sendero=Button(root_tk,text="Crear sendero")
    #buttom_crear_sendero.grid(row=2,column=0,padx=10)

    buttom_mostrar_poligono=Button(root_tk,text="Mostrar poligono 1",command=lambda:mostrar_poligono(map_widget))
    buttom_mostrar_poligono.grid(row=3,column=0,padx=10)
    #buttom_borrar_poligono=Button(root_tk,text="Borra poligono 1",command=lambda:borrar_poligono(map_widget))
    #buttom_borrar_poligono.grid(row=4,column=0,padx=10)
    

    # Crea el map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, corner_radius=0, width=800, height=600)
    map_widget.grid(row=1,column=1,columnspan=4, rowspan=3, padx=10, pady=10)
    map_widget.add_right_click_menu_command(label="Añade un marcador pichón", command=lambda coords:add_marker_event(coords,map_widget, database), pass_coords=True)
    map_widget.add_right_click_menu_command(label="Mostrar senderos", command=lambda:mostrar_senderos(database, map_widget), pass_coords=False)
    map_widget.add_left_click_map_command(left_click_event)
    
    textArea=Text(root_tk, bg='white', fg='black', bd=2, font=('Helvetica', 15, 'bold'), height=4)
    textArea.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

    
    # Establece la posición en coordenadas, ve a https://www.openstreetmap.org/  para obetenr las coordenadas en la barra de dirección
    latLong1=database.getById(2)
    map_widget.set_position(latLong1[1],latLong1[2])  # Murcia
    #mostramos todos los marcadores
    mostrar_todos_los_marcadores(database,map_widget)
    root_tk.mainloop()

if __name__ == "__main__":
    main()
    

