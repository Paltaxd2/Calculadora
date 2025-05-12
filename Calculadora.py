while True:
    try:
        num1 = int(input("Ingrese numero 1: "))
        num2 = int(input("Ingrese numero 2: "))
        menu = '''
               1. Sumar
               2. Restar
               3. Dividir
               4. Multiplicar
               5. Salir
           '''
        
        print(menu)
        op = int(input("Eliga un Numero por favor: "))

        if op == 1:
            print("La suma es: ",num1+num2)
            continue;
        elif op == 2:
            print("La Resta es: ",num1-num2)
            continue;
        elif op == 3:
            print("La Division es: ",num1/num2)
            continue;
        elif op == 4:
            print("La Multiplicacion es: ",num1*num2)
            continue;
        elif op == 5:
            print("Gracias por usar la calculadora, adios")
            break;
        else:
            print("Debe ser un Numero entre 1 y 5")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except ValueError:
        print("Debe ser un valor Numerico")
    except Exception as error:
        print("Hay un error: ",error)