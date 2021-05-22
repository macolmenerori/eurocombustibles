import pandas as pd
import numpy as np
import json

# Coger datos oficiales y parsearlos
prices_raw = pd.read_excel('http://ec.europa.eu/energy/observatory/reports/latest_prices_with_taxes.xlsx', 'En In EURO', header=8, usecols='B:D', names=['country', 'gasoline', 'diesel'], nrows=27, dtype=str, encoding='unicode')

# Crear un JSON
prices_JSON = prices_raw.to_json(orient='records', force_ascii=False)

# Escribir el JSON
filename = "fuel_prices.json"
fichero = open(filename, 'w')
fichero.write(prices_JSON)
fichero.close()
