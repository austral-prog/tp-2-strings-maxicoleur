def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)


    nombre=input("Nombre Completo del alumno:")
    mail=input("Mail institucional del alumno:")
    nota_1=int(input("Nota 1: "))
    nota_2= int(input("Nota 2: "))
    nota_3= int(input("Nota 3: "))

    nombre_correcto=nombre.strip().lower()

    mail_correcto=mail.strip()

    espacios=int(nombre_correcto.find(" "))
    letra_apellido=espacios+1



    nombre_archivo=nombre_correcto.replace(" ","_")
    codigo_secreto=nombre_correcto[::-1]


    promedio=(nota_1 + nota_2 + nota_3)/3

    espacios_mail = int(mail_correcto.find("@"))
    arroba_posicion=espacios_mail+1

    print(f"""========================\n    FICHA DEL ALUMNO\n========================""")
    print(f"Nombre: {nombre_correcto.title()}")
    print(f"Email: {mail_correcto.lower()}")
    print(f"Caracteres en nombre: {len(nombre_correcto)}")
    print(f"Iniciales: {nombre_correcto[0].upper()}{nombre_correcto[letra_apellido].upper()}")
    print(f"Usuario:{nombre_correcto[espacios:].lower()}.{nombre_correcto[0:espacios].lower()}")
    print(f"Email valido: {'@'in mail_correcto}")
    print(f"Dominio: {mail_correcto[arroba_posicion:].lower()}")
    print(f"Nombre para archivo: {nombre_archivo.title()}")
    print(f"Cantidad de a: {nombre_correcto.count("a")}")
    print(f"Codigo secreto: {codigo_secreto.upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {nota_1+nota_2+nota_3}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {int(promedio)}")

    print("="*24)



