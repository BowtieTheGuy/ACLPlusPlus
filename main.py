#ACL++
#4 error messages
from pathlib import Path

def calc(i):
    if len(i) == 3:
        one = i[0][1]
        two = i[2][1]

        op = i[1][1]

        one_val = i[0][0]
        two_val = i[2][0]
        op_val = i[1][0]



        if one_val == "INT":
            if not two_val == "INT":
                print(f"ERROR1: Expected int to add with int, Not {two[1]}.")
                return


            if not op_val == "OP":
                print(f"ERROR3: Unexpected Operator '{op}'")
                return



            if op == "+":
                print(one + two)
            
            elif op == "-":
                print(one - two)
            
            elif op == "*":
                print(one * two)
            
            elif op == "/":
                if two == 0:
                    print("ERROR2: Cannot Divide By 0.")
                    return
                print(one / two)


def tokenize(i):
    tokens = []
    split = i.split()

    for word in split:
        try:
            tokens.append(("INT", int(word)))
        except ValueError:
            if word == "+" or word == "-" or word == "/" or word == "*":
                tokens.append(("OP", word))

            else:
                tokens.append(("STRING", word))

    return tokens


    


while True:
    i = input("> ")

    calc(tokenize(i))
