class Asiento:
    def __init__(self, color:str, precio:int, registro:int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color:str) -> None:
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Motor(object):
    def __init__(self, numeroCilindros:int, tipo:str, registro:int):
        super(Motor, self).__init__()
        self.numeroCilindros:int = numeroCilindros
        self.tipo:str = tipo
        self.registro:int = registro

    def cambiarRegistro(self, registro:int) -> None:
        self.registro = registro
    
    def asignarTipo(self, tipo:str) -> None:
        tiposMotor = ("electrico", "gasolina")
        if tipo in tiposMotor:
            self.tipo = tipo

class Auto(object):
    cantidadCreados = 0
    def __init__(self, modelo:str, precio:int, asientos:list[Asiento], marca:str, motor:Motor, registro:int):
        super(Auto, self).__init__()
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def catidadAsientos(self, ) -> int:
        return len(self.asientos)

    def verificarIntegridad(self) -> str:
        #que el atributo registro de Motor, Auto y Cada Asiento sean el mismo

        for asiento in self.asientos:
            if asiento == None: continue

            if asiento.registro != self.motor.registro or asiento.registro != self.registro:
                return "Las piezas no son originales"

        return "Auto original"
