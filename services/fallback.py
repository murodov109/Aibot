import requests

class FallbackAPI:
    def __init__(self, apis):
        self.apis = apis

    def get_data(self, endpoint, params=None):
        for api in self.apis:
            try:
                response = requests.get(f'{api}{endpoint}', params=params)
                response.raise_for_status()  # Raise an error for bad responses
                return response.json()  # Return JSON response if successful
            except requests.RequestException as e:
                print(f'API call failed: {api} with error {e}')  # Log the error
        raise Exception('All APIs failed to provide data.')  # Raise an error if all fail

# Example APIs to use
apis = [
    'https://api1.example.com',
    'https://api2.example.com',
    'https://api3.example.com',
]

fallback_api = FallbackAPI(apis)

# Example usage:
# data = fallback_api.get_data('/your_endpoint')
# print(data)