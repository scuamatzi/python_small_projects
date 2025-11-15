import requests, pytz
from rich.console import Console
from rich.table import Table

console = Console()
cities = ["Mexico City", "Delhi", "London", "New York", "Tokyo"]
table = Table(title="Weather Dashboard", style="cyan")
table.add_column("City", justify="center")
table.add_column("Temperature (°C)", justify="center")

for city in cities:
    temp = requests.get(f"https://wttr.in/{city}?format=%t").text
    table.add_row(city, temp)

console.print(table)
