from listByFunction import isEmpty


class ArrayList:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1

        else:
            pass


    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else:pass

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def replace(self, pos, e):
        if not self.isEmpty() and 0 <= pos < self.size:
            self.array[pos] = e

        else:
            print("Invalid Position or array is empty")

    def __str__(self):
        return str(self.array[0:self.size])