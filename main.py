from bs4 import BeautifulSoup
import requests


def main():

    BASEURL = 'https://www.worldometers.info/coronavirus/'
    source = requests.get(BASEURL)

    response = source.status_code
    print(f'HTTP Response [{response}]')

    soup = BeautifulSoup(source.text, 'lxml')

    # Total Coronavirus Cases
    total_cases = soup.find_all('h1')
    total_cases_results = soup.find_all('div', class_='maincounter-number')

    total_covid_cases = zip(total_cases, total_cases_results)

    for x, y in total_covid_cases:
        print(x.get_text(), y.get_text())

    case_results_block = soup.find_all('div', class_='col-md-6')

    # Active cases
    active_cases_title = case_results_block[0].find(
        'span', class_='panel-title').get_text()

    active_infected_title = case_results_block[0].find(
        'div', attrs={'style': 'font-size:13.5px'}).get_text()

    active_infected_result = case_results_block[0].find(
        class_='number-table-main').get_text()

    mild_condition = case_results_block[0].find(
        'div', attrs={'style': 'float:left; text-align:center'}).get_text()

    critical_condition = case_results_block[0].find(
        'div', attrs={'style': 'float:right; text-align:center'}).get_text()


    # # Closed Cases
    closed_cases_title = case_results_block[1].find(
        'span', class_='panel-title').get_text()

    total_outcome_title = case_results_block[1].find(
        'div', attrs={'style': 'font-size:13.5px'}).get_text()

    total_outcome_result = case_results_block[1].find(
        'div', class_='number-table-main').get_text()

    recovered = case_results_block[1].find(
        'div', attrs={'style': 'float:left; text-align:center'}).get_text()

    deaths = case_results_block[1].find(
        'div', attrs={'style': 'float:right; text-align:center'}).get_text()


    # Table Reports by Country/Territory

    # table = soup.find('div', class_='row')
    # table_title = soup.find('h3', id='countries').get_text()
    table_contents = soup.find('table', id='main_table_countries_today')
    # table_results = table_contents.find('tr')
    table_body = table_contents.find('tbody')

    # print(table_contents)
    # print(table_body.get_text())

    

    

if __name__ == '__main__':
    main()
