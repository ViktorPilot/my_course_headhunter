from src.api_interaction import get_api_data_employers, get_api_data_vacancy
from src.file_interaction import create_database, create_table, insert_table


def main(list_employers, new_database) -> None:
    """Функция, объединяющая функциональность всего проекта"""
    list_data_employers = get_api_data_employers(list_employers)
    list_data_vacancy = get_api_data_vacancy(list_data_employers)
    create_database(new_database)
    create_table(new_database)
    insert_table(new_database, list_data_employers, list_data_vacancy)











if __name__ == '__main__':
    list_employers_ = ['Авиакомпания Победа', 'Уральские авиалинии, Авиакомпания', 'ЧПОУ Авиашкола Аэрофлота',
                      'Азур Эйр', 'Хабаровские авиалинии', 'Акционерное общество "Энергоспецмонтаж"', 'Банк ВТБ (ПАО)',
                      'СИБУР, Группа компаний', 'X5 Tech', 'Группа ЛСР']
    main(list_employers_, new_database='my_db')