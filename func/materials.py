import json
import tkinter

# Función para cargar los datos del archivo JSON
def cargar_datos():
    try:
        with open('./jsons/materials.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
    with open('./jsons/materials.json', 'w') as file:
        json.dump(data, file, indent=4)
        file.close()

# Función para agregar un nuevo material
def agregar_material(nombre, cantidad):
    if(cantidad<0):
        tkinter.messagebox.showerror('Error', 'Cantidad no valida')
        return
    data = cargar_datos()
    nuevo_material = {
        "id": len(data) + 1,
        "nombre": nombre,
        "cant": cantidad
    }
    data.append(nuevo_material)
    guardar_datos(data)
    tkinter.messagebox.showinfo('Exito', 'Material agregado correctamente.')

# Función para actualizar la cantidad de un material
def actualizar_cantidad(id_material, nueva_cantidad):
    if(nueva_cantidad<0):
        tkinter.messagebox.showerror('Error', 'Cantidad no valida')
        return
    data = cargar_datos()
    material_encontrado = False
    for material in data:
        if material['id'] == id_material:
            material_encontrado = True
            material['cant'] = nueva_cantidad
            guardar_datos(data)
            tkinter.messagebox.showinfo('Exito', 'Cantidad actualizada correctamente.')
            break
    if not material_encontrado:
        tkinter.messagebox.showerror('Error', 'ID de material no válido.')

# Función para eliminar un material
def eliminar_material():
    id_material = int(input("Ingrese el ID del material a eliminar: "))
    data = cargar_datos()
    material_encontrado = False
    for material in data:
        if material['id'] == id_material:
            material_encontrado = True
            data.remove(material)
            guardar_datos(data)
            print("Material eliminado correctamente.")
            break
    if not material_encontrado:
        print("Error: ID de material no válido.")
