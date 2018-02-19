import requests


def get_first_page():
    response = requests.get('https://swapi.co/api/planets').json()
    return response['results']


def get_second_page():
    response = requests.get('https://swapi.co/api/planets/?page=2').json()
    return response['results']


def get_third_page():
    response = requests.get('https://swapi.co/api/planets/?page=3').json()
    return response['results']


def get_fourth_page():
    response = requests.get('https://swapi.co/api/planets/?page=4').json()
    return response['results']


def get_fifth_page():
    response = requests.get('https://swapi.co/api/planets/?page=5').json()
    return response['results']


def get_last_page():
    response = requests.get('https://swapi.co/api/planets/?page=6').json()
    return response['results']