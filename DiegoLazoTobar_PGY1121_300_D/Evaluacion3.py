import csv
import os
import time

contticket = 0

datoscliente = {
            
    "Nombre":[],
    "Direccion":[],
    "Telefono":[],
    
}

listaproductos = {
    
    "Abono":[],
    "Tierra":[],
    "Lirio":[],
    "Rosas rojas":[],
    "Margaritas":[]
}

print("¡Hola! Bienvenido(a) a GreenGarden, la pagina de venta de plantas y flores.")

time.sleep(2)
os.system("cls")

print("Para empezar a comprar")

os.system("cls")

fecha = "28/06/2024"

contadorabn = 0
contadortrr = 0
contadorlr = 0
contadorrr = 0
contadorms = 0

productoticket = ""

abn = "Abono"
trr = "Tierra"
lr = "Lirio"
rr = "Rosas rojas"
ms = "Margaritas"

precioabn = 1200
preciotrr = 1000
preciolr = 1100
preciorr = 1700
precioms = 1100

totalproductoabn = 0
totalproductotrr = 0
totalproductolr = 0
totalproductorr = 0
totalproductoms = 0

totalproducto = 0

stockabn = 50
stocktrr = 35
stocklr = 40
stockrr = 43
stockms = 10

while True:
    while True:
        
        nombrecliente = str(input("Ingrese su nombre: "))
        direccion = str(input("Ingrese su direccion: "))
        telefono = str(input("Ingrese su telefono: "))

        datoscliente["Nombre"].append(nombrecliente)
        datoscliente["Direccion"].append(direccion)
        datoscliente["Telefono"].append(telefono)
        
        print("¿Que productos desea comprar?")
        print("1.- Abono : $1.200")
        print("2.- Tierra : $1.000")
        print("3.- Lirio : $1.100")
        print("4.- Rosas rojas: $1700")
        print("5.- Margaritas: $1.100")
        print("6.- Pagar")

        producto = str(input("Coloca el numero del producto que desea adquerir (de querer pagar, colocar 6): "))

        if producto == "1" or producto == "2" or producto == "3" or producto == "4" or producto == "5" or producto == "6":
                    print()
        else:
            while True:
                print("Elige un producto valido")
                producto = str(input())
                if producto == "1" or producto == "2" or producto == "3" or producto == "4" or producto == "5" or producto == "6":
                    break
        
        while True:
            
            while True:

                # ------------------------------------------------

                if producto == "1":
                    abonopreg = int(input("¿Cuanto deseas adquerir?: "))
                    if abonopreg <= stockabn:
                        contadorabn += abonopreg
                        totalproductoabn += abonopreg * precioabn
                        stockabn -= abonopreg
                        print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                    else:
                        while True:
                            print(f"Solo hay un stock de {stockabn}, vuelve a elegir una cantidad menor a tal.")
                            abonopreg = int(input())
                            if abonopreg <= stockabn:
                                contadorabn += abonopreg
                                totalproductoabn += abonopreg * precioabn
                                stockabn -= abonopreg
                                print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                                break

                # ------------------------------------------------

                if producto == "2":
                    tierrapreg = int(input("¿Cuanto deseas adquerir?: "))
                    if tierrapreg <= stocktrr:
                        contadortrr += tierrapreg
                        totalproductotrr += tierrapreg * preciotrr
                        stocktrr -= tierrapreg
                        print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                    else:
                        while True:
                            print(f"Solo hay un stock de {stocktrr}, vuelve a elegir una cantidad menor a tal.")
                            tierrapreg = int(input())
                            if tierrapreg <= stocktrr:
                                contadortrr += tierrapreg
                                totalproductotrr += tierrapreg * preciotrr
                                stocktrr -= tierrapreg
                                print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                                break

                # ------------------------------------------------
    
                if producto == "3":
                    liriopreg = int(input("¿Cuanto deseas adquerir?: "))
                    if liriopreg <= stocklr:
                        contadorlr += liriopreg
                        totalproductolr += liriopreg * preciolr
                        stocklr -= liriopreg
                        print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                    else:
                         while True:
                            print(f"Solo hay un stock de {stocklr}, vuelve a elegir una cantidad menor a tal.")
                            liriopreg = int(input())
                            if liriopreg <= stocklr:
                                contadorlr += liriopreg
                                totalproductolr += liriopreg * preciolr
                                stocklr -= liriopreg
                                print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                                break

                # ------------------------------------------------

                if producto == "4":
                    rosasrojaspreg = int(input("¿Cuanto deseas adquerir?: "))
                    if rosasrojaspreg <= stockrr:
                        preciorr += rosasrojaspreg
                        totalproductorr += rosasrojaspreg * preciorr
                        stockrr -= rosasrojaspreg
                        print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                    else:
                        while True:
                            print(f"Solo hay stock de {stockrr}, vuelve a elegir una cantidad menor a tal.")
                            rosasrojaspreg = int(input())
                            if rosasrojaspreg <= stockrr:
                                contadorrr += rosasrojaspreg
                                totalproductorr += rosasrojaspreg * preciorr
                                stockrr -= rosasrojaspreg
                                print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                                break
                
                # ------------------------------------------------

                if producto == "5":
                    margaritaspreg = int(input("¿Cuanto deseas adquerir?: "))
                    if margaritaspreg <= stockms:
                        precioms += stockms
                        totalproductoms += margaritaspreg * precioms
                        stockms -= margaritaspreg
                        print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                    else:
                        while True:
                            print(f"Solo hay stock de {stockms}, vuelve a elegir una cantidad menor a tal.")
                            margaritaspreg = int(input())
                            if margaritaspreg <= stockms:
                                contadorms += margaritaspreg
                                totalproductoms += margaritaspreg * precioms
                                stockms -= margaritaspreg
                                print("¿Que otro producto desea aquerir? (de querer pagar, colocar 6)")
                                break
                
                # ------------------------------------------------

                producto = str(input())


                if producto == "6":
                    break

            print("¿Deseas salir?")
            print("1.- Si")
            print("2.- No")
            resp11 = str(input())

            if resp11 == "1":
                break
            elif resp11 == "2":
                print()
            else:
                while True:
                    print("Ingresa una opcion correcta")
                    resp11 = str(input())
                    if resp11 == "1":
                        break
                    elif resp11 == "2":
                        break
            if resp11 == "1":
                break
            elif resp11 == "2":

                producto = str(input("Coloca el numero del producto que desea adquerir (de querer pagar, colocar 6): "))

                if producto == "1" or producto == "2" or producto == "3" or producto == "4" or producto == "5" or producto == "6":
                    print()
                else:
                    while True:
                        print("Elige un producto valido")
                        producto = str(input())
                        if producto == "1" or producto == "2" or producto == "3" or producto == "4" or producto == "5" or producto == "6":
                            break

        totalproducto = totalproductoabn + totalproductotrr + totalproductolr + totalproductorr + totalproductoms
    
        abono = f"Cantidad = {contadorabn}, Precio total: = {totalproductoabn}"
        tierra = f"Cantidad = {contadortrr}, Precio total: = {totalproductotrr}"
        lirio = f"Cantidad = {contadorlr}, Precio total: = {totalproductolr}"
        rosasRojas = f"Cantidad = {contadorrr}, Precio total: = {totalproductorr}"
        margaritas = f"Cantidad = {contadorms}, Precio total: = {totalproductoms}"

        listaproductos["Abono"].append(abono)
        listaproductos["Tierra"].append(tierra)
        listaproductos["Lirio"].append(lirio)
        listaproductos["Rosas rojas"].append(rosasRojas)
        listaproductos["Margaritas"].append(margaritas)
                
        contticket += 1
        
        os.system("cls")

        # writerow = fila, writerows = filas (se empieza con writerow)

        with open(f"DiegoLazoTobar_PGY1121_300_D/Tickets/Ticket{contticket}.csv", encoding="utf-8" , mode="w") as archivoCsv:
            # --------------------------------------------------------------------------------------
            escribirCsv= csv.writer(archivoCsv)
            escribirCsv.writerow([f"---------------- DATOS CLIENTE TICKET N {contticket} ----------------"])
            escribirCsv= csv.writer(archivoCsv)
            escribirCsv.writerows(datoscliente.items())
            # --------------------------------------------------------------------------------------
            escribirCsv= csv.writer(archivoCsv)
            escribirCsv.writerow([f"---------------- PRODUCTOS CLIENTE ----------------"])
            escribirCsv.writerows(listaproductos.items())
            # --------------------------------------------------------------------------------------
            escribirCsv.writerow([f"---------------- OTROS DATOS ----------------"])
            escribirCsv= csv.writer(archivoCsv)
            escribirCsv.writerow([f"Fecha compra: {fecha}"])
            escribirCsv= csv.writer(archivoCsv)
            escribirCsv.writerow([f"Total compra: {totalproducto}"])
            # --------------------------------------------------------------------------------------
            
            archivoCsv.close
            
            print(f"Creando ticket N {contticket}...")
            
            time.sleep(3)
            os.system("cls")
            
        print(f"¡Ticket N {contticket} creado!")
        time.sleep(3)
        os.system("cls")
        break
    break