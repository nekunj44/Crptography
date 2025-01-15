#ord - returns the ASCII value of the character
#chr - returns the character of the ASCII value

def main():
    a = input("enter the string: ")
    b = int(input("enter the key: "))
    d = ""
    for i in range(len(a)):
        if a[i].islower():
            c = chr(((ord(a[i]) + b) % 26) + 97)
            d += c
        elif a[i].isupper():
            c = chr(((ord(a[i]) + b) % 26) + 65)
            d += c
    print(d)

if __name__ == "__main__":
    main()