# class Motor(): 
#     def __init__(self, caballoz_fuerza):
#         self.caballos = caballoz_fuerza
#         self.encendido = False 
        
#     def arrancar(self): 
#         self.encendido = True
#         print("ENCENDIENDO EL MOTOR")
        
# class Auto():
#     #HACEMOS DOS PARAMETROS Y HACEMOS OTRO PARA INSTANCIAR NUESTRO OBJETO
#     def __init__(self, marca, modelo, potencia_motor):
#         self.marca = marca
#         self.modelo = modelo 
        
#         self.corazon_mecanico = Motor(potencia_motor) # estamos instanciando dentro de nuestro constructor 
        
#     def encender_auto(self):
#         print("GIRANDO LA LLAVE PARA ENCENDER...")

#         #RECORDAR QUE EL CORAZONMECANICO ES UN OBJETO AHORA
#         self.corazon_mecanico.arrancar()
        
# mi_carro = Auto("Toyota", "Corola", 200)
# mi_carro.encender_auto()
# ======================================================================

# class Procesador():
#     def __init__(self, modelo):
#         self.modelo = modelo
    
# class TarjetaVideo():
#     def __init__(self, memoria_gb):
#         self.memoria = memoria_gb
        
# class Computadora():
#     def __init__(self, cpu_externo, gpu_externa):
#         self.cpu = cpu_externo
#         self.gpu = gpu_externa
        
#     def mostrar_especificaciones(self): 
#         print("ESPESIFICACIONES DEL EQUIPO: ")
#         #ACCEDEMOS A LOS ATRIBUTOS DE LAS PIEZAS INYECTADAS 
        
#         print("PROCESADOR: ", {self.cpu.modelo})
#         print("GRAFICOS: ", {self.gpu.memoria}, "GB de video")

# # fabricar las piezas por separado 
# intel_i9 = Procesador("intel Core i9 14900K")
# nvidia_x = TarjetaVideo(24)
# pc_gamer = Computadora(intel_i9, nvidia_x)
# pc_gamer.mostrar_especificaciones()
    
# ======================================================================

class Estudiantes(): 
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        
class Curso():
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        
        self.lista_matriculados = []
    
    def matricular(self, nuevo_estudiante):
        self.lista_matriculados.append(nuevo_estudiante)
        print("SISTEMA: ", {nuevo_estudiante.nombre}, "MATRICULADO CON EXITO")
        
    def pasar_lista(self): 
        for alumno in self.lista_matriculados:
            print(f"- {alumno.carnet}: {alumno.nombre}")
            
alumno1 = Estudiantes("FERS", "AB1")
alumno2 = Estudiantes("ANDREW", "AB2")
curso_poo = Curso("POO")
curso_poo.matricular(alumno1)
curso_poo.matricular(alumno2)
#aca lo edite para poder aguardarlo
curso_poo.pasar_lista()
curso_poo.lista_matriculados[0].nombre = "FERS LIZ"
curso_poo.pasar_lista()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        