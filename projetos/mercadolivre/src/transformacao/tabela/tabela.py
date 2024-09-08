import pandas as pd
import sqlite3
from datetime import datetime

# Definir o caminho para o arquivo JSONL
jsonl_path = 'data.jsonl'

# Ler os dados do arquivo JSONL
df = pd.read_json(jsonl_path, lines=True)

# Exibir o DataFrame resultante
print(df.head())