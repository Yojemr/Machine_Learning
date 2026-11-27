# Carga y exploración de datos

| Notebook | Fuente |
| --- | --- |
| [1. Excel](1.load_excel.ipynb) | Libro de ventas de ejemplo generado a partir del CSV. |
| [2. CSV](2.load_csv.ipynb) | [Ventas de ejemplo](data/ventas_ejemplo.csv). |
| [3. API](3.load_api.ipynb) | Publicaciones de [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts). |
| [4. Web scraping](4.load_webscraping.ipynb) | Catálogo de [Books to Scrape](https://books.toscrape.com/). |

## Preparar el entorno

Ejecuta estos comandos en PowerShell desde la raíz del repositorio. Si ya tienes `.venv`, usa ese entorno.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\data_load\requirements.txt
```

Para el primer notebook, genera `data_load/data/dataset_ventas.xlsx` si aún no existe.

```powershell
.\.venv\Scripts\python.exe -c "import pandas as pd; pd.read_csv('data_load/data/ventas_ejemplo.csv', parse_dates=['fecha']).to_excel('data_load/data/dataset_ventas.xlsx', sheet_name='dataset_ventas', index=False)"
```

En VS Code, abre cada notebook con las extensiones Python y Jupyter, selecciona el kernel de `.venv` y ejecuta sus celdas en orden. Los notebooks de API y web scraping requieren conexión a Internet.
