    # set current widget position and zoom
    # 2. Establece la posición en coordenadas, ve a https://www.openstreetmap.org/  para obetenr las coordenadas en la barra de dirección
    #Obtengo la 1 coordenada guardada en la base de datos
    latLong1=database.getById(2)
    map_widget.set_position(latLong1[1],latLong1[2])  # Murcia

    # set current widget position by address
    # 3. Establecer la posición de la dirección
    #map_widget.set_address("Murcia")


    # Set position and zoom to fit bounding box
    # 5. Establece la ubicación y el zoom para crear un cuadrado
    #map_widget.set_fit_bbox([(38.068,-1.496), (38.069,-1.495)])


    # Create position markers
    # 6. Crea marcadores
    """
    También puedes establecer un marcador de posición sin enfocar el widget en él. 
    Puede pasar un argumento de texto a la función y recuperar el objeto marcador, 
    para poder almacenar el marcador y modificarlo o eliminarlo más tarde.
    Un marcador también se puede personalizar pasando los siguientes argumentos a .set_marker(), .set_address() o .set_position()
        text, font, icon, icon_anchor, image (PhotoImage), image_zoom_visibility, marker_color_circle, marker_color_outside, text_color
    """


    # Create polygon from position list
    # 8. Crea un polígono desde una lista de posiciones
    #map_widget.set_polygon([(38.068,-1.496), (38.069,-1.495)])
    """
    def polygon_click(polygon):
        print(f"polygon clicked - text: {polygon.name}")
        
    polygon_1 = map_widget.set_polygon([(46.0732306, 6.0095215),
                                        ...
                                        (46.3772542, 6.4160156)],
                                    # fill_color=None,
                                    # outline_color="red",
                                    # border_width=12,
                                    command=polygon_click,
                                    name="switzerland_polygon")
    """