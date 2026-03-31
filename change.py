def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """


    print(("Ingresar gasto:"))
    gasto=float(input())
    print(gasto)
    print("Dinero recibido")
    dinero_recibido=int(input())
    print(dinero_recibido)



    vuelto=dinero_recibido- gasto

    parte_entera=int(vuelto)
    centavos=int(round(100*(vuelto-int(vuelto))))

    print("\nVuelto\n")

    print(f"Pesos:\n{parte_entera}")

    print(f"Centavos:\n{centavos}")

