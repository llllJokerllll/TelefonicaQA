import requests
import unittest

class TestAlbumsAPI(unittest.TestCase):
    API_URL = "https://jsonplaceholder.typicode.com/albums"

    def test_albums(self):
        response = requests.get(self.API_URL)
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
