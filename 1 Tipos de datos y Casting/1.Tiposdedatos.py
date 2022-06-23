#Tarea Moral
"""
Cree 4 variables una de tipo string, una tipo float, una tipo int y una tipo booleana
Utilice casting para transformar la variable de tipo float a tipo int
luego cree una funcion que reste dos numeros
"""

#For in range
def menu(valor):
    match valor:
        case 0:
            print("Tenemos un 0")
        case 1:
            print("Tenemos un 1")
        case default:
            print("No tenemos ni un 0 ni un 1")
valor=int(input("Por favor brinde un valor: "))
menu(valor)