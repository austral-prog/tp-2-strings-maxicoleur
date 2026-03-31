def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    name=input("Ingrese su nombre:")
    surname=input("Ingrese su apellido:")
    print(f"{name.lower()} {surname.lower()}")
    print(f"{name.title()} {surname.title()}")
    print(f"{name.upper()} {surname.upper()}")
    print("\t"+f"{name.lower()} {surname.lower()}")

