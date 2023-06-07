from Manejador import ManejaAutos
from Encoder import ObjectEncoder

from Usado import VehiculoUsado
from Nuevo import Vehiculonuevo



if __name__ == "__main__":
    jsonF = ObjectEncoder()   
    manejador = ManejaAutos() 
    
    diccionario=jsonF.leerJSONArchivo('vehiculos.json')
    vehiculos=jsonF.decodificarDiccionario(diccionario, manejador)
    
    print("1.  Insertar en posición")
    print("2.  Agregar vehiculo")
    print("3.  Dada una posición mostrar tipo de dato")
    print("4.  Dada la patente de usado, modifica")
    print("5.  mostrar todos los datos del más económico")
    print("6.. Mostrar todos")
    print("7.  Almacenar objetos en archivo")
    
    op = int(input("Ingrese opcion: "))
    while op != 0:
        if op == 1:
            #Agrega vehiculo en la posición determinada
            posicion = int(input("Ingrese posición en la lista para colocar el vehículo: "))
            eleccion = int(input("Ingrese un auto 1-viejo 2-nuevo: "))
            modelo = input("Ingrese modelo: ")
            cantPuertas = input("Ingrese cantPuertas: ")
            color = input("Ingrese color: ")
            precioVenta = input("Ingrese precio: ")
            marca = input("Ingrese marca: ")
            if eleccion == 1:
                patente = input("Ingrese patente: ") 
                anio = input("Ingrese anio: ")
                kilometraje = input("Ingrese kilometraje: ")
                vehiculo = VehiculoUsado(modelo,cantPuertas,color,precioVenta,marca,patente,anio,kilometraje)            
            elif eleccion == 2:
                version = input("Ingrese version: ")
                vehiculo = Vehiculonuevo(modelo,cantPuertas,color,precioVenta,marca,version)
            manejador.agregaAutoPorPos(posicion, vehiculo)
        elif op == 2:
            
            eleccion = int(input("Ingrese un auto 1-viejo 2-nuevo: "))
            modelo = input("Ingrese modelo: ")
            cantPuertas = input("Ingrese cantPuertas: ")
            color = input("Ingrese color: ")
            precioVenta = input("Ingrese precio: ")
            marca = input("Ingrese marca: ")
            if eleccion == 1:
                patente = input("Ingrese patente: ") 
                anio = input("Ingrese anio: ")
                kilometraje = input("Ingrese kilometraje: ")
                vehiculo = VehiculoUsado(modelo,cantPuertas,color,precioVenta,marca,patente,anio,kilometraje)
                manejador.agregarAuto(vehiculo)            
            elif eleccion == 2:
                version = input("Ingrese version: ")
                vehiculo = Vehiculonuevo(modelo,cantPuertas,color,precioVenta,marca,version)
                manejador.agregarAuto(vehiculo)
        elif op == 3:
            pos = int(input("Ingrese posicion a mostrar: "))
            manejador.MuestraPorPos(pos)
        elif op == 4:
            patente = input("Ingrese patente a buscar: ")
            manejador.BuscaPorPatente(patente)
        elif op == 5:
            manejador.BuscaMenor()
        elif op == 6:
            manejador.Muestra()
        elif op == 7:             
            
            d = manejador.toJSON()
            jsonF.guardarJSONArchivo(d, "vehiculos.json")
        else:
            print("Ingreso opcion incorrecta ")
            
        print("1.  Insertar en posición")
        print("2.  Agregar vehiculo")
        print("3.  Dada una posición mostrar tipo de dato")
        print("4.  Dada la patente de usado, modifica")
        print("5.  mostrar todos los datos del más económico")
        print("6.. Mostrar todos")
        print("7.  Almacenar objetos en archivo")
        
        op = int(input("Ingrese opcion: "))
            