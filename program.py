import requests

class Cat:
    'Constructor just takes a number in. No real purpose of this constructor because'
    'everything is done in _get_breed'
    def __init__(self, number):
        self.number = number

    '_get_breed takes in an int n and uses that to find the corresponding breed.'
    'Uses json to convert http file to json in order for breed to be accessed easily'
    def _get_breed(self, n):
        result = requests.get('https://catfact.ninja/breeds')
        json_response = result.json()
        repository = json_response['data'][n]['breed']
        return repository
    
catcat = Cat(3)
print(catcat._get_breed(3))
