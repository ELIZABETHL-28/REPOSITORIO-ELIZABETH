
# class Animal: 
#     def comer (self):
#         print("EL ANIMAL ESTA COMIENDO")

# # 2# EL HIJO
# class Perro(Animal):
#     pass 

# # 3# USO
# mi_mascota = Perro()
# mi_mascota.comer()
        
# # = =============================================================================

# class Vehiculo(): 
#     def encender_motor (self):
#         print("EL MOTOR SE HA ENCENDIDO")

#     def apagar_motor(self):
#         print("EL MOTOR SE HA ENCENDIDO")

# # SUBCLASE (HIJA 1)
# class Auto(Vehiculo):
#     def encender_aire(self):
#         print("AIRE ACONDICIONADO ENCENDIDO")

# class Moto(Vehiculo):
#     def hacer_acrobacia(self):
#         print("LEVANTANDO LA RUEDA DELANTERA")

# carro = Auto()
# moto = Moto()

# print("ACCIONES DEL AUTO")
# carro.encender_motor()
# carro.encender_aire()

# print("ACCIONES DE LA MOTO")
# moto.encender_motor
# moto.hacer_acrobacia 

# # = =============================================================================
# class Padre():
#     def __init__(self, apellido):
#         self.apellido = apellido
        
# class Hijo(Padre): 
#     def __init__(self, nombre): # peligro! eso borra el __init__ del Padre
#         self.nombre = nombre
        
# chico = Hijo("Carlos")
# print(chico.apellido) # ERROR, el hijo nunca recibio el apellido porque su init aplasto al del padre
# = =============================================================================
# class Persona: 
#     def __init__(self, nombre):
#         self.nombre = nombre # SI LO PONEMOS PRIVADO, SE PUEDE ACCEDER DESDE LA CLASE HIJA PERO NO DESDE FUERA DE LA CLASE 
        
# class Estudiante(Persona): 
#     def __init__(self, nombre_ingresado, nota_ingresada): 
#         super().__init__(nombre_ingresado)

#         self.nota = nota_ingresada
        
#     def mostrar_info(self): 
#         print(f"HOLA, MI NOMBRE ES: {self.nombre} y mi nota es: {self.nota}")

# estu1 = Estudiante("Fer", 9.5)
# estu1.mostrar_info()

# print(estu1.__nombre) # se puede acceder pero no es recomdable porque es un atributo privado 

# # = =============================================================================



# # ================================
# # CLASE BASE: Vehiculo
# # ================================

# class Vehiculo:
#     """
#     Clase base que representa un vehículo genérico.
#     Aquí se definen los atributos y comportamientos comunes
#     a todos los vehículos del sistema.
#     """

#     def __init__(self, placa, marca, modelo, kilometraje=0):
#         # La placa identifica al vehículo (ej: P123ABC)
#         self.placa = placa

#         # Marca del vehículo (Toyota, Mazda, etc.)
#         self.marca = marca

#         # Modelo del vehículo (Corolla, Civic, etc.)
#         self.modelo = modelo

#         # Kilometraje actual del vehículo
#         self.kilometraje = kilometraje

#         # Indica si el vehículo está disponible para alquilar
#         self.disponible = True

#     def mostrar_info(self):
#         """
#         Devuelve información básica del vehículo en texto.
#         """
#         return f"Placa: {self.placa} | {self.marca} {self.modelo}"

#     def actualizar_kilometraje(self, nuevo_km):
#         """
#         Actualiza el kilometraje del vehículo.
#         Se evita el fraude comprobando que el nuevo
#         kilometraje no sea menor al actual.
#         """

#         # Si el nuevo kilometraje es menor al guardado
#         if nuevo_km < self.kilometraje:
#             print("Error: No se puede reducir el kilometraje. Posible fraude.")
#         else:
#             # Si es válido, se actualiza
#             self.kilometraje = nuevo_km
#             print("Kilometraje actualizado correctamente.")


# # ================================
# # CLASE HIJA: Auto
# # ================================

# class Auto(Vehiculo):
#     """
#     Clase Auto que hereda de Vehiculo.
#     Agrega lógica específica para el alquiler.
#     """
    
#     # Variable de clase: tarifa compartida por TODOS los autos
#     tarifa_base_diaria = 50

#     def __init__(self, placa, marca, modelo, kilometraje=0):
#         """
#         Constructor de la clase Auto.
#         Usa super() para llamar al constructor de Vehiculo.
#         """

#         # super() permite reutilizar el código del padre
#         super().__init__(placa, marca, modelo, kilometraje)

#     def alquilar(self, dias):
#         """
#         Alquila el vehículo por una cantidad de días.
#         Calcula automáticamente el costo.
#         """

#         # Si el auto no está disponible, no se puede alquilar
#         if not self.disponible:
#             print(" El vehículo no está disponible para alquiler.")
#             return 0

#         # Se marca el auto como no disponible
#         self.disponible = False

#         # Cálculo automático del costo del alquiler
#         costo_total = dias * Auto.tarifa_base_diaria

#         return costo_total

#     def devolver(self, nuevo_kilometraje):
#         """
#         Devuelve el vehículo, actualiza el kilometraje
#         y lo marca como disponible nuevamente.
#         """

#         # Se valida y actualiza el kilometraje
#         self.actualizar_kilometraje(nuevo_kilometraje)

#         # El auto queda disponible otra vez
#         self.disponible = True


# # ================================
# # GESTIÓN DE FLOTA
# # ================================

# class Flota:
#     """
#     Clase que gestiona todos los vehículos de la empresa.
#     Permite registrar autos y contar disponibles.
#     """

#     def __init__(self):
#         # Lista donde se almacenan los vehículos registrados
#         self.vehiculos = []

#     def registrar_vehiculo(self, vehiculo):
#         """
#         Agrega un vehículo a la flota.
#         """
#         self.vehiculos.append(vehiculo)

#     def contar_disponibles(self):
#         """
#         Cuenta cuántos vehículos están disponibles.
#         """
#         return sum(1 for v in self.vehiculos if v.disponible)

#     def mostrar_flotta(self):
#         """
#         Muestra información de todos los vehículos.
#         """
#         for v in self.vehiculos:
#             estado = "Disponible" if v.disponible else "Alquilado"
#             print(v.mostrar_info(), "| Estado:", estado)


# # ================================
# # EJEMPLO DE USO DEL SISTEMA
# # ================================

# # Se crea la flota de la empresa
# flota_empresa = Flota()

# # Se crean autos
# auto1 = Auto("P123ABC", "Toyota", "Corolla", 10000)
# auto2 = Auto("P456DEF", "Honda", "Civic", 20000)

# # Se registran en la flota
# flota_empresa.registrar_vehiculo(auto1)
# flota_empresa.registrar_vehiculo(auto2)

# # Se muestra la flota
# print("\n Flota actual:")
# flota_empresa.mostrar_flotta()

# # Alquilar un vehículo
# print("\nAlquiler del auto 1:")
# costo = auto1.alquilar(3)
# print(f"Costo del alquiler: Q{costo}")

# # La gerencia cambia la tarifa diaria
# Auto.tarifa_base_diaria = 60
# print("\n Tarifa diaria actualizada por gerencia.")

# # Devolver el vehículo
# print("\n Devolución del auto 1:")
# auto1.devolver(10300)

# # Intento de fraude
# print("\nIntento de fraude:")
# auto1.actualizar_kilometraje(9000)

# # Contar disponibles
# print("\n Vehículos disponibles:", flota_empresa.contar_disponibles())


# ====================================================================================
# class Empleado: 
#     def __init__(self, nombre, salario):
#         self.nombre = nombre
#         self.salario = salario
        
# class CalculadoraFinanciera():
# ====================================================================================

    
# class Persona_Mayor(): 
#     def saludar(self):
#         print("BUENAS TARDES ESTIMADO, COMO SE ENCUENTRE EL DIA DE HOY. UN PLACER SALUDARLO.")
        
# class Adolecente(Persona_Mayor):
#     def saludar(self): 
#         print("HOLA, TODO BIEN")
        
# senor = Persona_Mayor()
# pelado = Adolecente()

# senor.saludar()
# pelado.saludar()

# ====================================================================================

# class Animal (): 
#     def __init__(self, nombre):
#         self.nombre = nombre
        
#     def __str__(self): # ESE ES LA FUNCION QUE SE USA EN PYTHON AUTOMATICAMENTE POR
#         # COMO QUEREMOS QUE SE PRESENTE TIPO CADENA DE TEXTO CUANDO LE DAMOS UN PRINT
#         return f"Animal: {self.nombre}"
        
#     def hacer_sonido(self):
#         print(f"{self.nombre} hace un sonido generico")
        
# class Perro(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} | El perro hace: guau, guauuuu")
        
# class Gato(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} | El gato hace: miau, miauu")

# class Pato(Animal):
#     def hacer_sonido(self):
#         print(f"{self.nombre} | El pato hace: cuac, cuaaaaac")
        
# animal1 = Perro("Pochiberto")
# animal2 = Perro("Porfirio")
# animal3 = Perro("Pancracio")

# lista_granja = [animal1, animal2]
# lista_granja.append(animal3)

# animal_desconocido = Animal("Extraterrestre")

# lista_granja.append(animal_desconocido)

# print(animal2)

# for animal in lista_granja: 
#     animal.hacer_sonido()  
# # el polimorfismo es misma orden diferentes maneras
# print("= = = = = = = = = = = = = = = = = = = = = =")

# for animal in lista_granja: 
#     print(animal) # por medio del str 
# ====================================================================================

class EmpleadoBase():
    def iniciar_rutina(self):
        print("1. llego a la oficina a las 8")
        print("2. Reviso mis gmails")
        print("3. planifico mi dia")
        
class Programador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
        
        print("4. escribo codigo y resuelvo problemas tecnicos")
        
class Desarrollador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
        print("Y YO ME QUEDO EN CASA A DESARROLLAR PROGRAMAS ")
        
trabajador1 = Programador()
trabajador1.iniciar_rutina()

trabajador2 = Desarrollador()
trabajador2.iniciar_rutina()

# SI EXISTE UN RETURNO SEGUIDO DE UN SUPER, TRAE EL VALOR QUE TENEMOS QUE EL CONTTRUCTOR Y RETORNA EL VALOR


































 