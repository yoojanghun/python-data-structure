class Car:
    # 하나의 생성자, 두 개의 member method
    # 멤버 변수는 생성자 안에서 정의함. self. 가 붙어야 멤버 변수
    def __init__(self, color, speed = 0):
        # 자동차 객체가 가지고 있을 기본 특징
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    # 객체의 정보를 문자열로 표헌. 이거 없으면 그냥 객체가 메모리에 저장된 주소가 출력됨.
    def __str__(self):
        return "Color : %s, Speed : %d" %(self.color, self.speed)

if __name__ == "__main__":
    car1 = Car("black")
    car2 = Car("yellow", 10)
    car3 = Car("red", 100)

    print(car1)     # 객체가 저장되어 있는 메모리 주소
    print(car2)
    print(car3)

    car3.speedUp()
    print(car3)