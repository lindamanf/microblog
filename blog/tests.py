from django.test import TestCase, Client

# ./manage.py testでテストを開始

class BlogTestCase(TestCase):
    def setUp(self):
        self.c = Client()
    
    def test_index_access(self):
        res = self.c.get('/')
        self.assertEqual(200, res.status_code)
        # status code => 200 OK
        # status code => 404 Not Found
        # status code => 302 Redirect

    def test_fail_access(self):
        res = self.c.get('/unknown')
        self.assertEqual(404, res.status_code)