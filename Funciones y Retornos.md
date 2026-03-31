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

# Buenas Prácticas: Visualización y Parámetros en Python

### B. Mostrar como Tabla (Paso de Parámetros)
Se utiliza para visualizar estructuras de datos completas, como **arreglos o matrices**. 
* **Regla estricta:** Se deben pasar los datos por parámetro.
* **Prohibido:** Evitar el uso de variables globales para que la función sea reutilizable y modular.

### C. `print()` dentro de la Función (Casos Especiales)
Se recomienda únicamente en dos situaciones:
1. Cuando la función genera **múltiples resultados** que no conviene empaquetar en un solo `return`.
2. Cuando se pide un **reporte detallado** o un "Retorno múltiple visual".
   * *Ejemplo:* "Calcular el porcentaje de cada uno de los tipos de elementos en un vector".

---

## 2. Reglas de Oro para un Código Limpio

### El Principio de Parámetros No Globales
La comunicación entre el Programa Principal (PPAL) y las funciones debe ser explícita. Siempre pasa el vector como argumento.

* **`arreglo`**: Es el nombre del parámetro técnico dentro de la definición de la función.
* **`arreglos[]`**: Es el vector real declarado antes del PPAL para ser enviado como parámetro.

### Ejemplo de Uso Correcto (Índice y Valor)
Si buscas un valor máximo, lo ideal es retornar únicamente el **índice**. Esto permite que el PPAL decida cómo mostrar la información.

```python
# --- Dentro del Programa Principal (PPAL) ---

# La función busca y retorna solo el índice
idx = buscar_maximo(mi_vector) 

# El PPAL se encarga de la impresión final usando ese índice
print(f"El valor máximo es {mi_vector[idx]} en la posición {idx}")

resultado = calcular_promedio(vector)
print(f"El promedio es: {resultado}")
