# Program specification
"""
What is the decimal equivalent of 10011?
"""

number = input("Enter a binary number: ")
binary = ""

# reverse the sequence of the bits as we will start with the 2^e operations on the left most bit of the original number.
# build the reversed string and store in variable, binary.
for i in range(len(number)-1, -1, -1):
    binary += number[i]

# build the decimal equivalent
decimal = 0.0
for i in range(len(number)):
    decimal += int(binary[i]) * (2**i)


print(number, "decimal equivalent is", decimal)