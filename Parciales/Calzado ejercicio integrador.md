<p align="center">
  <img src="https://raw.githubusercontent.com/NanGuerr/Introducci-n-a-la-Programaci-n/refs/heads/main/Parciales/assets/Parcial%20Calzado.png" width="100%">
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

# Constantes de precios
SANDALIAS = 2500
ALPARGATAS = 3500

# Inicialización de variables
nro_factura = int(input("Ingrese el numero de factura: "))
cont_S = 0  # Cantidad total de sandalias
cont_A = 0  # Cantidad total de alpargatas

# Inicialización para máximo
cant_max = 0  
nro_fact_max = 0

# Validación inicial (0 es para finalizar, así que solo rechazamos negativos)
while nro_factura < 0:
    nro_factura = int(input("Error: Ingrese un número de factura válido (>=0): "))

# Bucle principal
while nro_factura != 0:
    
    # Validación de cantidad mayorista (> 50)
    cant = int(input("Cantidad comprada: "))
    while cant <= 50:
        print("Error: La cantidad debe ser mayor a 50 (venta mayorista).")
        cant = int(input("Cantidad comprada: "))
    
    # Validación de tipo de producto
    tipo = input("Ingrese tipo de producto (S para sandalias, A para alpargatas): ").upper()
    while tipo != 'A' and tipo != 'S':
        tipo = input("Error: Ingrese tipo de producto (S o A): ").upper()
    
    # Actualizar acumuladores por tipo
    if tipo == 'A':
        cont_A += cant
    elif tipo == 'S':
        cont_S += cant
    
    # Lógica simplificada para el máximo (Cualquier cant > 50 entrará la primera vez)
    if cant > cant_max:
        cant_max = cant
        nro_fact_max = nro_factura
    
    # Siguiente factura
    nro_factura = int(input("Ingrese número de factura (0 para finalizar): "))
    while nro_factura < 0:
        nro_factura = int(input("Error: Ingrese un número de factura válido (>=0): "))

# Cálculos finales
total_unidades = cont_S + cont_A

print("\n--- Resultados de las ventas ---")
# Si se cargó al menos una factura con cantidad válida, total_unidades será mayor a 0
if total_unidades > 0:
    # Total en monto de sandalias
    total_S = SANDALIAS * cont_S
    print(f"El total en monto de las sandalias es: ${total_S:.2f}")
    
    # Porcentaje de alpargatas
    porcentaje_A = (cont_A / total_unidades) * 100
    print(f"El porcentaje en cantidad de alpargatas respecto al total es: {porcentaje_A:.2f}%")
    
    # Factura con máxima cantidad
    print(f"El número de factura con la máxima cantidad es: {nro_fact_max} ({cant_max} unidades)")
else:
    print("No se registraron ventas.")
