from persistencia.dao import DAO
from entidade.Feira import Feira

class FeiraDAO(DAO):
    def __init__(self):
        super().__init__('feiras.pkl')

    def add(self, feira: Feira):
        if isinstance(feira.id, int) and (feira is not None) \
                and isinstance(feira, Feira):
            super().add(feira.id, feira)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()
