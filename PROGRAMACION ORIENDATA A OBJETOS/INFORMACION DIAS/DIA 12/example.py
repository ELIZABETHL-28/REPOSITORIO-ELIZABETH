# # ejemplo 1
# class FiguraGeometrica(): 
#     def calcular_area(self):
#         print("NO SE COMO CALCULAR EL AREA. NO SOY UNA FIGURA")
        
# class Cuadrado(FiguraGeometrica):
#     def calcular_area(self):
#         print("Area = lado * lado")
        
# figura_fantasma = FiguraGeometrica()
# figura_fantasma.calcular_area()

# ========================================================================================

# # importancion obligatoria
# from abc import ABC, abstractmethod

# class Documento(ABC):
#     def __init__(self, titulo):
#         self.titulo = titulo
        
#     @abstractmethod
#     def exportar(self): 
#         pass #metodo que los hijos deben de cumplir
    
#     #metodo opcion si quiere o no tenerlo, los padres abstractor pueden tener metodos normales
#     def mostrar_titulo(self): 
#         print("DOCUMENTO: ", {self.titulo})
        
# class PDF(Documento):
#     def exportar(self):
#         print(f"exportando {self.titulo} a pdf")
        
# class WORD(Documento):
#     def exportar(self):
#         print(f"exportando {self.titulo} a word")
        
# class EXCEL(Documento):
#     def exportar(self):
#         print(f"exportando {self.titulo} a excel")
    
#     def guardar(self): 
#         print(f"guardando {self.titulo} en excel")
        
# try: 
#     doc_invalido = Documento ("Mi  archivo")
# except: 
#     print("-BLOQUEO DE SEGURIDAD-")
    
    
# pdf_doc = PDF("REPORTE DE VENTAS")
# pdf_doc.mostrar_titulo()
# pdf_doc.exportar()

# excel_doc = EXCEL("ESTERNOCLEIDOMASTOIDEO")
# excel_doc.mostrar_titulo()
# excel_doc.exportar()


#========================================================================================

# from abc import ABC, abstractmethod

# class VehiculoComercial(ABC): 
#     @property
#     @abstractmethod
#     def tarifa_km(self): 
#         pass 
    
#     def calcular_viaje(self, kilometro): 
#         total = kilometro * self.tarifa_km
#         print("COSTO DEL VIAJE", {total})
        
# class Taxi(VehiculoComercial):
#     @property
#     def tarifa_km(self):
#         return 500
    
# mi_taxi = Taxi()
# mi_taxi.calcular_viaje(10) # 10*500 = 5000







































