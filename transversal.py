# Sección 0 10-v
import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios.")
        return

    bajos = []
    medios = []
    altos = []

    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            bajos.append((trabajador, sueldo))
        elif sueldo <= 2000000:
            medios.append((trabajador, sueldo))
        else:
            altos.append((trabajador, sueldo))

    print("\nSueldos menores a $800.000 TOTAL:", len(bajos))
    for trabajador, sueldo in bajos:
        print(f"{trabajador:<20} ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len(medios))
    for trabajador, sueldo in medios:
        print(f"{trabajador:<20} ${sueldo}")

    print("\nSueldos superiores a $2.000.000 TOTAL:", len(altos))
    for trabajador, sueldo in altos:
        print(f"{trabajador:<20} ${sueldo}")

    print(f"\nTOTAL SUELDOS: ${sum(sueldos)}")

def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios.")
        return

    print(f"Sueldo más alto: ${max(sueldos)}")
    print(f"Sueldo más bajo: ${min(sueldos)}")
    print(f"Promedio de sueldos: ${sum(sueldos) / len(sueldos):}")
    
    # calcular la media geometrica
    media_geometrica = math.pow(math.prod(sueldos), 1/len(sueldos))
    print(f"Media geométrica: ${media_geometrica:}")

def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios.")
        return

    print("\nReporte de Sueldos:")
    print(f"{'Nombre empleado':<20} {'Sueldo Base':<15} {'Descuento Salud':<20} {'Descuento AFP':<15} {'Sueldo Líquido':<15}")
    
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = int(sueldo * 0.07)
            descuento_afp = int(sueldo * 0.12)
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            
            print(f"{trabajador:<20} ${sueldo:<14} ${descuento_salud:<19} ${descuento_afp:<14} ${sueldo_liquido:<14}")
            writer.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("\nReporte exportado a 'reporte_sueldos.csv'")

# menu 
ejecutar_programa = True
while ejecutar_programa:
    print("\n--- Menú ---")
    print("1.Asignar sueldos aleatorios")
    print("2.Clasificar sueldos")
    print("3.Ver estadisticas")
    print("4.Reporte de sueldos")
    print("5.Salir del programa")

    opcion = input("Seleccione una opción: ")
    if opcion == "1": 
        asignar_sueldos_aleatorios()
    elif opcion == "2": 
        clasificar_sueldos()
    elif opcion == "3": 
        ver_estadisticas()
    elif opcion == "4": 
        reporte_sueldos()
    elif opcion == "5": 
        print("Gracias por usar el programa. ¡Hasta luego!")
        print("Finalizando programa...")
        print("Desarrollado por Cristóbal Cárdenas RUT 21.621.515-k ")
        ejecutar_programa = False
    else: 
        print("Opción no válida.")

    if ejecutar_programa:
        input("\nPresione Enter para continuar ")