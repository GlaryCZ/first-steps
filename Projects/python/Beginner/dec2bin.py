def dec2bin(dec_num):
    if dec_num == 0:
        return 0
    guess = 1
    while guess*2 < dec_num:
        guess *= 2
    res = ""
    while guess != 0:
        if guess <= dec_num:
            dec_num -= guess
            res += "1"
        else:
            res += "0"
        guess //= 2
    return res


def bin2dec(bin_num):
    s = 1
    res = 0
    reversed_bin_num = bin_num[::-1]
    for bit in reversed_bin_num:
        if bit == "1":
            res += s
        elif bit == "0":
            pass
        else:
            return "Only characters '0' and '1' are allowed!"
        s *= 2
    return res


while True:
    n = input(" 1. From dec to bin\n 2. From bin to dec\n 3. Exit program\n >> ")
    if n == "1":
        res = dec2bin(int(input(" Enter a dec number\n >> ")))
        print(res)
    elif n == "2":
        res = bin2dec(input(" Enter a bin number\n >> "))
        print(res)
    elif n == "3":
        break
    else:
        print("Invalid input\n")
