#ACL++
#4 error messages
from pathlib import Path

def calc(i):

    if len(i) == 3:
        try:
            one = int(i[0].split()[1])
            try:
                two = int(i[2].split()[1])

                op = i[1].split()[1]


                if op == "+":
                    print(one + two)

                elif op == "-":
                    print(one - two)

                elif op == "*":
                    print(one * two)

                elif op == "/":
                    if two == 0:
                        print("ERROR3: Cannot Divide By 0.")
                    else:
                        print(one / two)
                else:
                    print(f"ERROR4: Unexpected Operator '{op}'")


            except ValueError:
                print(f"ERROR2: Expected int, Not {i[2].split()[1]}.")


        except ValueError:
            print(f"ERROR2: Expected int, Not {i[0].split()[1]}.")


    else:
        print(f"ERROR1: Expected 3 Thingies, Not {len(i)}.")

def tokenize(i):
    tokens = []
    split = i.split()

    for word in split:
        try:
            tokens.append(f"INT: {int(word)}")
        except ValueError:
            if word == "+" or word == "-" or word == "/" or word == "*":
                tokens.append(f"OP: {word}")

            else:
                tokens.append(f"STRING: {word}")

    return tokens


    


while True:
    i = input("> ")

    calc(tokenize(i))
