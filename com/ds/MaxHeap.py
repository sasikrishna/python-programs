

class MaxHeap:
    def __init__(self):
        self.max_heap = []
        self.heap_index = -1
        pass

    def insert(self, key):
        self.heap_index += 1
        self.max_heap.append(key)

        current = self.heap_index
        parent = MaxHeap.get_parent(current)
        while self.max_heap[current] > self.max_heap[parent]:
            self.swap_keys(current, parent)
            current = MaxHeap.get_parent(current)
            parent = MaxHeap.get_parent(current)

            if current == parent:
                break

    def get_max(self):
        return None if self.heap_index < 0 else self.max_heap[0]

    def extract_max(self):
        if self.heap_index < 0:
            return None

        max = self.max_heap[0]
        self.max_heap[0] = self.max_heap[self.heap_index]
        del self.max_heap[self.heap_index]
        self.heap_index -= 1
        self.heapify(0)
        return max

    def heapify(self, index):

        if index < 0 or index > self.heap_index:
            return

        max_index = index
        left_child = MaxHeap.get_left_child(index)
        if left_child > -1 and left_child <= self.heap_index and self.max_heap[max_index] < self.max_heap[left_child]:
            max_index = left_child

        right_child = MaxHeap.get_right_child(index)
        if right_child > -1 and right_child <= self.heap_index and self.max_heap[max_index] < self.max_heap[right_child]:
            max_index = right_child

        if index == max_index:
            return

        self.swap_keys(index, max_index)
        self.heapify(max_index)

    def swap_keys(self, index1, index2):
        key1 = self.max_heap[index1]
        self.max_heap[index1] = self.max_heap[index2]
        self.max_heap[index2] = key1

    def get_parent(index):
        return 0 if index == 0 else int((index - 1)/2)

    def get_left_child(index):
        return 2 * index + 1

    def get_right_child(index):
        return 2 * index + 2


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(30)
    max_heap.insert(40)
    max_heap.insert(50)
    print(max_heap.max_heap)
    print('Max element is ', max_heap.get_max())
    print('Extracted max element is ', max_heap.extract_max())
    print('Max element is ', max_heap.get_max())
    print(max_heap.max_heap)
    print('Extracted max element is ', max_heap.extract_max())
    print('Max element is ', max_heap.get_max())
    print(max_heap.max_heap)
    print('Extracted max element is ', max_heap.extract_max())
    print('Max element is ', max_heap.get_max())
    print(max_heap.max_heap)
    max_heap.insert(50)
    print('Max element is ', max_heap.get_max())
    print(max_heap.max_heap)
