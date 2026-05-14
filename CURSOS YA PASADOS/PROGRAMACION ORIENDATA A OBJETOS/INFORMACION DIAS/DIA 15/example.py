# # # # EJEMPLO 1 
# # # from abc import ABC, abstractmethod
# # # class Personaje(ABC):
# # #     @abstractmethod
# # #     def atacar(self): 
# # #         pass
    
# # # class Guerrero(Personaje): 
# # #     def atacar(self): return "Ataca con espada"
    
# # # class Mago(Personaje): 
# # #     def atacar(self): return "Ataca con magia"
    
# # # # LA FABRICA (EL CORAZON DEL PATRON)
# # # class FabricaPersonajes(): 
# # #     @staticmethod # VIVE DENTRO DE LA CLASE, NO SABE NADA DE LA CLASE. SOLO NOR SIRVE PARA 
# # #     # UNA FUNCION NORMAL COMUN, POR ORGANIZACION ENTONCES NO VAMOS A METER EL SELF.
# # #     def crear_personaje(tipo): 
# # #         #ESTE METODO CENTRALIZA TODA LA LOGICA DE CRECION 
# # #         tipo = tipo.lower()
        
# # #         if tipo == "guerrero":
# # #             return Guerrero()
# # #         elif tipo == "mago": 
# # #             return Mago()
# # #         else: 
# # #             raise ValueError(f"LA FABRICA NO SABE CREAR: {tipo}")
        
# # # try: 
# # #     eleccion = input("QUE PERSONAJE DESEA: GUERREO/MAGO)")
# # #     heroe = FabricaPersonajes.crear_personaje(eleccion)
# # #     print("heroe.atacar")
    
# # # except ValueError as error:
# # #      print (error)
        
        
# # # fabrica = FabricaPersonajes()
# # # fabrica.crear_personaje()

# # # personaje = FabricaPersonajes.crear_personaje("mago")
# # # # por organizacion

# # # =================================================================================
# # # # EJEMPLO 2 MODELO (LOGICA PURA)

# # # class Tarea(): 
# # #     def __init__(self, descripcion):
# # #         self.descripcion = descripcion
# # #         self.completada = False 

# # # # VISTA        
# # # class VistaTarea(): 
# # #     @staticmethod
# # #     def mostrar_menu():
# # #         print("\n1 - AGREGAR TAREA\n2 - MOSTRAR TAREA \n3 - SALIR")
# # #         return input("OPCION: ")
    
# # #     @staticmethod
# # #     def mostrar_lista(lista): 
# # #         print("\nLISTA DE TAREAS: ")
        
# # #         for tarea in lista:
# # #             estado = "Completada" if tarea.completada else "Pendiente" 
# # #             print(f"{tarea.descripcion} esta en estado: {estado}" )
      
# # #     @staticmethod
# # #     def solicitar_descripcion(): 
# # #         return input("DESCRIPCION DE LA TEREA: ")  
    
# # #     @staticmethod
# # #     def mostrar_mensaje(mensaje): 
# # #         print(mensaje)
# # # # CONTROLADOR 
# # # class ControladorTareas(): 
# # #     def __init__(self):
# # #         self.tareas = []
# # #         self.vista = VistaTarea()
        
# # #     def ejecutar(self): 
# # #         while True: 
# # #             opcion = self.vista.mostrar_menu()
# # #             if opcion == "1": 
# # #                 descripcion = self.vista.solicitar_descripcion()
# # #                 tarea = Tarea(descripcion)
# # #                 self.tareas.append(tarea)
# # #             elif opcion == "2": 
# # #                 self.vista.mostrar_lista(self.tareas)
# # #             elif opcion == "3": 
# # #                 self.vista.mostrar_mensaje("SALIENDO...")
# # #                 break
                
# # # if __name__ == "__main__": 
# # #     controlador = ControladorTareas()
# # #     controlador = controlador.ejecutar()
    
                
# # from abc import ABC, abstractmethod
# # import uuid


# # # ==================================================
# # # EXCEPCIÓN PERSONALIZADA
# # # ==================================================
# # class EnergiaInvalidaError(Exception):
# #     """Error lanzado cuando la energía es negativa"""
# #     pass


# # # ==================================================
# # # CLASE NUCLEO (COMPOSICIÓN)
# # # ==================================================
# # class Nucleo:
# #     def __init__(self):
# #         self.id = uuid.uuid4()


# # # ==================================================
# # # CLASE ABSTRACTA BASE
# # # ==================================================
# # class EntidadBase(ABC):

# #     def __init__(self, energia):
# #         if energia < 0:
# #             raise EnergiaInvalidaError("La energía no puede ser negativa")
# #         self.energia = energia
# #         self.nucleo = Nucleo()  # Composición

# #     @abstractmethod
# #     def alimentarse(self, cantidad=10):
# #         pass

# #     # Sobrecarga del operador +
# #     def __add__(self, otra):
# #         if not isinstance(otra, EntidadBase):
# #             return NotImplemented
# #         return self.energia + otra.energia


# # # ==================================================
# # # HERENCIA SIMPLE
# # # ==================================================
# # class Sintetizador(EntidadBase):

# #     def alimentarse(self, cantidad=10):
# #         self.energia += cantidad
# #         print(f"Sintetizador genera energía (+{cantidad}). Energía actual: {self.energia}")


# # class Consumidor(EntidadBase):

# #     def alimentarse(self, cantidad=10):
# #         self.energia += cantidad
# #         print(f"Consumidor consume energía (+{cantidad}). Energía actual: {self.energia}")


# # # ==================================================
# # # HERENCIA MÚLTIPLE
# # # ==================================================
# # class Hibrido(Sintetizador, Consumidor):

# #     def alimentarse(self, cantidad=10):
# #         energia_total = cantidad * 2
# #         self.energia += energia_total
# #         print(f"Híbrido usa doble fuente (+{energia_total}). Energía actual: {self.energia}")


# # # ==================================================
# # # POLIMORFISMO
# # # ==================================================
# # def iniciar_ciclo_vital(lista_entidades):
# #     print("\n--- INICIANDO CICLO VITAL ---")
# #     for entidad in lista_entidades:
# #         entidad.alimentarse()


# # # ==================================================
# # # SIMULACIÓN CON ENTRADA DE USUARIO
# # # ==================================================
# # def crear_entidad():
# #     while True:
# #         print("\n¿Qué tipo de entidad desea crear?")
# #         print("1. Sintetizador")
# #         print("2. Híbrido")
# #         opcion = input("Seleccione una opción: ")

# #         if opcion not in ("1", "2"):
# #             print("❌ Opción no válida, intente de nuevo.")
# #             continue

# #         try:
# #             energia = int(input("Ingrese la energía inicial: "))
# #             if opcion == "1":
# #                 return Sintetizador(energia)
# #             else:
# #                 return Hibrido(energia)

# #         except ValueError:
# #             print("❌ Error: debe ingresar un número entero.")
# #         except EnergiaInvalidaError as e:
# #             print(f"❌ Error: {e}")


# # # ==================================================
# # # PROGRAMA PRINCIPAL
# # # ==================================================
# # if __name__ == "__main__":
# #     entidades = []

# #     for _ in range(2):
# #         entidad = crear_entidad()
# #         entidades.append(entidad)

# #     iniciar_ciclo_vital(entidades)

# #     print("\nSuma de energías de las entidades:")
# #     print(entidades[0] + entidades[1])


# import json
# from abc import ABC, abstractmethod

# # =========================
# # CONFIGURACIÓN (DADA)
# # =========================

# contenido_json = """
# [
#     {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
#     {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
#     {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
# ]
# """


# # =========================
# # MODELO
# # =========================

# class FuenteEnergia(ABC):
#     def __init__(self, id_generador, capacidad_maxima):
#         self.id_generador = id_generador
#         self.capacidad_maxima = float(capacidad_maxima)
#         self.produccion_actual = 0.0

#     @abstractmethod
#     def generar(self, **kwargs):
#         pass


# class PanelSolar(FuenteEnergia):
#     def generar(self, clima=None):
#         if clima == "soleado":
#             self.produccion_actual = self.capacidad_maxima
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual


# class TurbinaEolica(FuenteEnergia):
#     def generar(self, velocidad_viento=0.0):
#         self.produccion_actual = min(self.capacidad_maxima, velocidad_viento * 2)
#         return self.produccion_actual


# class GeneradorDiesel(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima, combustible):
#         super().__init__(id_generador, capacidad_maxima)
#         self.combustible = float(combustible)

#     def generar(self):
#         if self.combustible > 0:
#             self.produccion_actual = min(self.capacidad_maxima, self.combustible)
#             self.combustible -= self.produccion_actual
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual


# # =========================
# # FÁBRICA (FACTORY)
# # =========================

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


# # =========================
# # VISTA
# # =========================

# class InterfazRed:
#     def pedir_clima(self):
#         return input("Ingrese el clima (soleado / nublado): ").lower()

#     def pedir_viento(self):
#         return float(input("Ingrese velocidad del viento: "))

#     def mostrar_tablero(self, fuentes):
#         print("\n" + "*" * 40)
#         print("   ESTADO DE LA RED ELÉCTRICA")
#         print("*" * 40)
#         for f in fuentes:
#             print(f"{f.id_generador}: {f.produccion_actual} MW")
#         print("*" * 40)

#     def mostrar_error(self, mensaje):
#         print(f"[ERROR] {mensaje}")


# # =========================
# # CONTROLADOR
# # =========================

# class ControladorRed:
#     def __init__(self):
#         self.vista = InterfazRed()
#         self.fuentes = []

#     def cargar_datos(self):
#         datos = json.loads(contenido_json)
#         for item in datos:
#             self.fuentes.append(FabricaEnergia.crear_fuente(item))

#     def ejecutar(self):
#         try:
#             self.cargar_datos()

#             clima = self.vista.pedir_clima()
#             viento = self.vista.pedir_viento()

#             for fuente in self.fuentes:
#                 if isinstance(fuente, PanelSolar):
#                     fuente.generar(clima=clima)
#                 elif isinstance(fuente, TurbinaEolica):
#                     fuente.generar(velocidad_viento=viento)
#                 else:
#                     fuente.generar()

#             self.vista.mostrar_tablero(self.fuentes)

#         except Exception as e:
#             self.vista.mostrar_error(str(e))


# # =========================
# # MAIN
# # # =========================

# if __name__ == "__main__":
#     ControladorRed().ejecutar()
               
                
import json
from abc import ABC, abstractmethod

# =========================
# CONFIGURACIÓN (DADA)
# =========================

contenido_json = """
[
    {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
    {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
    {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
]
"""


# =========================
# MODELO
# =========================

class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima):
        self.id_generador = id_generador
        self.capacidad_maxima = float(capacidad_maxima)
        self.produccion_actual = 0.0

    @abstractmethod
    def generar(self, **kwargs):
        pass


class PanelSolar(FuenteEnergia):
    def generar(self, clima=None):
        if clima == "soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual


class TurbinaEolica(FuenteEnergia):
    def generar(self, velocidad_viento=0.0):
        self.produccion_actual = min(self.capacidad_maxima, velocidad_viento * 2)
        return self.produccion_actual


class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima)
        self.combustible = float(combustible)

    def generar(self):
        if self.combustible > 0:
            self.produccion_actual = min(self.capacidad_maxima, self.combustible)
            self.combustible -= self.produccion_actual
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual


# =========================
# FÁBRICA (FACTORY)
# =========================

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


# =========================
# VISTA
# =========================

class InterfazRed:
    def pedir_clima(self):
        return input("Ingrese el clima (soleado / nublado): ").lower()

    def pedir_viento(self):
        return float(input("Ingrese velocidad del viento: "))

    def mostrar_tablero(self, fuentes):
        print("\n" + "*" * 40)
        print("   ESTADO DE LA RED ELÉCTRICA")
        print("*" * 40)
        for f in fuentes:
            print(f"{f.id_generador}: {f.produccion_actual} MW")
        print("*" * 40)

    def mostrar_error(self, mensaje):
        print(f"[ERROR] {mensaje}")


# =========================
# CONTROLADOR
# =========================

class ControladorRed:
    def __init__(self):
        self.vista = InterfazRed()
        self.fuentes = []

    def cargar_datos(self):
        datos = json.loads(contenido_json)
        for item in datos:
            self.fuentes.append(FabricaEnergia.crear_fuente(item))

    def ejecutar(self):
        try:
            self.cargar_datos()

            clima = self.vista.pedir_clima()
            viento = self.vista.pedir_viento()

            for fuente in self.fuentes:
                if isinstance(fuente, PanelSolar):
                    fuente.generar(clima=clima)
                elif isinstance(fuente, TurbinaEolica):
                    fuente.generar(velocidad_viento=viento)
                else:
                    fuente.generar()

            self.vista.mostrar_tablero(self.fuentes)

        except Exception as e:
            self.vista.mostrar_error(str(e))


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    ControladorRed().ejecutar()

        
