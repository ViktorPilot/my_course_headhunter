import requests


def get_api_data_employers(list_employers: list[str]) -> list[tuple]:
    """Получение данных о работодателях через API"""
    url = 'https://api.hh.ru/employers'
    list_data_employers = []
    for employeer in list_employers:
        params = {'text': employeer}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            for i in response.json().get('items', {}):
                vacancy_url = i.get('vacancies_url', None)
                count_vacancyes = i.get('open_vacancies', None)
                tuple_company = (employeer, vacancy_url, count_vacancyes)
                list_data_employers.append(tuple_company)
        else:
            print(f'Ошибка при получении данных о работодателе {employeer}: {response.status_code}')
            continue
    return list_data_employers


def get_api_data_vacancy(list_data_employers: list[tuple]) -> list[tuple]:
    """Получение данных о вакансиях работодателей, полученных через API"""
    list_data_vacancy = []
    for employer in list_data_employers:
        if employer[1] is not None:
            response = requests.get(employer[1])
            if response.status_code == 200:
                for i in response.json().get('items', {}):
                     data = (employer[0], i.get('name', None),
                             i.get('area', {}).get('url', None) if i.get('area') is not None else None,
                             i.get('salary', {}).get('from', None) if i.get('salary') is not None else None,
                             i.get('salary', {}).get('to', None) if i.get('to') is not None else None,
                             i.get('address', {}).get('city', None) if i.get('city') is not None else None,
                             i.get('published_at', None))
                     list_data_vacancy.append(data)
            else:
                print(f'Ошибка при получении данных о вакансиях работодателя {employer[0]}: {response.status_code}')
                continue
        else:
            continue
    return list_data_vacancy




