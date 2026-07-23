#ACL++
#3 error messages


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



while True:
    i = input("> ")

    calc(i)
