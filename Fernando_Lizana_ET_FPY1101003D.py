def validar_codigo(codigo, juegos, inventario):
    cod_clean = codigo.strip().upper()
    if not cod_clean or cod_clean in juegos or cod_clean in inventario:
        return False
    return True

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_plataforma(plataforma):
    return bool(plataforma.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_clasificacion(clasificacion):
    return clasificacion.strip() in ['E', 'T', 'M']

def validar_multiplayer(multi):
    return multi.strip().lower() in ['s', 'n']

def validar_editor(editor):
    return bool(editor.strip())

def validar_precio(precio_str):
    try:
        val = int(precio_str)
        return val > 0
    except ValueError:
        return False

def validar_stock(stock_str):
    try:
        val = int(stock_str)
        return val >= 0
    except ValueError:
        return False

def leer_opcion():
    try:
        return int(input("Ingrese opción: "))
    except ValueError:
        return -1

def stock_plataforma(plataforma, juegos, inventario):
    plat_target = plataforma.strip().lower()
    total_stock = 0
    for codigo, datos_juego in juegos.items():
        if datos_juego[1].lower() == plat_target:
            if codigo in inventario:
                total_stock += inventario[codigo][1]
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    if p_min < 0 or p_max < 0 or p_min > p_max:
        print("No hay juegos en ese rango de precios.")
        return
    encontrados = []
    for codigo, datos_inv in inventario.items():
        precio, stock = datos_inv[0], datos_inv[1]
        if p_min <= precio <= p_max and stock > 0:
            if codigo in juegos:
                titulo = juegos[codigo][0]
                encontrados.append((titulo, f"{titulo}--{codigo}"))
    if not encontrados:
        print("No hay juegos en ese rango de precios.")
    else:
        encontrados.sort(key=lambda x: x[0])
        lista_resultados = [item[1] for item in encontrados]
        print(f"Los juegos encontrados son: {lista_resultados}")

def buscar_codigo(codigo, inventario):
    return codigo.strip().upper() in inventario

def actualizar_precio(codigo, nuevo_precio, inventario):
    cod_upper = codigo.strip().upper()
    if buscar_codigo(cod_upper, inventario):
        inventario[cod_upper][0] = nuevo_precio
        return True
    return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    cod_upper = codigo.strip().upper()
    if cod_upper in juegos or cod_upper in inventario:
        return False
    juegos[cod_upper] = [
        titulo.strip(),
        plataforma.strip(),
        genero.strip(),
        clasificacion.strip(),
        multiplayer,
        editor.strip()
    ]
    inventario[cod_upper] = [precio, stock]
    return True

def eliminar_juego(codigo, juegos, inventario):
    cod_upper = codigo.strip().upper()
    if buscar_codigo(cod_upper, inventario):
        if cod_upper in juegos:
            del juegos[cod_upper]
        if cod_upper in inventario:
            del inventario[cod_upper]
        return True
    return False

def main():
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
    }
   
    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2]
    }
   
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")
       
        opcion = leer_opcion()
       
        if opcion < 1 or opcion > 6:
            print("Debe seleccionar una opción válida")
            continue
           
        if opcion == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat, juegos, inventario)
           
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min, p_max, juegos, inventario)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
                   
        elif opcion == 3:
            while True:
                cod = input("Ingrese código del juego: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("El precio debe ser un número entero mayor a cero.")
                    else:
                        if actualizar_precio(cod, nuevo_precio, inventario):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                except ValueError:
                    print("Debe ingresar un valor entero válido.")
                   
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    break
                   
        elif opcion == 4:
            cod = input("Ingrese código del juego: ")
            tit = input("Ingrese título: ")
            plat = input("Ingrese plataforma: ")
            gen = input("Ingrese género: ")
            clasif = input("Ingrese clasificación: ")
            multi_str = input("¿Es multiplayer? (s/n): ")
            edit = input("Ingrese editor: ")
            prec_str = input("Ingrese precio: ")
            stk_str = input("Ingrese stock: ")
           
            if not validar_codigo(cod, juegos, inventario):
                print("El código no debe estar vacío ni existir previamente.")
            elif not validar_titulo(tit):
                print("El título no debe estar vacío.")
            elif not validar_plataforma(plat):
                print("La plataforma no debe estar vacía.")
            elif not validar_genero(gen):
                print("El género no debe estar vacío.")
            elif not validar_clasificacion(clasif):
                print("La clasificación debe ser exactamente 'E', 'T' o 'M'.")
            elif not validar_multiplayer(multi_str):
                print("La opción multiplayer debe ser 's' o 'n'.")
            elif not validar_editor(edit):
                print("El editor no debe estar vacío.")
            elif not validar_precio(prec_str):
                print("El precio debe ser un número entero mayor que cero.")
            elif not validar_stock(stk_str):
                print("El stock debe ser un número entero mayor o igual a cero.")
            else:
                multi_bool = (multi_str.strip().lower() == 's')
                precio_val = int(prec_str)
                stock_val = int(stk_str)
               
                if agregar_juego(cod, tit, plat, gen, clasif, multi_bool, edit, precio_val, stock_val, juegos, inventario):
                    print("Juego agregado")
                else:
                    print("El código ya existe")
                   
        elif opcion == 5:
            cod = input("Ingrese código del juego: ")
            if eliminar_juego(cod, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
               
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()