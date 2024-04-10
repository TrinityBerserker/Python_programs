import pandas as pd

# Cargar datos desde un archivo CSV
data = pd.read_csv("datos.csv")

# Mostrar las primeras filas del DataFrame
print(data.head())

# Resumen estadístico del DataFrame
print(data.describe())

# Información sobre el DataFrame
print(data.info())
