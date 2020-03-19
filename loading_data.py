import pandas as pd


def load():
    deaths = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
    confirmed = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
    return deaths, confirmed


def get_data_pd(deaths, confirmed):    # print(deaths['Country/Region'].to_list())

    def app_country_data(data, country):
        _data = {'date': [], 'n_deaths': [], 'n_confirmed': []}
        # Province/State     France
        # Country/Region
        #     country_index_confirmed = confirmed.index[confirmed['Province/State']==country].tolist()[0]
        country_index_confirmed = confirmed.index[confirmed['Country/Region'] == country].tolist()[0]
        # country_index_deaths = deaths.index[deaths['Province/State']==country].tolist()[0]
        country_index_deaths = deaths.index[deaths['Country/Region'] == country].tolist()[0]

        def append_data(date):
            try:
                n_confirmed = confirmed.loc[country_index_confirmed][date]
            except KeyError:
                return
            n_deaths = deaths.loc[country_index_deaths][date]
            _data['date'].append(date)
            _data['n_deaths'].append(n_deaths)
            _data['n_confirmed'].append(n_confirmed)

        for m in (2, 3, 4):
            for d in range(30):
                date = f'{m}/{d}/20'
                append_data(date)

        df = pd.DataFrame(_data)
        data[country] = df

    data = {}  # str: DataFrame   for each country in list
    for country in ('France', 'Italy', 'Korea, South'):
        app_country_data(data, country)
        print(country)
    return data
