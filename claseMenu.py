from ClaseManejadorRegistros import ManejadorRegistros
from ClaseRegistro import Registro

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.TEST,
                            '5':self.salir
                          }
    def opcion(self, unManejadorRegistros, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(unManejadorRegistros)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorRegistros):
        if isinstance(unManejadorRegistros, ManejadorRegistros):
            unManejadorRegistros.mostrarTodosMayorMenor()


    def opcion2(self, unManejadorRegistros):
        if isinstance(unManejadorRegistros, ManejadorRegistros):
            unManejadorRegistros.mostrarTemperaturaPromedioTodasHoras()


    def opcion3(self, unManejadorRegistros):
        if isinstance(unManejadorRegistros, ManejadorRegistros):
            unManejadorRegistros.listarValoresUnDia()
    

    def TEST(self):
        registroPrueba = Registro(20, 40.5, 763.2)
        otroRegistroPrueba = Registro(20, 43.5, "80")
        print("TEST".center(100, "-"))
        print(registroPrueba)
        print(otroRegistroPrueba)