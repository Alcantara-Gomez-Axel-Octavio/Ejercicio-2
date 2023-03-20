from tkinter import *
from tkinter import ttk
import tkinter as ttk



# Crear ventana principal
root = Tk()

# Crear frame principal
main_frame = ttk.Frame(root, width=200, height=200, bg="black")
main_frame.pack()

# Frame 1
frame1 = ttk.Frame(main_frame, width=693, height=100, bg="gray40", relief="raised")
frame1.pack()
frame1.grid(column=0, row=0)

etqTexto = ttk.Label(frame1)
etqTexto.grid()

imagen = PhotoImage(file= 'Carrito.png')

etqImagen = ttk.Label(frame1, bg="gray40")
etqImagen.grid(column=0, row=0,sticky=(E))
etqImagen["image"]  = imagen

ttk.Label(frame1, text="Product management", bg="gray40", font=("Arial", 36, "bold"), foreground="white").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(frame1, text="      ", bg="gray40", foreground="white").grid(column=2, row=0, padx=70, pady=10)

# Frame SeparadorSuperior
frameSeA = ttk.Frame(main_frame, width=300, height=10, bg="black")
frameSeA.grid(column=0, row=1)

# Frame 2 (Cafe)
frame2 = ttk.Frame(main_frame, width=690, height=510, bg="#482525")
frame2.grid(column=0, row=2)

    #Frame 3
frame3 = ttk.Frame(frame2, width=690, height=260, bg="#482525")
frame3.grid(column=0, row=0)

        #Frame 4
frame4 = ttk.Frame(frame3, width=690, height=260, bg="#482525")
frame4.grid(column=0, row=0,pady=20)
'''id_Product=0
Name=""
Descripcion=""
quantity=0
Price=0'''


ttk.Label(frame4, text="Id product:", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=0, row=0, padx=10, pady=10, sticky=(W))
ttk.Label(frame4, text="__________________", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=0, padx=10)
Id_Product = ttk.Entry(frame4, width=15, font=("Arial", 12, "bold"), bg="#482525", foreground="white", justify=CENTER )
Id_Product.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
Id_Product.grid(column=1, row=0, padx=10, sticky=(N))

ttk.Label(frame4, text="Name:", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=0, row=1, padx=10, pady=10, sticky=(W))
ttk.Label(frame4, text="__________________", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=1, padx=10)
NameE = ttk.Entry(frame4, width=15, font=("Arial", 12, "bold"), bg="#482525", foreground="white", justify=CENTER )
NameE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
NameE.grid(column=1, row=1, padx=10, sticky=(N))

ttk.Label(frame4, text="Descripcion:", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=0, row=2, padx=10, pady=10, sticky=(W))
ttk.Label(frame4, text="__________________", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=2, padx=10)
DescripcionE = ttk.Entry(frame4, width=15, font=("Arial", 12, "bold"), bg="#482525", foreground="white", justify=CENTER )
DescripcionE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
DescripcionE.grid(column=1, row=2, padx=10, sticky=(N))

ttk.Label(frame4, text="quantity:", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=0, row=3, padx=10, pady=10, sticky=(W))
ttk.Label(frame4, text="__________________", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=3, padx=10)
quantityE = ttk.Entry(frame4, width=15, font=("Arial", 12, "bold"), bg="#482525", foreground="white", justify=CENTER )
quantityE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
quantityE.grid(column=1, row=3, padx=10, sticky=(N))

ttk.Label(frame4, text="Price:", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=0, row=4, padx=10, pady=10, sticky=(W))
ttk.Label(frame4, text="__________________", bg="#482525", font=("Arial", 12, "bold"), foreground="white").grid(column=1, row=4, padx=10)
PriceE = ttk.Entry(frame4, width=15, font=("Arial", 12, "bold"), bg="#482525", foreground="white", justify=CENTER )
PriceE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
PriceE.grid(column=1, row=4, padx=10, sticky=(N))

        #Frame 5
frame5 = ttk.Frame(frame3, width=690, height=260, bg="#482525")
frame5.grid(column=1, row=0,sticky=(N),pady=5,padx=30)

            #Frame 6
frame6 = ttk.Frame(frame5, width=690, height=70, bg="#482525")
frame6.grid(column=0, row=0,sticky=(N))


imagen2 = PhotoImage(file= 'Lupa.png')
imagen2_reducida = imagen2.subsample(18, 18) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen2 = ttk.Button(frame6,bg="#482525",activebackground="#482525")
etqImagen2.grid(column=0, row=0,padx=10, sticky=(E))
etqImagen2['image']=imagen2_reducida
etqImagen2.config(borderwidth=0, highlightthickness=0)

imagen3 = PhotoImage(file= 'Brocha.png')
imagen3_reducida = imagen3.subsample(13, 13) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen3 = ttk.Button(frame6,bg="#482525",activebackground="#482525")
etqImagen3.grid(column=1, row=0,padx=5, sticky=(E))
etqImagen3['image']=imagen3_reducida
etqImagen3.config(borderwidth=0, highlightthickness=0)


BottonBack = ttk.Button(frame6,text="Back",  bg="#482525",activebackground="#482525", foreground="#7701da",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonBack.grid(column=2,row=0,pady=15)
BottonBack.config(borderwidth=0, highlightthickness=0)

ttk.Label(frame6, text="                     ", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=3, row=0)

#Frame 7

frame7 = ttk.Frame(frame5, width=690, height=70, bg="#482525")
frame7.grid(column=0, row=1)


BottonSave = ttk.Button(frame7,text="Save",  width=17, bg="green",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonSave.grid(column=0,row=0, pady=10,sticky=(W))
BottonSave.config(borderwidth=0, highlightthickness=0)
ttk.Label(frame7, text="                     ", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=0, padx=2)

BottonDelete = ttk.Button(frame7,text="Delete",  width=17, bg="Red",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonDelete.grid(column=0,row=1, pady=10, sticky=(W))
BottonDelete.config(borderwidth=0, highlightthickness=0)

BottonUpdate = ttk.Button(frame7,text="Update",  width=17, bg="Orange",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonUpdate.grid(column=0,row=2, pady=10, sticky=(W))
BottonUpdate.config(borderwidth=0, highlightthickness=0)

# Frame 8
frame8 = ttk.Frame(frame2, width=690, height=240, bg="#482525")
frame8.grid(column=0, row=3, pady=20)

# Crear encabezado de la tabla
ttk.Label(frame8, text="idproduit", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(frame8, text="namep", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(frame8, text="description", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(frame8, text="quantity", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(frame8, text="unite_price", width=10, bg="gray", fg="white").grid(row=0, column=4)

# Crear datos de la tabla
data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "hamound boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat", "80", "50.0"),
    ("5", "Aroma", "cafe", "60", "80.0"),
    ("6", "Facto", "Facto", "7000", "600.0"),
    ("", "", "", "", ""),
    ("", "", "", "", ""),
    ("", "", "", "", "")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(frame8, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))

# Frame SeparadorBase
frameSeB = ttk.Frame(main_frame, width=300, height=25, bg="black", relief="sunken")
frameSeB.grid(column=0, row=4)


root.mainloop()
