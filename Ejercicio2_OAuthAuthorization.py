import requests
import unittest

class TestAlbumsAPIAuthorizationCode(unittest.TestCase):
    TOKEN_URL = "https://example.com/oauth/token"
    AUTH_URL = "https://example.com/oauth/authorize"
    API_URL = "https://jsonplaceholder.typicode.com/albums"
    CLIENT_ID = "your_client_id"
    CLIENT_SECRET = "your_client_secret"
    REDIRECT_URI = "your_redirect_uri"
    AUTH_CODE = "authorization_code_provided_by_auth_server"

    def get_access_token(self):
        response = requests.post(self.TOKEN_URL, data={
            'grant_type': 'authorization_code',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'code': self.AUTH_CODE,
            'redirect_uri': self.REDIRECT_URI
        })
        response_data = response.json()
        return response_data['access_token']

    def test_albums_with_authorization_code(self):
        token = self.get_access_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(self.API_URL, headers=headers)
        self.assertEqual(response.status_code, 200)
        albums = response.json()
        successfull = 0

        # Verificamos si el texto de los álbumes coincide con lo esperado
        for album in albums:
            self.assertIn('userId', album)
            self.assertIn('id', album)
            self.assertIn('title', album)
            successfull += 1
    
        # Comparamos el resultado para ver que sea el correcto
        if len(albums) == successfull:
            print(f"La cantidad total de albums {len(albums)} se corresponde a la misma cantidad total que se verifican en la API {successfull}")
        else:
            print("La cantidad total de comprobaciones no son las mismas")

if __name__ == "__main__":
    unittest.main()
