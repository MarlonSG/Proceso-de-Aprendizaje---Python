def obtener_informacion ():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    edad_empleado = int(input("Ingrese la edad del empleado: "))
    salario_empleado = float(input("Ingrese la salario del empleado: "))
    es_jefe_departamento = input("¿Es jefe de departamento? (Si/No): ")
    es_jefe_departamento = es_jefe_departamento.lower() == "si"
    return nombre_empleado,apellido_empleado,edad_empleado,salario_empleado,es_jefe_departamento

nombre_empleado,apellido_empleado,edad_empleado,salario_empleado,es_jefe_departamento = obtener_informacion()

print("*** Sistema de Empleados ***")


print("\nDatos del Empleado:")
print(f"Nombre: {nombre_empleado}")
print(f"Apellido: {apellido_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado:.2f}")
print(f"¿Es jefe de departamento?: {es_jefe_departamento}")
