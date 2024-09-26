# Sean A
# Dynamic Array Class
# Create a class that contains a dynamic array

import ctypes


class DynamicArray:
    def __init__(self):
        self.__n = 0
        self.__capacity = 1
        self.__A = self.__make_array(self.__capacity)

    def __make_array(self, c):
        """return new array with capacity c"""
        return (c * ctypes.py_object)()

    def __str__(self):
        if self.__n == 0:
            return "[]"

        out = '['
        for i, element in enumerate(self.__A):
            try:
                out += str(element) + ', '
                self.__A[i + 1]
            except:
                break
        return out[:-2] + ']'

    def __len__(self):
        return self.__n

    def __getitem__(self, k):
        """return element at index"""
        if k <= 0 or k >= self.__n:
            raise IndexError("invalid index")

        return self.__A[k]

    def __resize(self):
        self.__capacity *= 2
        newArray = self.__make_array(self.__capacity)
        for i, obj in enumerate(self.__A):
            newArray[i] = obj
        self.__A = newArray

    def append(self, element):
        if len(self) >= self.__capacity:
            self.__resize()
        self.__A[self.__n] = element
        self.__n += 1

    def get_cap(self):
        return self.__capacity
