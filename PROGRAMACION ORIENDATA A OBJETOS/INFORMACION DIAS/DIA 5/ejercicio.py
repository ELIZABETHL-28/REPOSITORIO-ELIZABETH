print("\nCENTRO DE CONTROL DE DRONES -SkyWatch-")

class DronVigilancia(): 
    def __init__(self, nombre_dron, modelo_dron):
        self.nombre = nombre_dron
        self.modelo = modelo_dron
        self.bateria = 100
        self.estado = "EN TIERRA"
        
    def despegue_dron(self): 
        if self.bateria < 25: 
            print("=ERROR= EL DRON NO PUEDE PATRULLAR SI AUN ESTA EN TIERRA")
        elif self.estado == "EN VUELO": 
            print("EL DRON AHORA ESTA EN EL AIRE")
        else: 
            self.estado = "EN VUELO"
            print("DESPEGUE EXISTOSO. EL DRON ESTA EN EL AIRE")
            
    def patrullaje_dron(self):
        if self.estado != "EN VUELO": 
            print("=ERROR= EN ESTOS MOMENTOS NO PUEDE PATRULLAR. ESTADO: EN TIERRA") 
            return
        self.bateria -= 30
        if self.bateria < 0: 
            self.bateria = 0
        print(f"PATRULLAJE COMPLETADO. CONSUMO: 30%. BATERIA RESTANTE: {self.bateria}%.")
        if self.bateria < 10: 
            self.estado = "EN TIERRA"
            print("BATERIA DELICADA. POR SU SEGURIDAD, EL DRON HA ATERRIZADO AUTOMATICAMENTE")
 
    def recargar_dron(self): 
        if self.estado != "EN TIERRA": 
            print("=ERROR= EL DRON NO PUEDE RECARGARSE MIENTRAS ESTA EN VUELO")
        else:
            self.bateria = 100
            print("RECARGA DE BATERIA COMPLETA")  
    
    def reporte(self):
        print("=" * 40) 
        print(f"- - - ESTADO ACTUAL: {self.nombre} [{self.modelo}] - - -")
        print(f"BATERIA: {self.bateria} %")
        print(f"ESTADO: {self.estado}")
        print("=" * 40)
        
      
print("- - - SISTEMA SKYWATCH - - -")
nombre = input("INGRESE EL NOMBRE DEL DRON: ")
modelo = input("INGRESE EL MODELO DEL DRON: ")

dron_uno = DronVigilancia(nombre, modelo)

while True:
    dron_uno.reporte()
    print("¿QUE FUNCION DESEA REALIZAR?")
    print("1. DESPEGAR\n2. PATRULLAR\n3. RECARGAR\n4. SALIR")

    opcion = input("SELECCIONE UNA OPCION: ")

    if opcion == "1":
        dron_uno.despegue_dron()
    elif opcion == "2":
        dron_uno.patrullaje_dron()
    elif opcion == "3":
        dron_uno.recargar_dron()
    elif opcion == "4":
        print("APAGANDO EL SISTEMA DEL DRON...")
        break
    else:
        print("OPCION INVALIDA. ¡INTENTE DE NUEVO!")            
    
    