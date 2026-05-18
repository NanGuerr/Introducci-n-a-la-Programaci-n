<p align="center">
  <img src="https://raw.githubusercontent.com/NanGuerr/Introducci-n-a-la-Programaci-n/refs/heads/main/Parciales/assets/Parcial%20Pacientes.png" width="100%">
</p>

```python
"""Consigna: Sistema de Gestión de Ventas Mayoristas de Calzado
Objetivo:

Desarrollar un programa en Python para registrar y analizar las ventas mayoristas de una fábrica de calzado que comercializa dos 
productos: Sandalias (precio unitario: $2.500) y Alpargatas (precio unitario: $3.500).

1. Entrada de Datos y Reglas de Negocio
El sistema procesará facturas de venta de forma consecutiva. El ingreso de datos finalizará cuando el usuario introduzca el número
de factura 0.

Por cada factura se deben solicitar y validar los siguientes datos:
Número de factura: Debe ser un valor entero positivo (> 0). Si es negativo, se debe exigir un reingreso. El valor 0 se reserva exclusiva
mente para terminar la carga.

Cantidad comprada: Dado que se trata de un canal mayorista, la cantidad de unidades por factura debe ser estrictamente mayor a 50. 
De lo contrario, se mostrará un error y se pedirá una nueva cantidad.

Tipo de producto: Se debe ingresar una letra para identificar el artículo vendido (único tipo de producto por factura): 
'S' para Sandalias o 'A' para Alpargatas. El programa no debe distinguir entre mayúsculas y minúsculas y debe rechazar cualquier 
otra letra.

2. Procesamiento de Datos
A partir de las facturas válidas procesadas, el sistema debe llevar el control de:
La cantidad total de unidades vendidas acumuladas para cada producto.
Cuál es la factura que registró la mayor cantidad de unidades compradas (guardando tanto el número de factura como dicha cantidad máxima).

3. Reportes Finales (Resultados)
Al finalizar la carga de datos (ingreso de factura 0), y siempre que se haya procesado al menos una venta, el programa deberá calcular
y mostrar:
El monto total facturado (en pesos) correspondiente únicamente a la venta de Sandalias.
El porcentaje que representa la cantidad de Alpargatas vendidas sobre el total general de unidades comercializadas por la fábrica.
El número de factura en la que se despachó la máxima cantidad de unidades.
Nota: Si no se llegó a registrar ninguna factura válida antes del cierre, el sistema simplemente deberá informar que 
'No se registraron ventas'."""

# Constantes de precios (en mayúsculas por convención para constantes)

SANDALIAS = 2500
ALPARGATAS = 3500

# Inicialización de variables
nro_factura = int(input("Ingrese el numero de factura: "))  # Primer input de factura
cont_S = 0  # Contador total de unidades de sandalias vendidas (cantidad)
cont_A = 0  # Contador total de unidades de alpargatas vendidas (cantidad)
cont = 0  # Contador de facturas procesadas (usado como flag para primera iteración)

# Inicialización para máximo (descomentado y corregido)
cant_max = 0  # Cantidad máxima vendida en una factura (inicial en 0)
nro_fact_max = 0  # Número de factura correspondiente al máximo

# Validación inicial de la primera factura (debe ser >0 para entrar al bucle)
while nro_factura <= 0 and nro_factura != 0:  # Si es <=0 pero no 0 (finalización), pide de nuevo
    nro_factura = int(input("Error: Ingrese un número de factura válido (>0): "))

# Bucle principal: procesa facturas mientras nro_factura != 0
while nro_factura != 0:
    
    # Input y validación de cantidad (mayorista: mínima >50, y >=0)
    cant = int(input("Cantidad comprada: "))
    while cant <= 50:  # Corrección: <=50 para rechazar exactamente 50; también cubre negativos
        print("Error: La cantidad debe ser mayor a 50 (venta mayorista).")
        cant = int(input("Cantidad comprada: "))
    
    # Input y validación de tipo de producto (un solo tipo por factura)
    tipo = input("Ingrese tipo de producto (S para sandalias, A para alpargatas): ").upper()  # Convierte a mayúsculas inmediatamente
    while tipo != 'A' and tipo != 'S':  # Valida que sea A o S (mayúsculas)
        tipo = input("Error: Ingrese tipo de producto (S o A): ").upper()  # Corrección: Agregué .upper() aquí para consistencia
    
    # Actualizar contadores de cantidades por tipo de producto
    if tipo == 'A':  # Corrección: Simplificado (no necesita 'or tipo=='a'' ya que todo es upper())
        cont_A += cant  # Suma la cantidad al total de alpargatas
    if tipo == 'S':  # Para sandalias (if separado para cubrir ambos casos)
        cont_S += cant  # Suma la cantidad al total de sandalias
    
    # Lógica para máximo de cantidad por factura (inicializar y comparar)
    if cont == 0:  # Primera factura: inicializar el máximo con esta cantidad
        cant_max = cant
        nro_fact_max = nro_factura
    if cant > cant_max:  # Para facturas siguientes: actualizar si la cantidad actual es mayor
        cant_max = cant
        nro_fact_max = nro_factura
    
    # Incrementar contador de facturas
    cont += 1
    
    # Input para la siguiente factura (con validación básica)
    nro_factura = int(input("Ingrese número de factura (0 para finalizar): "))
    while nro_factura < 0:  # Valida que no sea negativo (0 es para finalizar)
        nro_factura = int(input("Error: Ingrese un número de factura válido (>=0): "))

# Cálculos finales
total_unidades = cont_S + cont_A  # Total de unidades vendidas (para porcentaje)

print("\n--- Resultados de las ventas ---")
if cont > 0:  # Si se procesó al menos una factura
    # Total en monto de sandalias
    total_S = SANDALIAS * cont_S
    print(f"El total en monto de las sandalias es: ${total_S:,.2f}")  # Formato con comas y 2 decimales
    
    # Porcentaje en cantidad de alpargatas respecto al total de unidades
    if total_unidades > 0:  # Evita división por cero
        porcentaje_A = (cont_A / total_unidades) * 100
        print(f"El porcentaje en cantidad de alpargatas respecto al total es: {porcentaje_A:.2f}%")
    else:
        print("No se vendieron productos (porcentaje: 0%)")
    
    # Número de factura con máxima cantidad
    print(f"El número de factura en la que se vendió la máxima cantidad es: {nro_fact_max} (cantidad: {cant_max} unidades)")
else:
    print("No se registraron ventas.")

# Nota: No se usa el precio de alpargatas en los cálculos requeridos, pero si necesitas total general, agrégalo aquí.
