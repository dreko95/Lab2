__author__ = 'lacks'

from functions import Bartender
import Server
import mock
import unittest

class DotsTest(unittest.TestCase):

    def test_bartender(self):
        obj = Bartender(1, 'WORK')
        obj.form_tasks()
        self.assertIsNotNone(len(obj.tasks), "CHECK IT BITCH!!!")
        self.assertIsNotNone(obj.get_task())


    @mock.patch('Server.server')
    def test_server(self, obj1):
        obj1.return_value = "I am server"
        self.assertEquals(Server.server(), "I am server", "Look at the page server")

    @mock.patch('Server.worker')
    def test_worker(self, obj1):
        obj1.return_value = "SAVE"
        self.assertEquals(Server.worker(), "SAVE")

    @mock.patch('Server.get_static')
    def test_get_static(self,obj1):
        obj1.return_value = 'ERROR get_static'
        self.assertEquals(Server.get_static(), "ERROR get_static")

    @mock.patch('Server.get_scripts')
    def test_get_scripts(self,obj1):
        obj1.return_value = 'ERROR get_scripts'
        self.assertEquals(Server.get_scripts(), "ERROR get_scripts")

    @mock.patch('Server.get_js')
    def test_get_js(self,obj1):
        obj1.return_value = 'ERROR get_js'
        self.assertEquals(Server.get_js(), "ERROR get_js")

    @mock.patch('Server.get_server_data')
    def test_get_server_data(self,obj1):
        obj1.return_value = {'AA': 'EE'}
        self.assertEquals(Server.get_server_data(),{'AA': 'EE'} )




if __name__ == "__main__":
    unittest.main()