import customtkinter
import tkinter
import func.maestro
import func.materials
import func.pedido
global x 
x = -1
cadena = "Ingresa nombre material"
def checar(*argv):
    ban = True
    for arg in argv:
        if(arg == ""):
            ban = False
            break
    return ban

def entero(*argv):
    ban = True
    for arg in argv:
        try:
            arg = int(arg)
        except:
            tkinter.messagebox.showerror('Fallo', 'Ingresa un numero')
            return False
    return ban

def menu_inicial():

    label = customtkinter.CTkLabel(master=frame, text="Proyecto Final Python", font=("Times-New-Roman",30))
    label.pack(pady=12, padx=10)
    button = customtkinter.CTkButton(master=frame, text="Asignar materiales", command=asignar, font=("Times-New-Roman",20), width=200, height=40)
    button.pack(pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=frame, text="Liberar", command=liberar, font=("Times-New-Roman",20), width=200, height=40)
    button2.pack(pady=12, padx=10)
    button3 = customtkinter.CTkButton(master=frame, text="Mostrar pedidos", command=ini, font=("Times-New-Roman",20),width=200, height=40)
    button3.pack(pady=12, padx=10)
    button5 = customtkinter.CTkButton(master=frame, text="Maestros", command=menu_maestros, font=("Times-New-Roman",20),width=200, height=40)
    button5.pack(pady=12, padx=10)
    button6= customtkinter.CTkButton(master=frame, text="Materiales", command=menu_materiales, font=("Times-New-Roman",20),width=200, height=40)
    button6.pack(pady=12, padx=10)
    button4 = customtkinter.CTkButton(master=frame, text="Salir", command=salir, font=("Times-New-Roman",20),width=200, height=40)
    button4.pack(pady=12, padx=10)

def menu_materiales():
    limpiar()
    label = customtkinter.CTkLabel(master=frame, text="Menu Materiales", font=("Times-New-Roman",30))
    label.pack(pady=12, padx=10)
    button = customtkinter.CTkButton(master=frame, text="Agregar material", command=agregar_mat, font=("Times-New-Roman",20), width=200, height=40)
    button.pack(pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=frame, text="Mostrar material", command=in3, font=("Times-New-Roman",20), width=200, height=40)
    button2.pack(pady=12, padx=10)
    button3 = customtkinter.CTkButton(master=frame, text="Actualizar material", command=aux, font=("Times-New-Roman",20),width=200, height=40)
    button3.pack(pady=12, padx=10)
    button5 = customtkinter.CTkButton(master=frame, text="Salir", command=regresar, font=("Times-New-Roman",20),width=200, height=40)
    button5.pack(pady=12, padx=10)

def menu_maestros():
    limpiar()
    label = customtkinter.CTkLabel(master=frame, text="Menu maestros", font=("Times-New-Roman",30))
    label.pack(pady=12, padx=10)
    button = customtkinter.CTkButton(master=frame, text="Agregar Maestro", command=agregar_maestro, font=("Times-New-Roman",20), width=200, height=40)
    button.pack(pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=frame, text="Mostrar Maestro", command=in2, font=("Times-New-Roman",20), width=200, height=40)
    button2.pack(pady=12, padx=10)
    button3 = customtkinter.CTkButton(master=frame, text="Actualizar Maestro", command=actualizar_ma, font=("Times-New-Roman",20),width=200, height=40)
    button3.pack(pady=12, padx=10)
    button4 = customtkinter.CTkButton(master=frame, text="Eliminar Maestro", command=eliminar_ma, font=("Times-New-Roman",20),width=200, height=40)
    button4.pack(pady=12, padx=10)
    button5 = customtkinter.CTkButton(master=frame, text="Salir", command=regresar, font=("Times-New-Roman",20),width=200, height=40)
    button5.pack(pady=12, padx=10)

def liberar():
    limpiar()
    menu_inicial()
    label6 = customtkinter.CTkLabel(master=frame, text="Ingresar ID pedido", font=("Times-New-Roman",20))
    label6.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    boton = customtkinter.CTkButton(frame, text="Enviar", command=obtener_info1)
    boton.pack(pady=20)
    mostrar_pedidos()

def obtener_info1():
    x = entrada.get()
    if(checar(x)):
        if(entero(x)):
            x = int(x)
            print(x)
            ban = func.pedido.liberar_pedido(x)
            if(ban):
                    tkinter.messagebox.showinfo('Exito', 'Pedido liberador')
            else:
                    tkinter.messagebox.showerror('Fallo', 'Error al liberar')
    else:
        tkinter.messagebox.showerror('Error', 'Ingresa un ID')

def obtener_info2():
    x = entrada.get()
    x1 = entrada2.get()
    x2 = entrada3.get()
    if(checar(x,x1,x2)):
        if(entero(x,x1,x2)):
            x = int(x)
            x1 = int(x1)
            x2 = int(x2)
            func.pedido.asignar_material(x,x1,x2)
        else:
            tkinter.messagebox.showerror('Error', 'Ingresa todos los campos')


def obtener_info3():
    x = entrada.get()
    x1 = entrada2.get()
    if(checar(x,x1)):
        maestros_data = func.maestro.cargar_maestros()
        valor = 0
        if(maestros_data == []):
            valor = 0
        else:
            ultimo_diccionario = maestros_data[-1]
            valor = ultimo_diccionario.get('id')
        nuevo_maestro = {
            "id": valor + 1,
            "maestro": x,
            "ubicacion": x1
        }
        maestros_data.append(nuevo_maestro)
        func.maestro.guardar_maestros(maestros_data)
        tkinter.messagebox.showinfo('Exito', 'Maestro agregado correctamente.')
    else:
        tkinter.messagebox.showerror('Error', 'Ingresa todos los campos')

def obtener_info4():
    x = entrada.get()
    x1 = entrada2.get()
    x2 = entrada3.get()
    if(checar(x,x1,x2)):
        if(entero(x)):
            x = int(x)
            func.maestro.actualizar_maestro(x, x1, x2)
        else:
            tkinter.messagebox.showerror('Error', 'Ingresa todos los campos')

def obtener_info5():
    x = entrada.get()
    x1 = entrada2.get()
    if(checar(x,x1)):
        if(entero(x1)):
            x1 = int(x1)
            func.materials.agregar_material(x,x1)
        else:
            tkinter.messagebox.showerror('Error', 'Ingresa todos los campos')

def obtener_info6():
    x = entrada.get()
    x1 = entrada2.get()
    if(checar(x,x1)):
        if(entero(x,x1)):
            x = int(x)
            x1 = int(x1)
            func.materials.actualizar_cantidad(x,x1)
        else:
            tkinter.messagebox.showerror('Error', 'Ingresa todos los campos')

def obtener_info7():
    x = entrada.get()
    if(checar(x)):
        if(entero(x)):
            x = int(x)
            func.maestro.eliminar_maestro(x)
        else:
            tkinter.messagebox.showerror('Error', 'Ingresa ID correcto')

def actualizar_ma():
    limpiar()
    menu_maestros()
    label = customtkinter.CTkLabel(master=frame, text="Ingresar ID maestro", font=("Times-New-Roman",20))
    label.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    label2 = customtkinter.CTkLabel(master=frame, text="Ingresar nuevo nombre ", font=("Times-New-Roman",20))
    label2.pack(pady=12, padx=10)
    global entrada2
    entrada2 = customtkinter.CTkEntry(frame)
    entrada2.pack(pady=20)
    label3 = customtkinter.CTkLabel(master=frame, text="Ingresar nueva direccion", font=("Times-New-Roman",20))
    label3.pack(pady=12, padx=10)
    global entrada3
    entrada3 = customtkinter.CTkEntry(frame)
    entrada3.pack(pady=20)
    boton = customtkinter.CTkButton(frame, text="Actualizar informacion", command=obtener_info4)
    boton.pack(pady=20)

def aux():
    global cadena
    cadena = "Ingresa ID material"
    agregar_mat()


def agregar_mat():
    limpiar()
    menu_materiales()
    global cadena
    t = cadena
    label10 = customtkinter.CTkLabel(master=frame, text=t, font=("Times-New-Roman",20))
    label10.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    label12 = customtkinter.CTkLabel(master=frame, text="Ingresar la cantidad material ", font=("Times-New-Roman",20))
    label12.pack(pady=12, padx=10)
    global entrada2
    entrada2 = customtkinter.CTkEntry(frame)
    entrada2.pack(pady=20)
    if(cadena == "Ingresa nombre material"):
        boton = customtkinter.CTkButton(frame, text="Agregar material", command=obtener_info5)
        boton.pack(pady=20)
    else:
        cadena = "Ingresa nombre material"
        boton = customtkinter.CTkButton(frame, text="Actualizar material", command=obtener_info6)
        boton.pack(pady=20)


def asignar():
    limpiar()
    menu_inicial()
    label = customtkinter.CTkLabel(master=frame, text="Ingresar ID material", font=("Times-New-Roman",20))
    label.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    label2 = customtkinter.CTkLabel(master=frame, text="Ingresar ID maestro", font=("Times-New-Roman",20))
    label2.pack(pady=12, padx=10)
    global entrada2
    entrada2 = customtkinter.CTkEntry(frame)
    entrada2.pack(pady=20)
    label3 = customtkinter.CTkLabel(master=frame, text="Ingresar cantidad", font=("Times-New-Roman",20))
    label3.pack(pady=12, padx=10)
    global entrada3
    entrada3 = customtkinter.CTkEntry(frame)
    entrada3.pack(pady=20)
    boton = customtkinter.CTkButton(frame, text="Asignar", command=obtener_info2)
    boton.pack(pady=40)
    label4= customtkinter.CTkLabel(master=frame, text="MAESTROS", font=("Times-New-Roman",20))
    label4.pack(pady=12, padx=10)
    mostrar_maestros()
    label5= customtkinter.CTkLabel(master=frame, text="MATERIALES", font=("Times-New-Roman",20))
    label5.pack(pady=12, padx=10)
    mostrar_materiales()
    
    

def regresar():
    limpiar()
    menu_inicial()

def salir():
    root.destroy()

def limpiar():
    for widget in frame.winfo_children():
        widget.destroy()

def ini():
    limpiar()
    menu_inicial()
    mostrar_pedidos()

def in2():
    limpiar()
    menu_maestros()
    mostrar_maestros()

def in3():
    limpiar()
    menu_materiales()
    mostrar_materiales()

def mostrar_pedidos():
    pedidos_data = func.pedido.cargar_pedidos()
    if pedidos_data:
        for pedido in pedidos_data:
             if pedido.get('estatus', 1) != 0:
                label = customtkinter.CTkLabel(master=frame, text=(f"ID Pedido: {pedido['id_pedido']}\tID Material: {pedido['id_material']}\tCantidad Pedida: {pedido['cantidad']}\tID Maestro: {pedido['id_maestro']}\tFecha y Hora Asignación: {pedido['fecha_asignacion']}"))
                label.pack(pady=12, padx=10)
    else:
        tkinter.messagebox.showerror('Error', 'No hay pedidos en la lista')

def mostrar_maestros():
    maestros_data = func.maestro.cargar_maestros()
    if maestros_data:
        for maestro in maestros_data:
            label = customtkinter.CTkLabel(master=frame, text=(f"ID: {maestro['id']}\t Nombre: {maestro['maestro']}\t Ubicación: {maestro['ubicacion']}"))
            label.pack(pady=12, padx=10)
            
    else:
        tkinter.messagebox.showerror('Error', 'No hay maestros en la lista')


def mostrar_materiales():
    data = func.materials.cargar_datos()
    if data:
        print("Lista de materiales:")
        for material in data:
            label = customtkinter.CTkLabel(master=frame, text=(f"ID: {material['id']}\t Nombre: {material['nombre']}\t Cantidad: {material['cant']}"))
            label.pack(pady=12, padx=10)
    else:
        tkinter.messagebox.showerror('Error', 'No hay materiales en la lista')

def agregar_maestro():
    limpiar()
    menu_maestros()
    label = customtkinter.CTkLabel(master=frame, text="Ingresar el nombre del maestro", font=("Times-New-Roman",20))
    label.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    label2 = customtkinter.CTkLabel(master=frame, text="Ingresar la ubicacion del maestro", font=("Times-New-Roman",20))
    label2.pack(pady=12, padx=10)
    global entrada2
    entrada2 = customtkinter.CTkEntry(frame)
    entrada2.pack(pady=20)
    boton = customtkinter.CTkButton(frame, text="Agregar maestro", command=obtener_info3)
    boton.pack(pady=20)

def eliminar_ma():
    limpiar()
    menu_maestros()
    label = customtkinter.CTkLabel(master=frame, text="Ingresar ID maestro", font=("Times-New-Roman",20))
    label.pack(pady=12, padx=10)
    global entrada
    entrada = customtkinter.CTkEntry(frame)
    entrada.pack(pady=20)
    boton = customtkinter.CTkButton(frame, text="Eliminar", command=obtener_info7)
    boton.pack(pady=20)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
root.title("Proyecto final LP")
frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entrada = customtkinter.CTkEntry(frame)
menu_inicial()