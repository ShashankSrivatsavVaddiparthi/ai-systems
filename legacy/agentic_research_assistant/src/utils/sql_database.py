import requests
from langchain_community.utilities import SQLDatabase

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"

response = requests.get(url)

if response.status_code == 200:
  with open("Chinook.db", "wb") as file:
    file.write(response.content)
  print("File downloaded and saved as Chinook.db")
else:
  print(f"Failed to download the file. Status code: {response.status_code}")

db = SQLDatabase.from_uri("sqlite:///Chinook.db")