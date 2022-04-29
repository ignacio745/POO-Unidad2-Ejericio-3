from claseMenu import Menu
from ClaseManejadorRegistros import ManejadorRegistros


if __name__=="__main__":

    unManejadorRegistros = ManejadorRegistros()
    unManejadorRegistros.cargarCSV("datos.csv")

    unMenu = Menu()


    opcion = 0

    while opcion != "5":
        print("MENU".center(100, "-"))
        print("[1] Mostrar los dias y horas de los valores mayores y menores de las variables")
        print("[2] Mostrar las temperaturas promedio del mes por hora")
        print("[3] Mostrar los valores de un dia dado")
        print("[4] Ejecutar test")
        print("[5] Salir")
        opcion = input("Ingrese la opcion: ")
        unMenu.opcion(unManejadorRegistros, opcion)
