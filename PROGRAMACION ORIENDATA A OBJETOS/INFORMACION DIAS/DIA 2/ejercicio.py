class CajaRegistradora():
    def cobrar_producto(self):
        precio = float(input("INGRESE EL PRECIO DEL PRODUCTO: " ))
        self.dinero_acumulado += precio
        print(f"COBRO EXITOSO. LLEVAMOS ACUMULADO: {self.dinero_acumulado}")

    def imprimir_cierre_turno(self): 
        print(f"CAJERO ENCARGADO: {self.cajero_asignado}")
        print(f"TOTAL RECAUDADO EN EL DIA: {self.dinero_acumulado}")

caja_express = CajaRegistradora()

caja_express.cajero_asignado = "Fernanda"
caja_express.dinero_acumulado = 0 

caja_express.cobrar_producto()
caja_express.cobrar_producto()

caja_express.imprimir_cierre_turno()