import flet as ft
import flet.map as map
import random

def main(page: ft.page):
    marker_layer_ref = ft.Ref[map.MarkerLayer]()
    page.title = "Senderos Murciadevs" 
    #Evento cuando se haga click
    def on_click(e: map.MapTapEvent, coordenates_text: ft.TextField):
        print(
            f"Name: {e.name} - coordinates: {e.coordinates} - Local: ({e.local_x}, {e.local_y}) - Global: ({e.global_x}, {e.global_y})"
        )
        coordenates_text.value = str(e.coordinates)
        page.update()

    coordenates_text = ft.TextField(label="Coordenadas")
    my_map = map.Map(
        expand=True,
        configuration=map.MapConfiguration(
            initial_center=map.MapLatitudeLongitude(40.028,-3.735),
            initial_zoom=7,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            on_init=lambda e: print(f"Initialized Map"),
            #Cuando se haga click
            on_tap=lambda e: on_click(e, coordenates_text),
        ),
        layers=[
            #Tilelayer:La capa principal del mapa, que muestra imágenes rasterizadas cuadradas en una cuadrícula continua.
            #https://flet.dev/docs/controls/maptilelayer
            map.TileLayer(
                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                on_image_error=lambda e: print("TileLayer Error"),
            ),
            #MarkerLayer:Una capa para mostrar marcadores.
            #https://flet.dev/docs/controls/mapmarkerlayer
            map.MarkerLayer(
                ref=marker_layer_ref,
                markers=[
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(39.049,-2.686),
                    ),
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(38.563,-2.197),
                    ),
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(38.565,-2.101),
                    ),
                ],
            ),
            #Una capa para mostrar PolygonMarkers.
            #https://flet.dev/docs/controls/mappolygonlayer
            map.PolygonLayer(
                polygons=[
                    map.PolygonMarker(
                        label="Fiesta de Murciadevs",
                        label_text_style=ft.TextStyle(
                            color=ft.colors.BLACK,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                        ),
                        color=ft.colors.with_opacity(0.3, ft.colors.BLUE),
                        coordinates=[
                            map.MapLatitudeLongitude(38.363,-6.163),
                            map.MapLatitudeLongitude(38.716,-4.499),
                            map.MapLatitudeLongitude(37.80,-5.652),
                            map.MapLatitudeLongitude(38.126,-6.438),
                            map.MapLatitudeLongitude(38.363,-6.163),
                        ],
                    ),
                ],
            ),
            #Una capa para mostrar PolylineMarkers.
            #https://flet.dev/docs/controls/mappolylinelayer
            
            map.PolylineLayer(
                polylines=[
                    map.PolylineMarker(
                        border_stroke_width=3,
                        border_color=ft.colors.RED,
                        gradient_colors=[ft.colors.BLACK, ft.colors.BLACK],
                        color=ft.colors.with_opacity(0.6, ft.colors.GREEN),
                        coordinates=[
                            map.MapLatitudeLongitude(38.363,-6.163),
                            map.MapLatitudeLongitude(38.716,-4.499),
                            map.MapLatitudeLongitude(37.80,-5.652),
                            map.MapLatitudeLongitude(38.126,-6.438),
                            map.MapLatitudeLongitude(38.363,-6.163),
                        ],
                    ),
                ],
            )
        ]
    )
    

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("Senderos Murciadevs", size=20, weight="bold"),
        ft.Row(
            [
                ft.Container(ft.TextButton("Crear sendero"),bgcolor=ft.colors.AMBER_100 ),
                ft.Container(ft.TextButton("Mostrar senderod"),bgcolor=ft.colors.AMBER_100 ),
                ft.Container(ft.TextButton("Crear marcador"),bgcolor=ft.colors.AMBER_100 ),
                ft.Container(ft.TextButton("Mostrar polígonos"),bgcolor=ft.colors.AMBER_100 ),

                
            ]
        ),
        coordenates_text,
        my_map,
    )

ft.app(main)