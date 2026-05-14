class RegistroAcademico():
    def __init__(self, nombre_alumno, nota_inicial):
        self.nombre = nombre_alumno
        self.__nota = nota_inicial
        self.cuenta_activa = True
        
    def get_nota(self): 
        return self.__nota
    
    def bloquear_cuenta(self): 
        self.cuenta_activa = False 
            
    def set_nota(self, nueva_nota):
        if not self.cuenta_activa:
            return -2 
        if 0 <= nueva_nota <= 100: 
            self.__nota = nueva_nota
            return 1
        return -1

# PROGRAMA PRINCIPAL 

alumna = RegistroAcademico("Laura", 85)

intentos_permitidos = 3 

while intentos_permitidos > 0: 
    nueva_nota = int(input("INGRESE LA NUEVA NOTA PARA"))
    resultado = alumna.set_nota(nueva_nota)
    
    if resultado == 1: 
        print("LA NOTA HA SIDO ACTUALIZADA")
        print("LA NOTA NUEVA ES:", alumna.set_nota(nueva_nota))
        break
    elif resultado == -1: 
        intentos_permitidos -=1 
        print("NOTA NO VALIDA. INTENTO RESTANTES: ", intentos_permitidos )
    elif resultado == -2: 
        print("ADVERTENCIA! CUENTA BLOQUEADA")
        break
    
if intentos_permitidos == 0:
    alumna.bloquear_cuenta()
    print("INTENTOS AGOTADOS. LA CUENTA HA SIDO BLOQUEADA")    
    
        
    
    
        
            
        
    
    
    
