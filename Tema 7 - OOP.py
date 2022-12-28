from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, PI=3.14):
        self.PI = PI

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        return "Cel mai probabil am colturi"


class Patrat(FormaGeometrica):
    def __init__(self, PI, latura):
        super().__init__(PI)
        self._latura = latura

    def get_latura(self):
        return self._latura

    def set_latura(self):
        return self._latura

    def del_latura(self):
        del self._latura

    def aria(self):
        return self._latura * self._latura


class Cerc(FormaGeometrica):
    def __init__(self, PI, raza):
        super().__init__(PI)
        self._raza = raza

    def get_raza(self):
        return self._raza

    def set_raza(self):
        return self._raza

    def del_raza(self):
        del self._raza

    def aria(self):
        return self.PI ** self._raza

    def descrie(self):
        return "Eu nu am colturi"


patrat = Patrat(3.14,int(input("Introdu latura: ")))
print(patrat.descrie())
print(patrat.aria())
print(patrat.get_latura())
print(patrat.set_latura())
print(patrat.del_latura())
cerc = Cerc(3.14,int(input("Introdu raza: ")))
print(cerc.aria())
print(cerc.descrie())
print(cerc.get_raza())
print(cerc.set_raza())
print(cerc.del_raza())
