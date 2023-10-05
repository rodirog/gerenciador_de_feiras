

class Feira():
    def __init__(self, dias_semana: list, id: int, municipio: str, logradouro: str, numero_logradouro: int):
        self.__dias_semana = dias_semana
        self.__id = id
        self.__municipio = municipio
        self.__logradouro = logradouro
        self.__numero_logradouro = numero_logradouro

    @property
    def dias_semana(self):
        return self.__dias_semana

    @dias_semana.setter
    def dias_semana(self, dias_semana: list):
        self.__dias_semana = dias_semana

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio: str):
        self.__municipio = municipio

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro: str):
        self.__logradouro = logradouro

    @property
    def numero_logradouro(self):
        return self.__numero_logradouro

    @numero_logradouro.setter
    def numero_logradouro(self, numero_logradouro: int):
        self.__numero_logradouro = numero_logradouro