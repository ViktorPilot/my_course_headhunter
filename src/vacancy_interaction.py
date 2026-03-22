from typing import Any


class DBManager:
    """Класс для получения данных из БД"""

    def __init__(self, conn: Any) -> None:
        """Инициализация экземпляров класса 'DBManager'"""
        self.__conn = conn
        self.__cur = self.__conn.cursor()

    def get_companies_and_vacancies_count(self) -> list[str]:
        """Получение списка всех компаний и количества вакансий у каждой компании"""
        self.__cur.execute('''SELECT company_name, COUNT(vacancy.vacancy) FROM company 
                            LEFT JOIN vacancy USING (company_id) GROUP BY company_id''')
        result = self.__cur.fetchall()
        return [f'{x[0]} - {x[1]} вакансий' for x in result]

    def get_all_vacancies(self) -> list[str]:
        """Получеение списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию"""
        self.__cur.execute(
            'SELECT company_name, vacancy, salary_from, vacancy_url FROM vacancy LEFT JOIN company USING (company_id)')
        result = self.__cur.fetchall()
        return [f'{x[0]}, должность: {x[1]}, зарплата: {x[2]}, ссылка на вакансию: {x[3]}' for x in result]

    def get_avg_salary(self) -> str:
        """Получение средней зарплаты по вакансиям"""
        self.__cur.execute(
            'SELECT AVG(salary_from) FROM vacancy WHERE salary_from IS NOT NULL')
        result = self.__cur.fetchone()
        return f'Средняя зарплата по вакансиям: {round(result[0])} руб.'

    def get_vacancies_with_higher_salary(self) -> list[str]:
        """Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.__cur.execute('''SELECT vacancy, salary_from FROM vacancy 
                            WHERE salary_from > (SELECT AVG(salary_from) FROM vacancy WHERE salary_from IS NOT NULL)''')
        result = self.__cur.fetchall()
        return [f'Должность: {x[0]}, зарплата: {x[1]}' for x in result]

    def get_vacancies_with_keyword(self, word: str) -> list[str]:
        """Получение списка всех вакансий, в названии которых содержатся переданные в метод слова"""
        self.__cur.execute(f'''SELECT * FROM vacancy WHERE EXISTS (SELECT * FROM company WHERE LOWER(company.company_name) 
        LIKE %s AND vacancy.company_id = company.company_id)''', (f'%{word.lower()}%',))
        result = self.__cur.fetchall()
        return [x[1] for x in result]
