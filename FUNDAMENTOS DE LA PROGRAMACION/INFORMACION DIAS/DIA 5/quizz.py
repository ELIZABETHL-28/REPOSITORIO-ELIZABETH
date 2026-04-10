# Un centro tecnológico tiene un laboratorio de impresión 3D al 
# que solo pueden ingresar estudiantes autorizados.

# Además, una vez dentro, el estudiante puede comprar minutos 
# extra de uso de impresora mientras tenga saldo suficiente.
# El programa debe verificar primero si el estudiante puede ingresar al laboratorio y luego permitirle
# comprar minutos extra de uso.

print ("\t--- EVALUACION-QUIZZ ---")
print ("--- IMPRESION 3D CON COMPRA DE MINUTOS ---")

estudiante = input("NOMBRE DEL ESTUDIANTE: ")
edad = int(input("EDAD DEL ESTUDIANTE: "))
autorizacion = input("TIENE AUTORIZACION DEL PROFESOR (si/no): ")
saldo = float(input("CUAL ES EL SALDO DISPONIBLE: "))
costo =float(input("COSTO DE CADA PAQUETE DE MINUTOS EXTRA: "))


if edad >= 15 and autorizacion == "si": 
        print("\n-------------------------------")
        print("EL ESTUDIANTE", estudiante, "PUEDE ENTRAR AL LABORATORIO")  
        print("-------------------------------")

        paquetes = 0 

        while saldo >= costo: 
          answer = input("DESEA COMPRAR UN PAQUETE? ")
          print("-------------------------------")

          if answer == "si": 
                saldo -= costo
                paquetes += 1
                print ("COMPRA REALIZADA!")
                print("-------------------------------")
          else: 
                print("NO SE PUEDO REALIZAR")

        print("\n\tDATOS DEL ESTUDIANTE")
        print("NOMBRE: ", estudiante)
        print("PAQUETES COMPRADOS: ", paquetes)
        print ("SALDO RESTANTE: ", saldo)
        print("-------------------------------")

else: 
      print("===EL ESTUDIANTE NO PUEDE INGRESAR===")





