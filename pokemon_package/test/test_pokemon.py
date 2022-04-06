import unittest
from unittest import mock
from json import dumps
from requests.models import Response
from src.attack_modifier import get_pokemon_attack_multiplier 

class TestDomino(unittest.TestCase):
    def mocked_request_correct(*args, **kwargs):
        response = Response()
        response.status_code = 200
        data = {
            "damage_relations": {
                "no_damage_to": [{"name": "dragon"}, {"name": "fairy"}],
                "double_damage_to": [{"name": "bug"}, {"name": "steel"}],
                "half_damage_to": [{"name": "ground"}, {"name": "water"}],
            }
        }
        data_json = dumps(data)
        response._content = str.encode(data_json)
        return response

    def mocked_request_incorrect_reponse_code(*args, **kwargs):
        response = Response()
        response.status_code = 404
        data = {
            "damage_relations": {
                "no_damage_to": [{"name": "dragon"}, {"name": "fairy"}],
                "double_damage_to": [{"name": "bug"}, {"name": "steel"}],
                "half_damage_to": [{"name": "ground"}, {"name": "water"}],
            }
        }
        data_json = dumps(data)
        response._content = str.encode(data_json)
        return response
    
    def mocked_request_incorrect_data(*args, **kwargs):
        response = Response()
        response.status_code = 200
        data = {
            "damage_relations": {
                "random_data": [{"name": "dragon"}, {"name": "fairy"}],
            }
        }
        data_json = dumps(data)
        response._content = str.encode(data_json)
        return response

    @mock.patch('requests.get', side_effect=mocked_request_incorrect_reponse_code)
    def test_incorrect_response_code(self, mock_get):
        modifier = get_pokemon_attack_multiplier('fire', ['bug'])
        self.assertFalse(modifier)

    @mock.patch('requests.get', side_effect=mocked_request_incorrect_data)
    def test_incorrect_response_data(self, mock_get):
        modifier = get_pokemon_attack_multiplier('fire', ['bug'])
        self.assertFalse(modifier)

    @mock.patch('requests.get', side_effect=mocked_request_correct)
    def test_correct_no_damage(self, mock_get):
        modifier = get_pokemon_attack_multiplier('fire', ['bug', 'water', 'dragon'])
        self.assertEqual(modifier, '0x')

    @mock.patch('requests.get', side_effect=mocked_request_correct)
    def test_correct_multiplier_simple(self, mock_get):
        modifier = get_pokemon_attack_multiplier('fire', ['bug'])
        self.assertEqual(modifier, '2x')

    @mock.patch('requests.get', side_effect=mocked_request_correct)
    def test_correct_multiplier_advanced(self, mock_get):
        modifier = get_pokemon_attack_multiplier('fire', ['bug', 'water'])
        self.assertEqual(modifier, '1x')

if __name__ == '__main__':
    unittest.main()