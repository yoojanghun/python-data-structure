capacity = 100
size = 0
array = [None] * capacity

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1

    else:
        print("Overflow or Invalid Position")


def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i+1]

        size -= 1
        return e
    else: 
        print("Underflow or Invalid Position")

#def getEntry(pos):
    def __str__(self):
        return str(self.array[0:self.size])


if __name__ == "__main__":

    L = ArrayList(50)
    L.insert(0, "A")
    L.insert(1, "B")
    L.insert(1, "C")
    print(L)
