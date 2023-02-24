if __name__ == "__main__":
    base = 2
    summand = 0

    for num in range(0, 12):
        sum = 0
        i = 2
        digit = num
        while digit > 0:
            sum += (digit % base) / i
            digit //= base
            i *= base

        print(sum)





    # for digit in range(5):
    #     sum = 0
    #     i = 2     
    #     while digit > 0:
    #         sum += (digit % 2) * i
    #         digit //= base
    #         i *= 2

    #     print(sum / i if sum else 0)

        
