
#PIEZA 1
filename = input("Escribe el nombre del archivo: ") 
with open(filename) as file:
    for line in file:
        ip = line.rstrip() #elimina los saltos de linea y nos da una variable linea por linea
        if ip.startswith("10."):
            print(f"{ip} es una IP privada.")
        elif ip.startswith("192.168."):
            print(f"{ip} es una IP privada.")
        elif ip.startswith("172."):
            partes = line.split(".") #divide todo el string según si tiene punto
            posicion = 1 #valor de la posicion =1 para buscar valores en el array
            numero_entero = int(partes[posicion]) #tomar el segundo valor del array y pasarlo de string a int para poder ser comparado
            if numero_entero >= 16 and numero_entero <= 31:
                print(f"{ip} es una IP privada.")
            else:
                print(f"{ip} es una IP publica.")
        else:
            print(f"{ip} es una IP publica.")
            # el : representa lo que viene a continuacion es un bloque indentado que pertenece
            #a esta linea
