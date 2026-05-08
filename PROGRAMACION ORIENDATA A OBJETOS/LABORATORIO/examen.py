from abc import ABC, abstractmethod

# =========================
# COMPONENTE INTERNO
# =========================
class NucleoEnergia:
    def __init__(self):
        self._energia = 100

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if not 0 <= valor <= 100:
            raise ValueError("La energía debe estar entre 0 y 100.")
        self._energia = valor


# =========================
# CLASE ABSTRACTA
# =========================
class Nave(ABC):
    total_fabricadas = 0

    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self._escudo = 100
        self.nucleo = NucleoEnergia()
        Nave.total_fabricadas += 1

    @property
    def energia(self):
        return self.nucleo.energia

    @property
    def escudo(self):
        return self._escudo

    @escudo.setter
    def escudo(self, valor):
        if valor < 0:
            self._escudo = 0
        else:
            self._escudo = valor

    @abstractmethod
    def mision(self, consumo):
        pass

    def __lt__(self, other):
        return self.energia < other.energia

    def __str__(self):
        return (f"Nave: {self.nombre} | Código: {self.codigo} | "
                f"Energía: {self.energia}% | Escudo: {self.escudo}%")

    @classmethod
    def total_naves(cls):
        return cls.total_fabricadas


# =========================
# NAVES ESPECÍFICAS
# =========================
class NaveCombate(Nave):
    def __init__(self, nombre, codigo, potencia):
        super().__init__(nombre, codigo)
        self.potencia = potencia

    def mision(self, consumo):
        if self.energia < consumo:
            raise ValueError("Energía insuficiente.")
        self.nucleo.energia -= consumo
        return f"Resultado: Desplegando ataque con potencia {self.potencia}."


class NaveCarga(Nave):
    def __init__(self, nombre, codigo, capacidad):
        super().__init__(nombre, codigo)
        self.capacidad = capacidad

    def mision(self, consumo):
        if self.energia < consumo:
            raise ValueError("Energía insuficiente.")
        self.nucleo.energia -= consumo
        return f"Resultado: Transporte de carga ({self.capacidad})."

    def __add__(self, other):
        if not isinstance(other, NaveCarga):
            raise TypeError("Solo se pueden fusionar naves de carga.")
        nueva = NaveCarga(
            nombre=f"{self.nombre}-{other.nombre}",
            codigo=f"{self.codigo}&{other.codigo}",
            capacidad=self.capacidad + other.capacidad
        )
        return nueva


class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, codigo, potencia, capacidad):
        Nave.__init__(self, nombre, codigo)
        self.potencia = potencia
        self.capacidad = capacidad

    def mision(self, consumo):
        if self.energia < consumo:
            raise ValueError("Energía insuficiente.")
        self.nucleo.energia -= consumo
        return (f"Resultado: Ataque ({self.potencia}) y "
                f"transporte ({self.capacidad}).")


# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    flota = []

    print(">>> ESTACIÓN AETHELGARD ACTIVADA <<<")

    while True:
        print("\n1. Registrar | 2. Misión | 3. Comparar | 4. Fusionar | 5. Stat")
        try:
            opcion = int(input("Seleccione acción: "))

            if opcion == 1:
                tipo = int(input("Tipo (1.Combate, 2.Carga, 3.Híbrida): "))
                nombre = input("Nombre: ")
                codigo = input("Código: ")

                if tipo == 1:
                    potencia = int(input("Potencia: "))
                    nave = NaveCombate(nombre, codigo, potencia)

                elif tipo == 2:
                    capacidad = int(input("Capacidad: "))
                    nave = NaveCarga(nombre, codigo, capacidad)

                elif tipo == 3:
                    potencia = int(input("Potencia: "))
                    capacidad = int(input("Capacidad: "))
                    nave = InterceptorHibrido(nombre, codigo, potencia, capacidad)

                else:
                    print("[ADVERTENCIA] Tipo inválido.")
                    continue

                flota.append(nave)
                print(f"Éxito. Total naves fabricadas: {Nave.total_naves()}")

            elif opcion == 2:
                idx = int(input("Índice de nave: "))
                consumo = int(input("Energía a consumir: "))
                print(flota[idx].mision(consumo))

            elif opcion == 3:
                i1 = int(input("Índice nave 1: "))
                i2 = int(input("Índice nave 2: "))
                if flota[i1] < flota[i2]:
                    print(f"{flota[i1].nombre} tiene menos energía.")
                else:
                    print(f"{flota[i2].nombre} tiene menos energía.")

            elif opcion == 4:
                i1 = int(input("Índice nave 1: "))
                i2 = int(input("Índice nave 2: "))
                nueva = flota[i1] + flota[i2]
                flota.append(nueva)
                print("Fusión completada.")

            elif opcion == 5:
                for i, nave in enumerate(flota):
                    print(f"[{i}] {nave}")

            else:
                break

        except (ValueError, TypeError, IndexError) as e:
            print(f"[ADVERTENCIA] Entrada inválida: {e}")


if __name__ == "__main__":
    main()