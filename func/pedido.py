import json
from datetime import datetime
import tkinter

#Trae datos de materiales en json
#CHECAR
def cargar_materiales():
    try:
        with open('./jsons/materials.json', 'r') as file:
            materiales = json.load(file)
        return materiales
    except FileNotFoundError:
        return []

#Carga la lista de maestros
def cargar_maestros():
    try:
        with open('./jsons/maestros.json', 'r') as file:
            maestros_data = json.load(file)
        return maestros_data
    except FileNotFoundError:
        return []
#Carga los pedididos
def cargar_pedidos():
    try:
        with open('./jsons/pedido.json', 'r') as file:
            pedidos_data = json.load(file)
            pedidos_validos = [pedido for pedido in pedidos_data if isinstance(pedido, dict)]
        return pedidos_validos
    except FileNotFoundError:
        return []
    
#Guarda los materiales en json
def guardar_materiales(materiales):
    with open('./jsons/materials.json', 'w') as file:
        json.dump(materiales, file, indent=4)
#Guarda los pedidos en json
def guardar_pedido(pedido):
    pedidos_data = cargar_pedidos()
    pedidos_data.append(pedido)
    with open('./jsons/pedido.json', 'w') as file:
        json.dump(pedidos_data, file, indent=4)

#asigna material a maestro
def asignar_material(materialID, maestroID, cantidad):
    materiales = cargar_materiales()
    maestros = cargar_maestros()
    if(cantidad<0):
        tkinter.messagebox.showerror('Error', 'Cantidad no valida')
        return
    print("Lista de materiales disponibles:")
    for material in materiales:
        print(f"ID: {material['id']}, Nombre: {material['nombre']}, Cantidad: {material['cant']}")

    print("\nLista de maestros disponibles:")
    for maestro in maestros:
        print(f"ID: {maestro['id']}, Nombre: {maestro['maestro']}, Ubicación: {maestro['ubicacion']}")

    material_encontrado = next((m for m in materiales if m['id'] == int(materialID)), None)
    maestro_encontrado = next((m for m in maestros if m['id'] == int(maestroID)), None)

    if material_encontrado is None or maestro_encontrado is None or cantidad is None:
        tkinter.messagebox.showerror('Error', 'Error al ingresar los datos')
        print("Error: ID de material o maestro no válido.")
        return

    #cantidad = int(input("Ingrese la cantidad a asignar: "))
    fecha_asignacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    material_encontrado['cant'] -= cantidad
    if material_encontrado['cant'] < 0:
        tkinter.messagebox.showerror('Error', 'La cantidad a asignar es mayor que la cantidad disponible.')
        print("Error: La cantidad a asignar es mayor que la cantidad disponible.")
        return

    guardar_materiales(materiales)

    pedidos_data = cargar_pedidos()
    nuevo_id_pedido = len(pedidos_data) + 1
    pedido = {
        "id_pedido": nuevo_id_pedido,
        "id_material": material_encontrado['id'],
        "id_maestro": maestro_encontrado['id'],
        "cantidad": cantidad,
        "fecha_asignacion": fecha_asignacion,
        "estatus": 1  # Nuevo pedido tiene estado activo
    }

    guardar_pedido(pedido)
    print("Material asignado correctamente.")
    tkinter.messagebox.showinfo('Exito', 'Material asignado correctamente.')
#Libera pedido
def liberar_pedido(id_pedido):

    pedidos_data = cargar_pedidos()

    for pedido in pedidos_data:
        if pedido['id_pedido'] == id_pedido:
            pedido['estatus'] = 0  # Cambiar el estado a "devuelto"
            materiales = cargar_materiales()
            material = next((m for m in materiales if m['id'] == pedido['id_material']), None)
            if material:
                material['cant'] += pedido['cantidad']
                #pedido['cantidad']=0
                guardar_materiales(materiales)
            with open('./jsons/pedido.json', 'w') as file:

                json.dump(pedidos_data, file, indent=4)
            tkinter.messagebox.showinfo('Exito', 'Pedido liberado y cantidad devuelta correctamente.')
            return True
    print("Pedido no encontrado.")

    return False

def liberar_pedido_maestro(id_maestro):
    pedidos_data = cargar_pedidos()
    for pedido in pedidos_data:
        if pedido['id_maestro'] == id_maestro:
            pedido['estatus'] = 0  # Cambiar el estado a "devuelto"
            materiales = cargar_materiales()
            material = next((m for m in materiales if m['id'] == pedido['id_material']), None)
            if material:
                material['cant'] += pedido['cantidad']
                guardar_materiales(materiales)
            with open('./jsons/pedido.json', 'w') as file:
                json.dump(pedidos_data, file, indent=4)
            tkinter.messagebox.showinfo('Exito', 'Pedido liberado y cantidad devuelta correctamente.')
            #return True
    #print("Pedido no encontrado.")

    #return False