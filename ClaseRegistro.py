from numpy import isin


class Registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0
    
    def __init__(self, temperatura:float, humedad, presion):
        if isinstance(temperatura, float) or isinstance(temperatura, int):
            self.__temperatura = temperatura
        if isinstance(humedad, float) or isinstance(humedad, int):
            self.__humedad = humedad
        if isinstance(presion, float) or isinstance(presion, int):
            self.__presion = presion
    
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad
    
    def getPresion(self):
        return self.__presion
    
    def __str__(self):
        return "Temperatura: {0}\nHumedad: {1}\nPresion: {2}".format(self.getTemperatura(), self.getHumedad(), self.getPresion())