def costo_pieza():
    total_gramos = int(input("¿Cuantos gramos pesa la  pieza?: "))
    resultado = total_gramos * 2.5 * 2
    
    print(f"El costo ideal de la pieza es: ${resultado}")

def costo_filamento(filamento):
    total = filamento / 1000
    return print(f"El gramo de filamento va a costar: ${total}")

def main():
    filamento = int(input("Cuanto costo el filamento ($$$)?: "))
    costo_filamento(filamento)
    

if __name__ == "__main__":
    main()

