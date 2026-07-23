#ACL++
#4 error messages
from pathlib import Path

def calc(i):
    split = i.split()

    if len(split) == 3:
        try:
            one = int(split[0])
            try:
                two = int(split[2])

                op = split[1]


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
                print(f"ERROR2: Expected int, Not {split[2]}")


        except ValueError:
            print(f"ERROR2: Expected int, Not {split[0]}.")


    else:
        print(f"ERROR1: Expected 3 Thingies, Not {len(split)}.")

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

    calc(i)
