def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio=int("150")
    descuento=float("23.5")

    precio_con_descuento=precio-descuento
    cantidad=int(input("cantidad: "))

    total=precio_con_descuento*cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")
