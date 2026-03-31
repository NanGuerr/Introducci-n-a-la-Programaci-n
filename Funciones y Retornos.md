# Guía de Buenas Prácticas: Funciones y Retornos en Python

Esta guía resume los criterios para decidir cuándo una función debe retornar valores, cómo mostrar datos y el manejo correcto de parámetros.

---

## 1. ¿Cuándo usar `return` vs. cuándo no?

La decisión depende de la **responsabilidad** de la función:

* **Usa `return` (Funciones de Cálculo):** Cuando la función procesa información para obtener un resultado específico. 
    * *Ejemplos:* Calcular un promedio, buscar el máximo/mínimo, obtener un porcentaje o realizar búsquedas.
* **No uses `return` (Procedimientos):** Cuando la función realiza una acción de modificación o carga.
    * *Ejemplos:* Cargar datos en un vector, ordenar un arreglo (sorting) o limpiar una pantalla.

---

## 2. Formas de Mostrar Información

Existen tres escenarios principales para visualizar los datos procesados:

### A. Llamada con Retorno en el Programa Principal
Es la forma más estándar. La función hace el cálculo, devuelve el valor y este se imprime fuera.
> **Importante:** Si olvidas el `return` en una función de cálculo, al intentar imprimirla obtendrás `None` o errores de lógica.
```python
resultado = calcular_promedio(vector)
print(f"El promedio es: {resultado}")
