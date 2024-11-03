from tkinter import *
from MyMap import MyMap









def main():    
    # create tkinter window
    root_tk = Tk()
    width=1000
    height=800
    color_verde_claro="#ccfad5"
    color_azul_claro="#b9b0fa"
    color_rosa_claro="#fab0f6"
    color_gris_claro="#c3c3c3"
    color_boton_bg="#ffffff"
    color_fondo="lightblue"
    #color_boton_fg="#158aff"
    color_boton_fg="#000000"
    root_tk.geometry(f"{width}x{height}")
    root_tk.title("Senderos")
    #root_tk.resizable(0,0)
    root_tk.iconbitmap("assets/icon.ico")
    root_tk.configure(bg="lightblue")

    head_frame=Frame(root_tk)
    #ancho, alto, background, borde
    head_frame.configure(width=width, height=40, bg=color_fondo, bd=5)
    head_frame.pack()
    #head_frame.propagate(False)
    my_label=Label(head_frame,text="Senderos", font=('Helvetica', 15, 'bold'))
    my_label.place(x=width/2,y=2)


    options_frame=Frame(root_tk, bg=color_fondo, width=200, height=height-40)
    options_frame.pack(side=LEFT)
    #options_frame.propagate(False)

    Button(options_frame,text="Centrar",pady=5, bd=2, bg=color_boton_bg,command=lambda:myMap.centrar_por_nombre("Murcia")).pack()

    Label(options_frame, text="Senderos",pady=5).pack()
    listBox_senderos=Listbox(options_frame, width=20, height=10)
    listBox_senderos.bind('<<ListboxSelect>>', lambda e: myMap.mostrar_senderos())
    listBox_senderos.select_set(1)
    listBox_senderos.pack()
    text_nuevo_sendero=Text(options_frame, pady=5, bg='white', fg='black', bd=2, height=1, width=20)
    text_nuevo_sendero.pack()
    button_crear_sendero=Button(options_frame,text="Crear nuevo sendero",pady=5, bd=2, bg=color_boton_bg,command=lambda:myMap.crear_sendero(text_nuevo_sendero))
    button_crear_sendero.pack()
    button_borrar_sendero_activo=Button(options_frame,text="borrar_sendero_activo",pady=5, bd=2, bg=color_boton_bg,command=lambda:myMap.borrar_sendero())
    button_borrar_sendero_activo.pack()
    


    main_frame=Frame(root_tk, width=width, height=height-200, padx=50, bg=color_fondo)
    main_frame.pack()

    foot_frame=Frame(root_tk, width=width, height=100, bg=color_fondo)
    foot_frame.pack()
    #foot_frame.propagate(False)
    text_consulta=Text(foot_frame, bg='white', fg='black', bd=2, font=('Helvetica', 9, 'bold'), height=1)
    text_consulta.place(x=0,y=10)
    text_resultados=Text(foot_frame, bg='white', fg='black', bd=2, font=('Helvetica', 9, 'bold'), height=4)
    text_resultados.place(x=0,y=50)
  

    #Mapa
    myMap=MyMap(main_frame, text_consulta, text_resultados, listBox_senderos)
    myMap.centrar_por_nombre("Murcia")
    senderos=myMap.get_senderos()
    for sendero in senderos:
        listBox_senderos.insert(END, sendero[1])

    
    root_tk.mainloop()


if __name__ == "__main__":
    main()
    

