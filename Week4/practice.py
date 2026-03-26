import ctypes
import time
index = int

class MyVector():
    """ 일반적으로 Python에서는  Class내의 메소드들은 이름을 PEP8을 준용한다.
    클래스의 경우에는 CamelClass 로 ex) MyVector, MyList
    메소드의 경우에는 snake_case 로 ex) insert_at_rank, remove_at_rank
    함수는 snake_case 로 ex) my_function, calculate_sum
    """
    def __init__(self, capacity=1):
        self._n = 0
        self._capacity = capacity
        self._A = self._make_array(self._capacity)
        
    def __str__(self):
        """ Return string representation of the list.
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> print(my_list)
        [10, 20]
        """
        if self._n == 0:
            return "[]"
        else:
            result = "["
            for i in range(self._n):
                result += str(self._A[i]) + ", "
            result = result[:-2] + "]"
            return result
    
    def __len__(self):
        """ Return number of elements stored in the list.
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> len(my_list)
        2
        """
        return self._n
    
    def __getitem__(self, i:index)->ctypes.py_object:
        """elementAt Algorithm
        Usae:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> my_list[1]
        20
        >>> my_list[4]
        IndexError: Index out of bounds
        """
        if i < 0 or i >= self._n:
            raise IndexError("Index out of bounds")
        return self._A[i]
    
    def __setitem__(self, i:index, value:ctypes.py_object):
        """Refer replaceAt Algorithm
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> my_list[1] = 25
        >>> my_list[1]
        25
        >>> my_list[3] = 20
        IndexError: Index out of bounds
        """
        if i < 0 or i >= self._n:
            raise IndexError("Index out of bounds")
        self._A[i] = value
    
    def _make_array(self, c:int)->ctypes.Array:
        """Allocates an array of size c."""
        return (c * ctypes.py_object)()
    
    def _resize(self, c:int):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        
        for k in range(self._n):
            B[k] = self._A[k]
            
        self._A = B
        self._capacity = c
            
    def insert_at_rank(self, i:index, value:ctypes.py_object):
        """ Inserts the element at index i in the list.
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> my_list.insert_at_rank(1, 15)
        >>> my_list
        [10, 15, 20]"""
 
    def remove_at_rank(self, r:index):
        """ Removes and returns the element at index i in the list.
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> my_list.remove_at_rank(0)
        10
        >>> my_list
        [20]
        """
    
    def replace_at_rank(self, i:index, value:ctypes.py_object):
        """ Replaces the element at index i in the list with a new value.
        Usage:
        >>> my_list = MyVector()
        >>> my_list.append(10)
        >>> my_list.append(20)
        >>> my_list.replace_at_rank(0, 15)
        10
        >>> my_list
        [15, 20]
        """

    
    def append(self, value:ctypes.py_object):
        """insertLast Algorithm
        Usage:
        >>> my_vector = MyVector()
        >>> my_vector.append(10)
        >>> my_vector.append(20)
        >>> my_vector
        [10, 20]
        """
    
if __name__ == "__main__":
    import random
    
    print("1. MyVector append Test")
    my_vector = MyVector()
    start=time.time()
    for i in range(5):
        my_vector.append(random.randint(1, 100))
    my_vector.append("404")
    my_vector.append("not found")
    my_vector.append("system")
    my_vector.append("404 new")
    my_vector.append("era era")
    end=time.time()
    print(f"Time taken: {end - start} seconds")
    
    print("\n2. MyVector elementAt Test")
    for i in range(len(my_vector)):
        print(f"Element at index {i}: {my_vector[i]}")
    
    print("\n2. MyVector insert_at_rank Test")
    my_vector.insert_at_rank(2, "삽입삽입")
    print(my_vector)
    
    my_vector.insert_at_rank(2, "Inserted")
    print(my_vector)
    
    print("\n3. MyVector replace_at_rank Test")
    my_vector.replace_at_rank(2, "Replaced")
    print(my_vector)
    
    print("\n4. MyVector remove_at_rank Test")
    removed_value = my_vector.remove_at_rank(0)
    print(removed_value) 
    print(my_vector)  

    print(my_vector)