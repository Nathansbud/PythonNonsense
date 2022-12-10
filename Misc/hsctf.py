from PIL import Image

def text2numbers():
    input_numbers = (23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19)
    flag_str = "".join([" " if n == 27 else "_" if n == 28 else chr(n+64) for n in input_numbers])
    print("".join([f for f in flag_str.split(" ") if "_" in f]))

def fibonacci():
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a+b

def appended_fibonacci_sum():
    s = {0:"1"}
    for i, num in enumerate(fibonacci()):
        if i < 49: s[i+1]=s[i]+str(num)
        else: break
    print(str(sum([int(v) for v in s.values()]))[-9:])



if __name__ == "__main__":
    #Crypto 100 - text2numbers
    text2numbers()
    #Solution: SECRETS_ARE_HIDDEN_IN_THE_LIST
    #Algo 100 - Appended Fibonacci Sum
    appended_fibonacci_sum()
    ##Solution: 313056018
    """Forensics 100 - Competition Hype"""
    #Textbox on page can be copied, revealing "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm_go_to_youdidit_on_this_site_mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
    #Going to https://sites.google.com/site/practicehsctf/youdidit reveals key;
    #Solution: "FEEL THE HYPE! HYPE! HYPEHYPEHYPE!"
    # img = Image.open("/Users/zackamiton/Desktop/test.jpg")
    # print(img._getexif())






