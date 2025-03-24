import requests


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.data_fetched = False

    def fetch_all_data(self):
        response = requests.get('')

        if response.ok:
            self.data_fetched = True
            return 'CONNECTED'
        else:
            self.data_fetched = False
            return 'ERROR 404'
