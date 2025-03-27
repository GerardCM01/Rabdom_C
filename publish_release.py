import requests
import os
import datetime

# Configura aquests valors segons el teu repositori
GITHUB_REPO = "GerardCM01/Random_C"  # Nom correcte del repositori
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Obté el token de les credencials de Jenkins
EXECUTABLE_PATH = "a.out"  # Canvia a "Main.exe" si treballes en Windows

# Genera el nom de la release i el tag
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
TAG_NAME = f"v{now}"
RELEASE_NAME = f"Release {now}"

# 1️. Crear la release a GitHub
release_url = f"https://api.github.com/repos/{GITHUB_REPO}/releases"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
release_data = {
    "tag_name": TAG_NAME,
    "name": RELEASE_NAME,
    "body": "Release generada automàticament per Jenkins",
    "draft": False,
    "prerelease": False
}

response = requests.post(release_url, json=release_data, headers=headers)

if response.status_code == 201:
    release_id = response.json()["id"]
    upload_url = response.json()["upload_url"].split("{")[0]  # Agafa la URL per pujar assets
    print(f"✅ Release creada: {RELEASE_NAME}")
else:
    print(f"❌ Error creant la release: {response.text}")
    exit(1)

# 2️. Pujar l'executable a la release
if os.path.exists(EXECUTABLE_PATH):
    with open(EXECUTABLE_PATH, "rb") as file:
        headers["Content-Type"] = "application/octet-stream"
        upload_response = requests.post(f"{upload_url}?name={os.path.basename(EXECUTABLE_PATH)}", headers=headers, data=file)

    if upload_response.status_code == 201:
        print("✅ Executable pujat correctament a la release!")
    else:
        print(f"❌ Error pujant l'executable: {upload_response.text}")
else:
    print("❌ No s'ha trobat l'executable per pujar!")
