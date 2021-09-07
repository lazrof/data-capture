import operator
from collections import deque

class DataCapture:
    items = deque()
    hash = {}
    builded_items = None
    is_builded = False

    __not_ready_error_msg = "Can't instantiate greater, less or between methods before build_stats method"
    __bad_format_error_msg = "greater, less and between only allow arguments that you have entered with add"

    def add(self, num:int):
        '''
        Using deque.add() to accomplish a O(1) Complexity.
        '''
        
        if num < 0  or num > 1000:
            raise ValueError("DataCapture Object only allows positive integers, max value 1000")

        if self.builded_items is not None:
            raise TypeError("Can't add numbers after build_stats method is called")
        
        self.items.append(num)

        return num
    
    def greater(self, num):
        '''
        This method get his data from a dictionary created in the method build_stats. It required that the parameter num have been provided
        from the add method. Complexity O(1)
        '''
        self.validate_implementation()

        try:
            result = self.hash[num]
        except KeyError:
            raise BadFormat(self.__bad_format_error_msg)
            
        return result
    
    def less(self, num):
        '''
        This method get his data from a dictionary created in the method build_stats. It required that the parameter num have been provided
        from the add method. Complexity O(1)
        '''
        self.validate_implementation()

        try:
            result = self.hash[-num]
        except KeyError:
            raise BadFormat(self.__bad_format_error_msg)
            
        return result

    def between(self, num1:int, num2:int):

        '''
        This method get his data from a dictionary created in the method build_stats. It required that the parameters num1 and num2 have been provided
        from the add method. Complexity O(1)
        '''

        self.validate_implementation()

        result = []
        
        if num1 == num2:
            return result

        init, end = self._order_between_args(num1, num2)

        try:
            init_set = self.hash[init]
            end_set = self.hash[-end]
        except KeyError:
            raise BadFormat(self.__bad_format_error_msg)

        return init_set & end_set
    
    def greater_expensive(self, num:int):
        '''
        This method validates the data using a for loop. Complexity O(N)
        '''

        self.validate_implementation()
        result = self._get_numbers(num, 'greater')
        return result

    def less_expensive(self, num:int):
        '''
        This method validates the data using a for loop. Complexity O(N)
        '''

        self.validate_implementation()
        result = self._get_numbers(num, 'less')
        return result

    def _get_numbers(self, num:int, compare_verb:str):
        
        result = []
        compare_operator = lambda num1, num2: operator.lt(num1,num2) \
            if compare_verb == 'less' \
            else lambda num1, num2:operator.gt(num1,num2)

        for i in self.builded_items:
            #if i > num:
            if compare_operator(i, num):
                result.append(i)

        return result

    
    def _order_between_args(self, num1, num2):
        
        init = num1
        end = num2
        if num1 > num2:
            init = num2
            end = num1
        
        return init, end


    def between_expensive(self, num1:int, num2:int):
        '''
        This method validates the data using a for loop. Complexity O(N)
        '''
        
        self.validate_implementation()
        
        result = [] 
        if num1 == num2:
            return result

        init = num1
        end = num2
        if num1 > num2:
            init = num2
            end = num1        

        for i in self.builded_items:

            if i >= init and i <= end:
                result.append(i)

        return result
        

    def build_stats(self):

        '''
        This method creates a dictionary loading the data provided from the add method. This data can be accessed in a complexity of O(1) 
        in greater() and less() methods.
        '''

        self.builded_items = [x for x in self.items]
        self.builded_items.sort()

        negative_index = -1
        for i, current in enumerate(self.builded_items):
            num_oposite = self.builded_items[negative_index]

            self.hash[current] = set(self.builded_items[i+1:])
            self.hash[-num_oposite] = set(self.builded_items[:negative_index])

            negative_index -= 1

        self.is_builded = True

        return self.builded_items


    def validate_implementation(self):
        if self.builded_items == None:
            raise NotImplementedError(self.__not_ready_error_msg)

    
class BadFormat(Exception):
    pass
