import random

def find_min_max(A):
    min = max = A[0]

    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]

    return (min, max)       # 소괄호는 생략 가능. 튜플의 형식으로 반환


if __name__ == "__main__":          # if 실행시키는 파일이 지금 현재 파일이라면. import한 파일에서 실행시키면 아래 코드는 실행 안됨.
    A = []
    for _ in range(10):
        A.append(random.randint(1,100))

    print(A)
    print(find_min_max(A)) 