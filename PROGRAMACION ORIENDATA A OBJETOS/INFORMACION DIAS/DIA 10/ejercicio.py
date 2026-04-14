class PersonajeBase(): 
    def caminar(self): 
        print("EL PERSONAJE ESTA AVANZANDO POR EL MAPA")
        
    def descansar(self): 
        print("EL PERSONAJE ESTA RECUPERANDO ENERGIA")
        
class Mago(PersonajeBase): 
    def lanzar_hechizo(self): 
        print("EL MAGO LANZA UNA BOLA DE FUEGO!")
        
class Guerrero(PersonajeBase): 
    def bloquear_ataque(self): 
        print("EL GUERRERO LEVANTA SU ESCUDO DE METAL!")
        
mi_mago = PersonajeBase()
mi_guerrero = PersonajeBase()

print("ACCIONES DEL MAGO")
mi_mago.caminar()
mi_mago.descansar()
mi_mago.lanzar_hechizo

print("ACCIONES DEL GUERRERO")
mi_guerrero.caminar()
mi_guerrero.descansar()
mi_guerrero.bloquear_ataque

# ===================================================================================================




    
    
