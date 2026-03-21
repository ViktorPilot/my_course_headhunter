from src.api_interaction import get_api_data_employers, get_api_data_vacancy


def main(list_employers) -> None:
    """Функция, объединяющая функциональность всего проекта"""
    list_data_employers = get_api_data_employers(list_employers)
    print(get_api_data_vacancy(list_data_employers))







if __name__ == '__main__':
    list_employers_ = ['Авиакомпания Победа', 'Уральские авиалинии, Авиакомпания', 'ЧПОУ Авиашкола Аэрофлота',
                      'Азур Эйр', 'Хабаровские авиалинии', 'Акционерное общество "Энергоспецмонтаж"', 'Банк ВТБ (ПАО)',
                      'СИБУР, Группа компаний', 'X5 Tech']
    main(list_employers_)