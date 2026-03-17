def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass

    base=int(input("Base: "))
    altura=int(input("Altura: "))

    area=int((base*altura)/2)
    perimetro=base*3

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
