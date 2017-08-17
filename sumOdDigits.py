def sumOfDigits(num):
    tot=0
    while(num>0):
        dig=num%10
        tot=tot+dig
        num=num//10
    return tot
