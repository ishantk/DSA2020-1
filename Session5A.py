# 8   ->  1 0 0 0

def binary(num):

    if num == 0:
        return

    binary(num//2)

    print(num % 2, end=" ")


binary(8)

