import requests

def iterar_archivo(path,funcion):
    try:
        with open(path, "r") as archivo:
            for linea in archivo:
                limpio = linea.strip()
                funcion(limpio)
    except FileNotFoundError:
        print("Ese archivo no existe")
    except Exception as error:
        print("[Error] " + error)

def check_status(url):
    url = add_http(url)
    try:
        respuesta = requests.get(url, timeout=5)
        print(respuesta.status_code, url)
        write_file(respuesta.status_code, url)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")
        write_file(requests.exceptions.RequestException, url)

def add_http(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
        return url
    else:
        return url


def converter_capitalize(texto):
    print(texto.capitalize())

#iterar_archivo("domains", converter_capitalize)


def write_file(code,url,file = "resultados.txt"):
    with open(file, "a") as f:
        f.write(f"[{code}] - {url}\n")

iterar_archivo("domains", check_status)
