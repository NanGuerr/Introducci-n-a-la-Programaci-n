<p align="center">
  <img src="https://raw.githubusercontent.com/NanGuerr/Introducci-n-a-la-Programaci-n/refs/heads/main/Parciales/assets/Parcial%20Pacientes.png" width="100%">
</p>

```python

"""Desarrollar un programa en Python que permita procesar y analizar los datos de ocupación de un complejo cinematográfico
compuesto por exactamente 15 salas.
1. Entrada de Datos y Validaciones
El programa debe solicitar para cada una de las 15 salas los siguientes datos, aplicando sus respectivas validaciones mediante
bucles de re-intento:
Número de sala: Debe ser un número entero mayor o igual a 0.
Cantidad total de butacas: Debe ser un número entero mayor o igual a 1.
Cantidad de butacas vendidas: Debe ser un número entero mayor o igual a 0.
2. Procesamiento por Sala (Durante la carga)
A medida que se ingresan los datos de cada sala, el sistema debe:
Calcular y mostrar inmediatamente el porcentaje de ocupación (butacas vendidas sobre el total de capacidad) de esa sala,
formateado con un decimal. Evaluar e identificar si la sala se encuentra completa (100% de éxito en ventas).
3. Resultados Finales
Una vez finalizada la carga de las 15 salas, el programa deberá emitir un reporte final con los siguientes indicadores:
El número de la sala que registró la menor cantidad de entradas vendidas.
El número de la sala que registró la mayor cantidad de entradas vendidas.
La cantidad total de salas que se llenaron por completo. En caso de que ninguna haya alcanzado el 100% de su capacidad,
se debe mostrar un mensaje aclaratorio. El promedio general de ocupación de todo el cine, expresado en porcentaje
(total de butacas vendidas en el complejo sobre el total de butacas disponibles)."""

salas_comp = 0
total_butacas = 0
total_vendidas = 0
sala_menor = 0

# Procesamos las 15 salas en un solo bucle
for i in range(15):
    num_sala = int(input("Ingrese el numero de sala: \t"))
    while num_sala < 0:
        num_sala = int(input("Error. Ingrese el numero de sala: \t"))
        
    cant_butacas = int(input("Ingrese la cantidad total de butacas: \t"))
    while cant_butacas < 1:
        cant_butacas = int(input("Error. Ingrese la cantidad total de butacas: \t"))
        
    cant_vendidas = int(input("Ingrese la cantidad de butacas vendidas: \t"))
    # BONUS: Validamos que las vendidas no superen a las butacas totales de la sala
    while cant_vendidas < 0 or cant_vendidas > cant_butacas:
        cant_vendidas = int(input("Error. Cantidad inválida. Ingrese las butacas vendidas: \t"))
        
    # Acumuladores
    total_butacas += cant_butacas
    total_vendidas += cant_vendidas
        
    if i == 0:
        mayorcant_vendidas = cant_vendidas
        sala_mayor = num_sala
        menorcant_vendidas = cant_vendidas
        sala_menor = num_sala  
        
    # Buscar mínimo
    if cant_vendidas < menorcant_vendidas:
        menorcant_vendidas = cant_vendidas
        sala_menor = num_sala
       
    # Buscar máximo
    if cant_vendidas > mayorcant_vendidas:
        mayorcant_vendidas = cant_vendidas
        sala_mayor = num_sala
        
    # Calcular porcentaje de la sala
    porce_vendidas = (cant_vendidas * 100) / cant_butacas
    print(f"El porcentaje de butacas vendidas de la sala es: {porce_vendidas:.1f}%\n")
        
    # Verificar si la sala está completa
    if cant_butacas == cant_vendidas:
        salas_comp += 1

# --- Bloque final de reportes (Fuera del bucle) ---
print("Finalizo el ingreso de datos\n")        
print("--------------Resultados finales--------------------------\n")
print(f"El numero de sala con menor cantidad de butacas vendidas es: {sala_menor}\n")

if salas_comp == 0:
    print("En ninguna sala se vendio el total de butacas.\n")
else:
    print(f"En {salas_comp} sala(s) se vendieron el total de butacas.\n")

promedio_vendidas = (total_vendidas * 100) / total_butacas
print(f"El promedio de butacas vendidas de todo el cine es: {promedio_vendidas:.1f}%\n")
print(f"El numero de sala con mayor cantidad de butacas vendidas es: {sala_mayor}\n")
