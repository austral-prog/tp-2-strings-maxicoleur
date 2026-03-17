def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto=float(input("Ingrese su gasto: "))
    dinero_recibido=float(input("Dinero recibido: "))



    vuelto=dinero_recibido- gasto

    parte_entera=int(vuelto)
    centavos=int(100*(vuelto-int(vuelto)))

    print("\nVuelto\n")

    print(f"Pesos: \n {parte_entera}")

    print(f"Centavos:\n {centavos}")
