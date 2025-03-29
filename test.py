L1 = [1,2,3]
L2 = [1,2,3]
L3 = L1
# L1이 가리키는 객체의 값과 L2가 가리키는 객체의 값이 같나?
print(L1 == L2)     # True
print(L1 == L3)     # True

# is는 L1과 L2의 객체 주소가 같은 지 물어보는 연산자
print(L1 is L2)     # False
print(L1 is L3)     # True

psw = input("Enter your psw: ____\b\b\b\b")