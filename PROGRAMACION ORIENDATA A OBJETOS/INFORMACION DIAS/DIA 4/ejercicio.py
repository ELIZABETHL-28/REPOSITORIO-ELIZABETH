class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100

    def alimentar(self):
        if self.energia < 100:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
            print(f"{self.nombre} ha comido. Energía actual: {self.energia}")
        else:
            print(f"{self.nombre} ya tiene energía completa.")

    def jugar(self):
        if self.energia >= 30:
            self.energia -= 30
            print(f"Has jugado con {self.nombre}. Energía actual: {self.energia}")
        else:
            print(f"{self.nombre} está muy cansada para jugar (Energía: {self.energia})")


# ---------------- PROGRAMA PRINCIPAL ----------------

nombre = input("¿Cómo se llamará tu mascota? ")
mi_mascota = Mascota(nombre)

while mi_mascota.energia > 0:
    print("\n¿Qué deseas hacer?")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_mascota.alimentar()
    elif opcion == "2":
        mi_mascota.jugar()
    elif opcion == "3":
        print("Saliendo del juego...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")

if mi_mascota.energia <= 0:
    print(f"\n{mi_mascota.nombre} se quedó sin energía. Fin del juego.")