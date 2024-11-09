import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv("ventas.csv")

# Mostrar las primeras filas
print(data.head())

# Convertir la columna de fechas al formato datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])

# Crear una columna para el mes
data['Mes'] = data['Fecha'].dt.month

# Agrupar las ventas por mes
ventas_por_mes = data.groupby('Mes')['Ventas'].sum()

# Visualización de ventas por mes
plt.figure(figsize=(10, 6))
sns.barplot(x=ventas_por_mes.index, y=ventas_por_mes.values, palette="viridis")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Total de Ventas")
plt.show()
