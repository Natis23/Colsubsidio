numIdentificación = 12345678 
nombre = 'Jhon'
apellidos = 'Doe'
dirección = '123 main st, Bogota' 
teléfono = 3005201234
edad = int(input("Que Edad Tiene? "))
estadoCivil = input("Estado Civil?")
numeroHijos = int(input("Hijos?"))
estaturaCentimetros = 1.80 
fechaContratacion = '23/Julio/2020' 
sueldoBasico = float(input("Escriba su sueldo? "))
diasLaborados = int(input("Días laborados al mes? "))

""" Dando continuidad con la primera entrega del proyecto, en esta oportunidad 
el estudiante debe realizar las siguientes validaciones utilizando la sentencia 
condicional IF. """

""" 1. Si el empleado es mayor de 55 años disfrutará de un bono de prepensión 
correspondiente al 5% de su sueldo básico. """
if edad >= 55:
    bono = sueldoBasico * .05
    print (f"Bono de: ${bono:,.0f}")

""" 2. Si el empleado es casado y tiene hijos se le otorgará un paseo cada 
diciembre """
if estadoCivil == "casado" and numeroHijos > 0:
    print("Paseo de Diciembre")

""" 3. Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 
2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 
tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos 
no habrá comisión. """
if sueldoBasico >= 1000000 and sueldoBasico <= 1500000:
    comision1 = sueldoBasico * .02
    print("comisión del 2%")

elif sueldoBasico >= 1500001 and sueldoBasico <= 2000000:
    comision2 = sueldoBasico * .05
    print("comisión del 5%")

else:
    print("no habrá comisión")

""" 4. Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 
1000000 tendrá derecho a un bono de alimentación. """

if diasLaborados > 20 and sueldoBasico < 1000000:
    print("tendrá derecho a un bono de alimentación")