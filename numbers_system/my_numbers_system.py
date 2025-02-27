def binari_octal_hex(num):
    return bin(num)[2:], oct(num)[2:], hex(num)[2:].upper()


number = int(input())
result = binari_octal_hex(number)
print(*result, sep="\n")
