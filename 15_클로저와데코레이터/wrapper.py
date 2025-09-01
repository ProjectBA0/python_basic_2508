def mul(m):
    def wrapper(n):
        return m * n
    
if __name__ == '__main__':

    mul3 = Mul(3)
    mul5 = Mul(5)
    mul10 = Mul(10)

    #print(mul3.mul(10))
    #print(mul5.mul(10))
    #print(mul10.mul(10))  call 함수사용시 mul함수 호출 불필요

    print(mul3(10))
    print(mul5(10))
    print(mul10(10))