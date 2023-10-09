import requests
from bs4 import BeautifulSoup


def scrape_aerodrome_info(icao_code):
    # Construct the URL for the specific ICAO code
    url = f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao_code}"

    # Send a request to the website
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data from the website.")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Extracting the information
    cartas_title = soup.find(id="cartas")
    cartas_ul = cartas_title.find_next("ul")
    cartas_lis = cartas_ul.find_all_next("li")
    sunrise_info = soup.find(
        "sunrise").text.strip()
    sunset_info = soup.find("sunset").text.strip()
    taf_component = soup.find(string='TAF')
    taf_info = taf_component.find_next("p").text.strip()
    metar_component = soup.find(string='METAR')
    metar_info = metar_component.find_next("p").text.strip()

    # Printing the information
    print("Cartas Disponíveis:")
    for link in cartas_lis:
        print(link.text.strip())

    print("\nHorários de Nascer e Pôr do Sol:")
    print("Nascer do sol:", sunrise_info)
    print("Pôr do sol", sunset_info)

    print("\nInformações de TAF e METAR Disponíveis:")
    print("TAF:", taf_info)
    print("METAR:", metar_info)


if __name__ == "__main__":
    icao_code = input(
        "Digite o código ICAO do aeródromo (por exemplo, SBMT): ").upper()
    scrape_aerodrome_info(icao_code)
