import requests

def get_weather(city, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # Corrected 'metrie' to 'metric'

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        weather_data = response.json()
        if weather_data['cod'] == 200:
            print(f'El clima en {weather_data["name"]}:')
            print(f'Descripción: {weather_data["weather"][0]["description"]}')
            print(f'Temperatura: {weather_data["main"]["temp"]}°C')
            print(f'Humedad: {weather_data["main"]["humidity"]}%')
            print(f'Vento: {weather_data["wind"]["speed"]} m/s')
        else:
            print(f'Error: {weather_data["message"]}')
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response")

if __name__ == "__main__":
    city_name = 'Zapopan'
    api_key = "69ec8ca2037d63a120d31c59efd0f604"
    get_weather(city_name, api_key)
# Ejemplo de uso
# city = 'Madrid'  # Cambia esto a la ciudad deseada
# api_key = 'tu_api_key_aqui'  # Reemplaza con tu clave de API
# get_weather(city, api_key)
