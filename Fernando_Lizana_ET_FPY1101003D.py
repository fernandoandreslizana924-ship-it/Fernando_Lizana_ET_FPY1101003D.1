juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    
}


inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],

}

def validar_titulos(Titulos):
    return bool (Titulos.strip)
def validar_plataforma(plataforma):
    return bool (plataforma)
def validar_genero(genero):
    return bool (genero.strip)
def validar_clasificacion(clasificacion):
    return bool (clasificacion.strip)

    print["e","t","m,"]


def validar_multiplayer(multi):
    return multi.strip().lower()["s","n"]

def validar_editor(editor):
    return bool (editor.strip)()
def validar_precio(precio_str):
    try:
        val=int(precio_str)
        return val<0
    except ValueError:
        return False
    
def validar_stock(stock_str):
    try:
        val=int(stock_str)
        return val<=0
    except ValueError:
        return False

def leer_opcion():
    try:
        return int(input("ingrese opcion:"))
    except ValueError:
        return-1

def stock_plataforma(plataforma,juegos,inventario):
    plat_target=plataforma.strip().lower()
    for juegos pass #falta algo aqui
    if datos_juegos[1].lower()==plat_target:
        if codigo in inventario:
            total_stock+=inventario[codigo][1]
    print("El total del stock disponible:{total_stock}")

def busqueda_precio(p_min,p_max,juegos,inventario):
    if p_min<0 or p_max <0 or p_min >p_max:
        print("no hay juegos en ese rango de precio.")
        return
    encontrados=[]
        precio,stock=datos_inv[0],datos_inv[1]





           

    












print("========== MENÚ PRINCIPAL ==========")
print("1. Stock por plataforma")
print("2. Búsqueda de juegos por rango de precio")
print("3. Actualizar precio de juego")
print("4. Agregar juego")
print("5. Eliminar juego")
print("6. Salir")
print("=====================================")