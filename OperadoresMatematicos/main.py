""" 1. Un vendedor recibe un sueldo base más un 10% extra por
comisión de sus ventas, el vendedor desea saber cuánto
dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en
el mes tomando en cuenta su sueldo base y comisiones."""

sueldoBase = float(input("Escriba Salario Basico: "))
print(f"Sueldo Base: ${sueldoBase:,.0f}")
venta1 = float(input(" Primera Venta: "))
venta2 = float(input(" Segunda Venta: "))
venta3 = float(input(" Tercera Venta: "))
comision1 = venta1 * .10
comision2 = venta2 * .10
comision3 = venta3 * .10
totalcomision = comision1 + comision2 + comision3
print(f"Valor de Comision: ${totalcomision:,.0f} valor de comision y sueldo: ${sueldoBase + totalcomision:,.0f}")

""" 2. Una tienda ofrece un descuento del 15% sobre el total
de la compra y un cliente desea saber cuánto deberá
pagar finalmente por su compra. """

total = float(input("Digite el valor de la compra: "))
print(f"Valor de la Compra: ${total:,.0f}")
descuento = total * .15
NewTotal = total - descuento
print(f"Total descuento incluido ${NewTotal:,.0f}")

""" 3. Un alumno desea saber cuál será su calificación final en
la materia de Algoritmos. Dicha calificación se compone
de tres exámenes parciales. """
exam1 = float(input("Exam 1: "))
exam2 = float(input("Exam 2: "))
exam3 = float(input("Exam 3: "))
final = (exam1 + exam2 + exam3)/3
print(f"Nota Final: {final}")

""" 4. Un maestro desea saber qué porcentaje de hombres y que
porcentaje de mujeres hay en un grupo de estudiantes.  """

mujeres = int(input("Cuantas mujeres estudiantes hay el grupo?" ))
hombres = int(input("Cuantos hombres estudiantes hay el grupo?"))
total = mujeres + hombres
pMujeres = (mujeres * 100)/total
pHombres = (hombres * 100)/total
print(f"Porcentage de Mujeres? %{pMujeres} Porcentage de Hombres? %{pHombres}")