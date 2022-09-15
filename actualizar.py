## Actualizacion de datos: Ingresar valor de un ticker, fceha inicio y fecha fin, valores de la Api y guardarlo

import requests
## Request GET a la API
json_file = requests.get("https://api.polygon.io/v3/reference/tickers?apiKey=1ZpTnYWjNq5UmhH8hEhx0xNozdKtEg_9")
print(json_file.text)

## Guardo los contenidos en una DB
