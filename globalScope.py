pi = 3.141592
perimeter = 0                       # 전역 변수

def calc_perimeter(radius):
    # global perimeter              # 이 코드 사용하면 전역 변수를 함수 안에서도 읽기 쓰기 모두 가능
    print("Pi :", pi)               # 전역 변수 값을 읽을 수 있다
    perimeter = 2 * pi * radius
    print(perimeter)                # 지역 변수는 들여쓰기 안 공간에만 적용. perimeter는 함수 안 지역변수임.

calc_perimeter(10)
print(perimeter)                    # 0으로 출력됨. 전역 변수를 함수 안에서 update 못함