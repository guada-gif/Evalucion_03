from django.test import TestCase, Client

# Create your tests here.


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        # Prueba que la página de home carga correctamente, en la url específica
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def test_pag_crear_carcasa(self):
        # Prueba que la página de crear carcasa carga correctamente, en la url específica
        client = Client()
        response = client.get('http://localhost:8000/carcasa/crear')
        self.assertEqual(response.status_code, 200)
