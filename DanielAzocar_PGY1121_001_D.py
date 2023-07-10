from os import system
system('cls')

asientos= [[0 for x in range(10)] for y in range(10)]

precio= [120000 if i<20 else 80000 if i >50 else 50000 for i in range(10)  ] 

ganancias=0

def comprar():
    asiento=int(input("Ingrese el numero del asiento a escoger del 1 al 100: "))
    while asiento<1 or asiento>100:
        print("** Asiento invalido  **")
        asiento=int(input("Ingrese el numero del asiento a escoger del 1 al 100: "))
    





while True:
    print("Entradas concierto de Michael Jam")
    print("1- Comprar entradas")
    print("2- Mostrar ubicaciones disponibles")
    print("3- Ver listado de asistentes")
    print("4- Mostrar ganancias totales")
    print("5- Salir")

    opc=input()
    
    if opc =='1':
        comprar()
    elif opc =='2':
        print()
    elif opc =='3':
        print
    elif opc =='4':
        print()
    elif opc =='5':
        print("Saliendo del sistema....")
        print("Daniel Azocar ")
        print("10/07/2023")
        break
        
    
    