# # MODELO
# class Libro(): 
#     def __init__(self, id, titulo, autor):
#         self.id = id
#         self.titulo = titulo
#         self.autor = autor
#         self.prestado = False 

# # VISTA
# class VistaBiblioteca(): 
#     @staticmethod   
#     def mostrar_menu(): 
#         print("\n1 - AGREGAR NUEVO LIBRO\n2 - LISTA DE LIBROS \n 3 - PRESTAR LIBRO(POR ID) \n 4 - SALIR")
#         return input("OPCION: ")
    
#     @staticmethod
#     def pedir_datos_libro():
#         print("============================================")
#         id = input("ID DEL LIBRO: ")
#         titulo = input("TITULO: ")
#         autor = input("AUTOR: ")
#         print("============================================")
#         return id, titulo, autor 
    
#     @staticmethod
#     def buscar_por_id(): 
#         return input("ID-LIBRO A PRESTAR: ")
    
#     @staticmethod
#     def mostrar_lista(lista): 
#         print("============================================")
#         print("\nLISTA DE LIBROS: ")
        
#         for libros in lista: 
#             estado = "Prestado" if libros.prestado else "Disponible"
#             print(f"{libros.id} - {libros.titulo} - {libros.autor} - {estado}") 
#         print("============================================")   

    
#     @staticmethod
#     def mostrar_mensaje(mensaje):
#         print(mensaje)

# # CONTROLADOR 
# class ControladorBiblioteca():
#     def __init__(self):
#         self.libros = []
#         self.vista = VistaBiblioteca()

#     def ejecutar(self):
#         while True:
#             opcion = self.vista.mostrar_menu()

#             if opcion == "1":
#                 id, titulo, autor = self.vista.pedir_datos_libro()
#                 libro = Libro(id, titulo, autor)
#                 self.libros.append(libro)

#             elif opcion == "2":
#                 self.vista.mostrar_lista(self.libros)

#             elif opcion == "3":
#                 id = self.vista.buscar_por_id()
#                 encontrado = False
#                 for libro in self.libros:
#                     if libro.id == id and not libro.prestado:
#                         libro.prestado = True
#                         encontrado = True
#                         break

#                 if encontrado:
#                     self.vista.mostrar_mensaje("LIBRO PRESTADO.")
#                 else:
#                     self.vista.mostrar_mensaje("LIBRO NO ENCONTRADO/YA PRESTADO.")

#             elif opcion == "4":
#                 self.vista.mostrar_mensaje("SALIENDO...")
#                 break

# if __name__ == "__main__":
#     controlador = ControladorBiblioteca()
#     controlador.ejecutar()












# import json
# from abc import ABC, abstractmethod

# # ==================================================
# # CONFIGURACIÓN (JSON SIMULADO)
# # ==================================================

# contenido_json = """
# [
#     {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
#     {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
#     {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
# ]
# """

# # ==================================================
# # MODELO
# # ==================================================

# class FuenteEnergia(ABC):
#     def __init__(self, id_generador, capacidad_maxima, tipo):
#         self.id_generador = id_generador
#         self.capacidad_maxima = float(capacidad_maxima)
#         self.produccion_actual = 0.0
#         self.tipo = tipo

#     @abstractmethod
#     def generar(self):
#         pass


# class PanelSolar(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima):
#         super().__init__(id_generador, capacidad_maxima, "solar")

#     def generar(self, clima=None):
#         if clima == "soleado":
#             self.produccion_actual = self.capacidad_maxima
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual


# class TurbinaEolica(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima):
#         super().__init__(id_generador, capacidad_maxima, "eolica")

#     def generar(self, velocidad_viento=0.0):
#         self.produccion_actual = min(self.capacidad_maxima, velocidad_viento * 2)
#         return self.produccion_actual


# class GeneradorDiesel(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima, combustible):
#         super().__init__(id_generador, capacidad_maxima, "diesel")
#         self.combustible = float(combustible)

#     def generar(self):
#         if self.combustible > 0:
#             self.produccion_actual = min(self.capacidad_maxima, self.combustible)
#             self.combustible -= self.produccion_actual
#             self.combustible = max(0, self.combustible)
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual


# # ==================================================
# # FABRICA
# # ==================================================

# class FabricaEnergia:
#     REGISTRO = {
#         "solar": PanelSolar,
#         "eolica": TurbinaEolica,
#         "diesel": GeneradorDiesel
#     }

#     @staticmethod
#     def crear_fuente(datos):
#         tipo = datos["tipo"]
#         clase = FabricaEnergia.REGISTRO.get(tipo)

#         if not clase:
#             raise ValueError("Tipo de energía no soportado")

#         if tipo == "diesel":
#             return clase(
#                 datos["id_generador"],
#                 datos["capacidad_maxima"],
#                 datos["combustible"]
#             )

#         return clase(
#             datos["id_generador"],
#             datos["capacidad_maxima"]
#         )


# # ==================================================
# # VISTA
# # ==================================================

# class InterfazRed:
#     def pedir_clima(self):
#         return input("Ingrese el clima (soleado / nublado): ").lower()

#     def pedir_viento(self):
#         return float(input("Ingrese velocidad del viento: "))

#     def mostrar_tablero(self, fuentes):
#         print("\n" + "=" * 40)
#         print("   ESTADO DE LA RED ELÉCTRICA")
#         print("=" * 40)
#         for f in fuentes:
#             print(f"{f.id_generador}: {f.produccion_actual} MW")
#         print("=" * 40)

#     def mostrar_error(self, mensaje):
#         print(f"[ERROR] {mensaje}")


# # ==================================================
# # CONTROLADOR
# # ==================================================

# class ControladorRed:
#     def __init__(self):
#         self.vista = InterfazRed()
#         self.fuentes = []

#     def cargar_datos(self):
#         datos = json.loads(contenido_json)

#         for item in datos:
#             self.fuentes.append(FabricaEnergia.crear_fuente(item))

#     def guardar_datos(self):
#         datos = []

#         for f in self.fuentes:
#             info = {
#                 "tipo": f.tipo,
#                 "id_generador": f.id_generador,
#                 "capacidad_maxima": f.capacidad_maxima
#             }

#             if isinstance(f, GeneradorDiesel):
#                 info["combustible"] = f.combustible

#             datos.append(info)

#         print("\nCONFIGURACIÓN FINAL (SIMULANDO GUARDADO):")
#         print(json.dumps(datos, indent=4))

#     def ejecutar(self):
#         try:
#             self.cargar_datos()

#             clima = self.vista.pedir_clima()
#             viento = self.vista.pedir_viento()

#             for fuente in self.fuentes:
#                 if isinstance(fuente, PanelSolar):
#                     fuente.generar(clima)
#                 elif isinstance(fuente, TurbinaEolica):
#                     fuente.generar(viento)
#                 else:
#                     fuente.generar()

#             self.vista.mostrar_tablero(self.fuentes)

#             # Guardado simulado
#             self.guardar_datos()

#         except Exception as e:
#             self.vista.mostrar_error(str(e))


# # ==================================================
# # MAIN
# # ==================================================

# if __name__ == "__main__":
#     ControladorRed().ejecutar()


import json
from abc import ABC, abstractmethod

# ==================================================
# CONFIGURACIÓN (JSON SIMULADO)
# ==================================================

contenido_json = """
[
    {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
    {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
    {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
]
"""

# ==================================================
# MODELO
# ==================================================

class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima, tipo):
        self.id_generador = id_generador
        self.capacidad_maxima = float(capacidad_maxima)
        self.produccion_actual = 0.0
        self.tipo = tipo

    @abstractmethod
    def generar(self):
        pass


class PanelSolar(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima):
        super().__init__(id_generador, capacidad_maxima, "solar")

    def generar(self, clima=None):
        if clima == "soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual


class TurbinaEolica(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima):
        super().__init__(id_generador, capacidad_maxima, "eolica")

    def generar(self, velocidad_viento=0.0):
        produccion = velocidad_viento * 2

        if produccion > self.capacidad_maxima:
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = produccion

        return self.produccion_actual


class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima, "diesel")
        self.combustible = float(combustible)

    def generar(self):
        if self.combustible > 0:

            if self.combustible > self.capacidad_maxima:
                self.produccion_actual = self.capacidad_maxima
            else:
                self.produccion_actual = self.combustible

            self.combustible = self.combustible - self.produccion_actual

            if self.combustible < 0:
                self.combustible = 0

        else:
            self.produccion_actual = 0.0

        return self.produccion_actual


# ==================================================
# FABRICA
# ==================================================

class FabricaEnergia:
    REGISTRO = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_fuente(datos):
        tipo = datos["tipo"]
        clase = FabricaEnergia.REGISTRO.get(tipo)

        if not clase:
            raise ValueError("Tipo de energía no soportado")

        if tipo == "diesel":
            return clase(
                datos["id_generador"],
                datos["capacidad_maxima"],
                datos["combustible"]
            )

        return clase(
            datos["id_generador"],
            datos["capacidad_maxima"]
        )


# ==================================================
# VISTA
# ==================================================

class InterfazRed:
    def pedir_clima(self):
        return input("Ingrese el clima (soleado / nublado): ").lower()

    def pedir_viento(self):
        return float(input("Ingrese velocidad del viento: "))

    def mostrar_tablero(self, fuentes):
        print("\n" + "=" * 40)
        print("   ESTADO DE LA RED ELÉCTRICA")
        print("=" * 40)
        for f in fuentes:
            print(f"{f.id_generador}: {f.produccion_actual} MW")
        print("=" * 40)

    def mostrar_error(self, mensaje):
        print(f"[ERROR] {mensaje}")


# ==================================================
# CONTROLADOR
# ==================================================

class ControladorRed:
    def __init__(self):
        self.vista = InterfazRed()
        self.fuentes = []

    def cargar_datos(self):
        datos = json.loads(contenido_json)

        for item in datos:
            self.fuentes.append(FabricaEnergia.crear_fuente(item))

    def guardar_datos(self):
        datos = []

        for f in self.fuentes:
            info = {
                "tipo": f.tipo,
                "id_generador": f.id_generador,
                "capacidad_maxima": f.capacidad_maxima
            }

            if isinstance(f, GeneradorDiesel):
                info["combustible"] = f.combustible

            datos.append(info)

        print("\nCONFIGURACIÓN FINAL (SIMULANDO GUARDADO):")
        print(json.dumps(datos, indent=4))

    def ejecutar(self):
        try:
            self.cargar_datos()

            clima = self.vista.pedir_clima()
            viento = self.vista.pedir_viento()

            for fuente in self.fuentes:
                if isinstance(fuente, PanelSolar):
                    fuente.generar(clima)
                elif isinstance(fuente, TurbinaEolica):
                    fuente.generar(viento)
                else:
                    fuente.generar()

            self.vista.mostrar_tablero(self.fuentes)

            self.guardar_datos()

        except Exception as e:
            self.vista.mostrar_error(str(e))


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":
    ControladorRed().ejecutar()