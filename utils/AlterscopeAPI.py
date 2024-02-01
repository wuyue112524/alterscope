import requests
import os
from typing import Dict, Any



class AlterscopeAPI:
    """
    A class to interact with the Alterscope API, providing methods to retrieve protocol development data
    and Discord sentiment scores.
    """

    def __init__(self, api_key: str = None):
        """
        Initialize the AlterscopeAPI object with an API key for authentication.
        If the API key is not provided, it attempts to fetch it from an environment variable.
        
        :param api_key: Optional; API key for authentication.
        """
        self.api_key = api_key or os.getenv('ALTERSCOPE_API_KEY', None)
        self.base_url = 'https://api.alterscope.org/'
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def _get_protocol_data(self, endpoint: str, protocol: str) -> Dict[str, Any]:
        """
        A helper method to get data for a specific protocol from a specified endpoint.
        
        :param endpoint: The API endpoint to query.
        :param protocol: The protocol to query.
        :return: A dictionary containing the API response.
        """
        if not protocol:
            raise ValueError("Protocol parameter is required")

        try:
            response = self.session.get(f'{self.base_url}{endpoint}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def get_protocol_development(self, protocol: str) -> Dict[str, Any]:
        """
        Get the development data for a specific protocol.
        
        :param protocol: The protocol to query.
        :return: A dictionary containing the development data for the protocol.
        """
        
        endpoint = f'data/development/{protocol}'
        return self._get_protocol_data(endpoint=endpoint, protocol=protocol)
    
    
    def get_protocol_discord_sentiment(self, protocol: str) -> Dict[str, Any]:
        """
        Get the Discord sentiment scores for a specific protocol.
        
        :param protocol: The protocol to query.
        :return: A dictionary containing the Discord sentiment scores for the protocol.
        """
        
        endpoint = f'scores/social/discord/{protocol}'
        return self._get_protocol_data(endpoint=endpoint, protocol=protocol)
