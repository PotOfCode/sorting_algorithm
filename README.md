
# **Planteamiento del Problema: Sistema de Ordenamiento para Carfix**  

## **📌 Contexto**  
**Carfix** es una plataforma de venta de repuestos automotrices que necesita mostrar productos ordenados de manera eficiente. Actualmente, el sistema no cuenta con un método optimizado para ordenar grandes volúmenes de datos, lo que puede afectar la experiencia del usuario al realizar búsquedas.  

### **Problemas específicos:**  
1. **Tiempo de respuesta lento** al ordenar listas grandes de repuestos.  
2. **Falta de comparación entre algoritmos** para determinar cuál es más eficiente.    

---

# **💡 Solución Propuesta: Algoritmos de Ordenamiento**  

## **🔧 Implementación**  
Se desarrolló un sistema en Python que permite:  
✅ **Ordenar repuestos por precio** usando 4 algoritmos distintos:  
- **Bubble Sort** (para conjuntos pequeños)  
- **Insertion Sort** (eficiente en datos casi ordenados)  
- **Quick Sort** (óptimo para grandes volúmenes)  
- **Merge Sort** (estable y consistente)  

✅ **Comparar tiempos de ejecución** para determinar el método más eficiente.    

## **📊 Características de cada Caso**  
| Algoritmo       | Mejor Caso | Peor Caso | Uso Recomendado          |  
|-----------------|------------|-----------|--------------------------|  
| **Bubble Sort**    | O(n)       | O(n²)     | Pequeños datasets        |  
| **Insertion Sort** | O(n)       | O(n²)     | Datos parcialmente ordenados |  
| **Quick Sort**     | O(n log n) | O(n²)     | Grandes volúmenes        |  
| **Merge Sort**     | O(n log n) | O(n log n)| Datos muy grandes        |  

---

# **🚀 Cómo Usar el Código**  
1. **Menú de opciones:**  
   - **1️⃣ Ver repuestos sin ordenar** (muestra los datos originales).  
   - **2️⃣ Ordenar por método específico** (elige entre los 4 algoritmos).  
   - **3️⃣ Comparar todos los métodos** (analiza cuál es más rápido).  
   - **4️⃣ Salir** (cierra el programa).  

2. **Resultados:**  
   - Se muestran los **primeros 8 repuestos ordenados por precio**.  
   - Se calcula el **tiempo de ejecución** de cada algoritmo.  

3. **Datos Personalizables:**
   ```bash
   def mostrar_repuestos(repuestos, limite=n):
   ```
n=Número máximo de repuestos a generar

```bash
   datos = generar_repuestos(x)
   ```

x=Valor de los datos asignados a un repuesto

---

# **📌 Conclusión**  
Este proyecto demuestra cómo diferentes algoritmos de ordenamiento optimizan la gestión de catálogos en **Carfix**, mejorando la velocidad y eficiencia en la visualización de productos.  

🔗 **GitHub:** [https://github.com/PotOfCode/sorting_algorithm](#)  

---
