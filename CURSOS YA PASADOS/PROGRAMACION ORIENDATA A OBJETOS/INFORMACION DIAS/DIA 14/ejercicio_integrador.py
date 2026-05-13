# BLOQUE 1 (HERENCIA Y ABSTRACCION)
from abc import ABC, abstractmethod
class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre 
        self.especialidad = especialidad
    
    @abstractmethod
    def realizar_labor(self): 
        pass 
    
class Doctor(PersonalMedico):
    def realizar_labor(self):
        print("REALIZANDO UN DIAGSNOSTICO ESPECIALIZADO")
        
    def atender_paciente(self, objeto_paciente):
        self.realizar_labor()

        anotacion = input("INGRESE NOTA DESCRIPTIVA PARA EL HISTORIAL:")
        objeto_paciente.historial_cli.agregar_observaciones(anotacion)
        
        while True: 
            try: 
                dosis_medicina = int(input("INGRESE DOSIS DE RECUPERACION: "))
                if dosis_medicina <= 50:
                    objeto_paciente.salud += dosis_medicina 
                    print(f"TRATAMIENTO EXITOSO! LA SALUD DE {objeto_paciente.nombre} HA SUBIDO A {objeto_paciente.salud}")               
                    break
                else: 
                    print("=ADVERTENCIA= LA DOSIS DEBE DE ESTAR ENTRE 1-50")
            except ValueError:
                print("[ERROR]: INGRESE UNICAMENTE VALORES NUMERICOS PARA LA DOSIS")
                
class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] - EL ENFERMERO {self.nombre} ESTA APLICANDO CUIDADO Y REVISANDO SIGNOS VITALES.")   
             
class HistorialClinico():
    def __init__(self):
        self.observaciones = []
    
    def agregar_observaciones(self, texto): 
        self.observaciones.append(texto)
    
    def mostrar_registros(self):
        print("NOTAS REGISTRADAS: ")
        for notas in self.observaciones: 
            print(notas)
            
class Paciente():
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad 
        self.salud = 50
        self.historial_cli = HistorialClinico()
        
    def condicion(self): 
        if self.salud < 20:
            return "Crítico"
        else: 
            return "Estable"
        
class Hospital():
    def __init__(self):
        self.pacientes = []
        self.personal = []
        
    def registrar_pacientes(self):
        nombre = input("NOMBRE DEL PACIENTE: ")
        while True: 
            try: 
                edad = int(input("EDAD PACIENTE: "))
                break
            except ValueError:
                print("[ERROR] INGRESE NUEVAMENTE (SOLO NUMEROS)")
                
        paciente = Paciente(nombre, edad)
        self.pacientes.append(paciente)
        print("REGISTRADO CORRECTAMENTE")
        
    def contratacion(self):
        print("1 - DOCTOR")
        print("2 - ENFERMERO")
        
        seleccionar = input("SELECCION PERSONAL A CONTRATAR: ")
        
        nombre = input("NOMBRE: ") 
        especialidad = input("ESPECIALIDAD: ")
        
        if seleccionar == "1":
            self.personal.append(Doctor(nombre, especialidad))
        elif seleccionar == "2":
            self.personal.append(Enfermero(nombre, especialidad))
        else:
            print("[ERROR]: Opción inválida")
            
    def mostrar_pacientes(self):
        print("\n-- Pacientes Disponibles --")
        for no_paciente in range(len(self.pacientes)):
            usuario = self.pacientes[no_paciente]
            print(f"{no_paciente}. {usuario.nombre} ({usuario.edad})")   
            
            
    def mostrar_personal(self):
        print("\n-- Personal Disponible --")
        for no_personal in range(len(self.personal)):
            usuario = self.personal[no_personal]
            print(f"{no_personal}. {usuario.nombre} ({usuario.especialidad})")
            
    def realizar_consulta(self):
        if not self.personal or not self.pacientes:
            print("No hay personal o pacientes disponibles.")
            return

        self.mostrar_personal()
        try:
            usuario_medico = int(input("Elija el médico: "))
    
            if usuario_medico < 0 or usuario_medico >= len(self.personal):
                print("[ERROR]: Número fuera de rango.")
                return

            medico = self.personal[usuario_medico]

        except ValueError:
            print("[ERROR]: Debe ingresar un número.")
            return
        
        self.mostrar_pacientes()
        try:
            usuario_paciente = int(input("Elija el paciente: "))
            paciente = self.pacientes[usuario_paciente]
        except ValueError:
            print("[ERROR]: Selección inválida.")
            return

        if isinstance(medico, Doctor):
            medico.atender_paciente(paciente)
        else:
            medico.realizar_labor()

    def reporte(self):
        print("\n=== REPORTE | PACIENTES ===")
        for usuario in self.pacientes:
            print(f"PACIENTE: {usuario.nombre} | EDAD: {usuario.edad} | SALUD: {usuario.salud}% | ESTADO: {usuario.condicion()}")
        usuario.historial_cli.mostrar_registros()
        
def menu():
    hospital = Hospital()

    while True:
        print("\n>>> SISTEMA HOSPITALARIO <<<")        
        print("\t\n>>> VIDA-SANA <<<")
        print("1 - Registrar Paciente")
        print("2 - Contratar Personal")
        print("3 - Realizar Consulta Médica")
        print("4 - Ver Reporte de Pabellón")
        print("5 - Salir")

        opcion = input("SELECCIONE UNA OPCION: ")

        if opcion == "1":
            hospital.registrar_pacientes()
        elif opcion == "2":
            hospital.contratacion()
        elif opcion == "3":
            hospital.realizar_consulta()
        elif opcion == "4":
            hospital.reporte()
        elif opcion == "5":
            print("SALIENDO DEL SISTEMA VIDA-SANA...")
            break
        else:
            print("[ERROR]: OPCION INVALIDA")

menu()
        
        
        
        