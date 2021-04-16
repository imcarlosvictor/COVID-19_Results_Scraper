from bs4 import BeautifulSoup
import requests


class Data:

    def __init__(self):
        self.URL = 'https://www.worldometers.info/coronavirus/'
        self.source = requests.get(self.URL)

        self.soup = BeautifulSoup(self.source.content, 'html.parser')
        self.case_results_block = self.soup.find_all('div', class_='col-md-6')

    def http_response(self):
        response = self.source.status_code
        print(f'HTTP Response [{response}]')

    def total_cases(self):

        # Total Coronavirus Cases
        total_cases = self.soup.find_all('h1')
        total_cases_results = self.soup.find_all(
            'div', class_='maincounter-number')

        total_covid_cases = zip(total_cases, total_cases_results)

        for x, y in total_covid_cases:
            print(x.get_text(), y.get_text())

    def active_cases(self):
        # Active cases
        active_cases_title = self.case_results_block[0].find(
            'span', class_='panel-title').get_text()

        active_infected_title = self.case_results_block[0].find(
            'div', attrs={'style': 'font-size:13.5px'}).get_text()

        active_infected_result = self.case_results_block[0].find(
            class_='number-table-main').get_text()

        mild_condition = self.case_results_block[0].find(
            'div', attrs={'style': 'float:left; text-align:center'}).get_text()

        critical_condition = self.case_results_block[0].find(
            'div', attrs={'style': 'float:right; text-align:center'}).get_text()

        results = {
            'active_cases_title': active_cases_title,
            'active_infected_title': active_infected_title,
            'mild_condition': mild_condition,
            'critical_condition': critical_condition
        }

        return results

    def closed_cases(self):
        # Closed Cases
        closed_cases_title = self.case_results_block[1].find(
            'span', class_='panel-title').get_text()

        total_outcome_title = self.case_results_block[1].find(
            'div', attrs={'style': 'font-size:13.5px'}).get_text()

        total_outcome_result = self.case_results_block[1].find(
            'div', class_='number-table-main').get_text()

        recovered = self.case_results_block[1].find(
            'div', attrs={'style': 'float:left; text-align:center'}).get_text()

        deaths = self.case_results_block[1].find(
            'div', attrs={'style': 'float:right; text-align:center'}).get_text()
        pass

    def table_data(self):
        # Table Reports by Country/Territory
        # table = soup.find('div', class_='row')
        # table_title = soup.find('h3', id='countries').get_text()
        # table_results = table_contents.find('tr')
        table_contents = self.soup.find(
            'table', id='main_table_countries_today')
        table_body = table_contents.find('tbody')

        # print(table_contents)
        print(table_body.get_text())
        # print(table_body.get_text())
        pass


def main():

    covid_data = Data()

    for title, data in covid_data.active_cases().items():
        print(title)



if __name__ == '__main__':
    main()
