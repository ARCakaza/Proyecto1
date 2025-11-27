def calculadora():#hago una funcion llamada calculadora 
    while True:#comienzo con el bucle lo que hace que menu de abajo se repita hasta que el usuario slecciona la opcion 5 que es la que acaba con el bucle 
        print("\n1. Sumar")#opciones a elejir osea el menu 
        print("2. Restar") 
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Elige una opcion: ")#aqui se va a guardar la opcion que se seleccione el usuario 
        
        if opcion == "5":#esta es la opcion para salir del while osea el bucle 
            break
            
        if opcion in ["1", "2", "3", "4"]:#verifica que la opcion que puse sea una de las opciones validas si no entonces se pasa al else de abajo 
            a = float(input("Primer numero: "))#pide el primer valor e cual se convierte en a 
            b = float(input("Segundo numero: "))#pide el segundo valor al cual se convierte en b
            
            if opcion == "1":#si es igual a 1 suma
                print(f"Resultado: {a + b}")
            elif opcion == "2":#si es igual a 2 resta
                print(f"Resultado: {a - b}")
            elif opcion == "3":#si es igual a 3 multiplica
                print(f"Resultado: {a * b}")
            elif opcion == "4":
                if b != 0:#si es diferente a 0 divide 
                    print(f"Resultado: {a / b}")
                else:#pero si este es igual a 0  no divide ya que no se puede dividir por 0
                    print(" Division por cero")
        else:#en dado caso de que por accidente se ponga un 6 o 7 como no estan dentro de las opciones va a dar opcion no valida
            print("Opcion invalida")

calculadora()#llamo a la funcion 
