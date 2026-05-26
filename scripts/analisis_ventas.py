
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# Crear columna total
df["total"] = df["cantidad"] * df["precio"]

# Calcular ventas totales
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Crear gráfico
ventas_por_producto = df.groupby("producto")["total"].sum()

ventas_por_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico generado correctamente")
