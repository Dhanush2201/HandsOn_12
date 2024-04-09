class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        if not 0 <= k < self.size:
            raise IndexError('Index out of bounds!')
        return self.array[k]

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_cap):
        new_array = self.make_array(new_cap)
        for k in range(self.size):
            new_array[k] = self.array[k]
        self.array = new_array
        self.capacity = new_cap

    @staticmethod
    def make_array(new_cap):
        return (new_cap * ctypes.py_object)()

import ctypes

# Example usage
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(13)
    arr.append(3)
    arr.append(5)
    arr.append(31)
    arr.append(15)
    print("Array length:", len(arr))
    print("Element at index 0:", arr[0])
    print("Element at index 1:", arr[1])
    print("Element at index 2:", arr[2])
    print("Element at index 3:", arr[3])
    print("Element at index 4:", arr[4])