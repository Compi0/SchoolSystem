import json
import tkinter
import func.pedido
    
# Función para imprimir mensajes con color
def imprimir_mensaje(mensaje):
  print(mensaje)

# Función para cargar los datos de maestros desde el archivo JSON
def cargar_maestros():
    try:
        with open('./jsons/maestros.json', 'r') as file:
            maestros_data = json.load(file)
        return maestros_data
    except FileNotFoundError:
        return []

# Función para guardar los datos de maestros en el archivo JSON
def guardar_maestros(maestros_data):
    with open('./jsons/maestros.json', 'w') as file:
        json.dump(maestros_data, file, indent=4)



# Función para actualizar la información de un maestro
def actualizar_maestro(id_maestro, nuevo_nombre,nueva_ubicacion):
    maestros_data = cargar_maestros()
    if maestros_data:
        #id_maestro = int(input("Ingrese el ID del maestro a actualizar: "))
        for maestro in maestros_data:
            if maestro['id'] == id_maestro:
                #nuevo_nombre = input("Ingrese el nuevo nombre del maestro: ")
                #nueva_ubicacion = input("Ingrese la nueva ubicación del maestro: ")
                maestro['maestro'] = nuevo_nombre
                maestro['ubicacion'] = nueva_ubicacion
                guardar_maestros(maestros_data)
                tkinter.messagebox.showinfo('Exito', 'Informacion actualizada correctamente')
                break
        else:
            tkinter.messagebox.showerror('Error', 'ID de maestro no encontrado.')
    else:
        tkinter.messagebox.showerror('Error', 'No hay maestros en la lista.')

# Función para eliminar un maestro
def eliminar_maestro(id_maestro):
    maestros_data = cargar_maestros()
    if maestros_data:
        for maestro in maestros_data:
            if maestro['id'] == id_maestro:
                func.pedido.liberar_pedido_maestro(id_maestro)
                maestros_data.remove(maestro)
                guardar_maestros(maestros_data)
                tkinter.messagebox.showinfo('Exito', 'Maestro eliminado correctamente.')


                break
        else:
            tkinter.messagebox.showerror('Error', 'ID de maestro no encontrado.')
    else:
        tkinter.messagebox.showerror('Error', 'No hay maestros en la lista.')