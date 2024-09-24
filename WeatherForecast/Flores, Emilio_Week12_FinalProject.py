# DSC 510 - Intro to Programming
# Professor Michael Eller
# Final Project - Weather App -  Week 12
# Author Emilio Flores
# May 28th, 2024


import requests


def welcome_message():
    # This function prints a welcome message for the user.
    print("Thank you for using this weather app.",
          "This program will obtain the current weather from any location in the United States.",
          "You will need the zip code or city/state of the location(s) you want to look up.",
          "Please follow the instructions to request a weather forecast(s) and/or to end the program.",
          "_________________________________________________________________________________________",
          sep="\n")


def zipcode_or_city_name():
    # This function will ask the user if they want to obtain a weather forecast using zip code or city name/ state code.
    # This function will call the API function by zip code or city name/state code depending on the input.
    while True:
        try:
            search_type = input("Do you want to search by zip code or by city name? (Type 'z' for 'zip code' or 'c' "
                                "for city name):\n").strip().lower()
            if search_type not in ['z', 'c']:
                raise ValueError("Invalid input. Please type 'z' for 'zip code' or 'c' for 'city name'.")
        except ValueError as value:
            print(f"Error: {value}")
        except Exception as all_errors:
            print("An error has occurred, ", all_errors)
        else:
            if search_type.lower() == 'z':
                return zip_code_request()
            elif search_type.lower() == 'c':
                return city_name_request()


def zip_code_request():
    # This function gets the geolocation (latitude, longitude) of the zip code entered by the user.
    # This try/except/else block prevents users from typing a zip code that does not match the
    # US standard zip code format.
    while True:
        try:
            zip_code = input("Please enter zip code: \n").strip()
            if len(zip_code) != 5 or not zip_code.isdigit() or int(zip_code) < 0:
                raise ValueError("Invalid Input. Zip codes must be 5 digits long, positive, and numeric.")
            api_key = "YOUR KEY"
            country_code = "US"
            zip_code_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
            response = requests.get(zip_code_url)
        except ValueError as value:
            print(f"Error: {value}")
        except requests.HTTPError as http_error:
            print("There was an HTTp error, ", http_error)
        except requests.ConnectionError as connection_error:
            print("There was a connection error, ", connection_error)
        except Exception as all_errors:
            print("An error has occurred, ", all_errors)
        else:
            if response.status_code == 200:
                response_json = response.json()
                latitude = response_json['lat']
                longitude = response_json['lon']
                return latitude, longitude
            else:
                print('Zip code was not found. Please try again.')


def city_name_request():
    # This function gets the geolocation (latitude, longitude) of the city name/state code entered by the user.
    # This function prevents the user for entering invalid city names and/or state codes.
    while True:
        try:
            city_name = input("Please enter city name: \n").lower().strip()
            if len(city_name) < 2 or not all(character.isalpha() or character.isspace() for character in city_name):
                raise ValueError("Invalid Input. City name must be at least 2 characters long and contain only letters.")
            state_code = input("Please enter state code: (For example: 'Texas' = 'TX') \n").lower().strip()
            if len(state_code) != 2 or not state_code.isalpha():
                raise ValueError("Invalid Input. State code must be exactly 2 letters longs and contain only letters.")
            country_code = "US"
            limit = '1'
            api_key = "YourKey"
            city_name_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.title()},{state_code.upper()},{country_code}&limit={limit}&appid={api_key}"
            response = requests.get(city_name_url)
        except ValueError as value:
            print(f"Error: {value}")
        except requests.HTTPError as http_error:
            print("There was an HTTp error, ", http_error)
        except requests.ConnectionError as connection_error:
            print("There was a connection error, ", connection_error)
        except Exception as all_errors:
            print("An error has occurred, ", all_errors)
        else:
            if response.status_code == 200:
                response_json = response.json()
                if len(response_json) == 0:
                    print("City and/or state not found. Please try again.")
                else:
                    for item in response_json:
                        latitude = item['lat']
                        longitude = item['lon']
                    return latitude, longitude


def geo_location_request():
    # This function will obtain the weather forecast from the weather API using the latitude and longitude that
    # the zip_code_request function generates.
    # This function will also ask the user if they want to obtain weather forecast using imperial or metric units.
    latitude_response1, longitude_response1 = zipcode_or_city_name()
    while True:
        try:
            units_request = input("Do you want your forecast in metric units? Or in imperial units? (Type 'metric' or "
                                  "'imperial')\n").strip().lower()
            if units_request.lower() not in ['metric', 'imperial']:
                raise ValueError("Invalid input. Type 'metric' or 'imperial'.")
            api_key = "Your Key"
            geo_location_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude_response1}&lon={longitude_response1}&appid={api_key}&units={units_request.lower()}"
            geo_response = requests.get(geo_location_url)
        except ValueError as value:
            print(f"Error: {value}")
        except requests.HTTPError as http_error:
            print("There was an HTTp error, ", http_error)
        except requests.ConnectionError as connection_error:
            print("There was a connection error, ", connection_error)
        except Exception as all_errors:
            print("An error has occurred, ", all_errors)
        else:
            if geo_response.status_code == 200:
                geo_response_json = geo_response.json()
                return geo_response_json
            else:
                print("Weather forecast not found. Try again.")


def pretty_print():
    # This function calls the geolocation request and prints the weather forecast in a user-friendly format.
    weather_forecast = geo_location_request()
    print(f"This weather forecast is for the city of: {weather_forecast['name']}",
          f"The current temperature is {weather_forecast['main']['temp']}",
          f"The temperature feels like: {weather_forecast['main']['feels_like']}",
          f"The high for today is: {weather_forecast['main']['temp_max']}",
          f"The low for today is: {weather_forecast['main']['temp_min']}",
          f"The current pressure is: {weather_forecast['main']['pressure']}",
          f"The current humidity is: {weather_forecast['main']['humidity']}",
          f"The current wind speed is: {weather_forecast['wind']['speed']}",
          f"The weather description is: {weather_forecast['weather'][0]['description']}",
          sep="\n")


def program_loop():
    # This function is a while loop that will allow the user to obtain as many weather forecasts as needed/wanted
    # until the loop is broken by following the right command.
    while True:
        try:
            loop_input = input("Do you want to search a weather forecast today? (Type 'y' for 'yes' and 'n' for "
                               "'no'):\n").strip().lower()
            if loop_input not in ['y', 'n']:
                raise ValueError("Invalid input. Please type 'y' for 'yes' and 'n' for 'no'.")
            elif loop_input == 'y':
                pretty_print()
            else:
                print("Thanks for using the weather forecast program. Have a good day!")
                break
        except ValueError as value:
            print(f"Error: {value}")


def main():
    # Main function calls welcome message once and then the program loop. The program loop function calls all other
    # functions within a while loop.
    welcome_message()
    program_loop()


if __name__ == "__main__":
    main()
