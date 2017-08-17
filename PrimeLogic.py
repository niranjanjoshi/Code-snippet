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
