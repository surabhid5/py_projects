import unittest
import unit_test_main

class TestMain(unittest.TestCase):
   def setUp(self):
       ##sets up this function before each other function/method is run
       print('about to test a function')

   def test_do_stuff(self):
       test_param = 10
       result = unit_test_main.do_stuff(test_param)
       self.assertEqual(result, 15)

   def test_do_stuff2(self):
       test_param = 'gsjkdj'
       result = unit_test_main.do_stuff(test_param)
       #self.assertTrue(isinstance(result, ValueError))
       self.assertIsInstance(result, ValueError)

   def test_do_stuff3(self):
       test_param = None
       result = unit_test_main.do_stuff(test_param)
       #self.assertTrue(isinstance(result, ValueError))
       self.assertEqual(result, 'Please enter a number')


   def test_do_stuff4(self):
        test_param = ''
        result = unit_test_main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertEqual(result, 'Please enter a number')

   def test_do_stuff5(self):
       test_param = 0
       result = unit_test_main.do_stuff(test_param)
       # self.assertTrue(isinstance(result, ValueError))
       self.assertEqual(result, 'Please enter a number')

   def tearDown(self):
      '''To clean up or repalce some variables'''
      print('cleaning up')


if __name__== '__main__':
  unittest.main()
