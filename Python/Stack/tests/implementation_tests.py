
import unittest
import sys
sys.path.insert(0,'..')
from implementation import Stack


class TestStack(unittest.TestCase):

    def test_push_operation(self):
        """
        Test whether i can push successfully in stack or not
        will be pushing 1,2,3,4 and checking whether stack have that or not.
        """
        list_of_elements = [1,2,3]

        s = Stack()
        for each_element in list_of_elements:
            print('PUSHING--->',each_element)
            s.push(each_element)
  
        result = s.show_stack()
        self.assertEqual(result, list_of_elements)

    def test_pop_operation(self):
        """
        Test whether i can pop or not.
        Tests are devided in 2 senarios 
        
        1) popping from an empty stack ------> should return UNDEFLOW
        2) popping from filled stack

        will checked the popped element and result stack
        """
        empty_stack , filled_stack = [],[1,2,3]

        s = Stack()
        for each_element in empty_stack:
            print('PUSHING--->',each_element)
            s.push(each_element)

        result = s.pop()
        self.assertEqual(result, 'UNDERFLOW')

        for each_element in filled_stack:
            print('PUSHING--->',each_element)
            s.push(each_element)

        result = s.pop()
        self.assertEqual(result, 3)

    def test_top_operation(self):
        """
        Test whether i can view top element or not.
        Tests are devided in 2 senarios 
        
        1) top from an empty stack ------> should return UNDEFLOW
        2) top from filled stack

        will checked the popped element and result stack
        """
        empty_stack , filled_stack = [],[1,2,3]

        s = Stack()
        for each_element in empty_stack:
            print('PUSHING--->',each_element)
            s.push(each_element)

        result = s.top()
        self.assertEqual(result, 'UNDERFLOW')

        for each_element in filled_stack:
            print('PUSHING--->',each_element)
            s.push(each_element)

        result = s.top()
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()