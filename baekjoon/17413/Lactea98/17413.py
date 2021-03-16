from sys import stdin

input_data = stdin.readline().strip()

def printReverse(input_data):
    input_data = list(map(lambda x : x[::-1], input_data.split(" ")))
    print(" ".join(input_data), end="")

while True:
    if input_data.find("<") != -1:
        print(input_data[input_data.find("<") : input_data.find(">")+1], end="")
        input_data = input_data[input_data.find(">")+1 : ]
        
        if input_data.find("<") != -1:
            printReverse(input_data[ : input_data.find("<")])
            input_data = input_data[input_data.find("<") : ]
        else:
            input_data = input_data[ : len(input_data)]
            printReverse(input_data)
            break
    else:
        printReverse(input_data)
        break