class Poly:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.degree = 0
        self.coef = [0] * capacity

    def readPoly(self):
        self.degree = int(input("다항식의 차수를 입력 : "))
        for i in range(self.degree, -1, -1):
            coef = int(input(" %d차 항의 계수 : " % i))
            self.coef[i] = coef

    def printPoly(self):
        for i in range(self.degree, 0, -1):
            print("%dx^%d + " % (self.coef[i], i), end="")
        print(self.coef[0])

    def addPoly(self, other):
        max_degree = max(self.degree, other.degree)
        result = Poly()
        result.degree = max_degree

        for i in range(max_degree + 1):
            result.coef[i] = self.coef[i] + other.coef[i]

        return result

if __name__ == "__main__":
    print("첫 번째 다항식 입력")
    a = Poly()
    a.readPoly()
    a.printPoly()

    print("두 번째 다항식 입력")
    b = Poly()
    b.readPoly()
    b.printPoly()

    print("첫번째와 두 번째 다항식 덧셈 결과")
    result = a.addPoly(b)
    result.printPoly()

