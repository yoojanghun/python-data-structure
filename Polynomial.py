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

    def evaluate(self, x):  # ✅ 다항식 계산 기능 추가
        result = 0
        for i in range(self.degree + 1):
            result += self.coef[i] * (x ** i)  # 각 항 계산

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

    print("세 번째 다항식 입력")
    c = Poly()
    c.readPoly()
    x = int(input("미지수 x 값 입력: "))
    resultEvauluate = c.evaluate(x)
    print("결과는 %d 입니다" % resultEvauluate)