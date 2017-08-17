import math

def is_prime(num):
    if (num<=1):
        return False
    if(num == 2):
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(num))+1):
            if (num % i == 0):
                return False
        else:
            return True

def sumOfDigits(num):
    tot=0
    while(num>0):
        dig=num%10
        tot=tot+dig
        num=num//10
    return tot

def sumOfSquaresDigits(num):
    tot = 0
    while (num > 0):
        dig = num % 10
        tot = tot + dig*dig
        num = num // 10
    return tot

if __name__ == '__main__':
    test_cases = int(input())
    storage = []
    for i in range(0,test_cases):
        numLow,numHigh =  [int(x) for x in input().split()]
        lucky_count = 0
        for j in range (numLow,numHigh):
            sum  = sumOfDigits(j)
            if(is_prime(sum)):
                squareSum = sumOfSquaresDigits(j)
                if(is_prime(squareSum)):
                    #print('The lucky number is : ',j)
                    lucky_count = lucky_count + 1
        storage.append(lucky_count)
    for num in storage:
        print(num)
