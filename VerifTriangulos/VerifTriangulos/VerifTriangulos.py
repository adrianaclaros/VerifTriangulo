def determinar_tipo_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b == lado_c:
        return "EL TRIANGULO ES EQUILATERO"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "EL TRIANGULO ES ISOSCELES"
    else:
        return "EL TRIANGULO ES ESCALENO"

def verificar_triangulo():
    print("Ingrese los valores de los lados del triangulo:")
    try:
        lado_a = float(input("INGRESE EL LADO A: "))
        lado_b = float(input("INGRESE EL LADO B: "))
        lado_c = float(input("INGRESE EL LADO C: "))
        
        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            print("Los lados de un triangulo deben ser mayores a 0.")
            return
        
        # Verificar si los lados forman un triangulo valido
        if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
            tipo_triangulo = determinar_tipo_triangulo(lado_a, lado_b, lado_c)
            print(tipo_triangulo)
        else:
            print("Los valores ingresados no forman un triangulo valido.")
    except ValueError:
        print("Por favor, ingrese valores numericos validos.")

if __name__ == "__main__":
    verificar_triangulo()
