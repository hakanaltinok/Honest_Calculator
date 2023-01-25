# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0

result = 0.0


def get_input():
    print(msg_0)
    calc = input()
    return calc.strip().split()


def is_one_digit(num):
    return 0 == (num - int(num)) and -10 < num < 10


def check(v1, v2, v3):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 in ["*", "+", "-"]:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_num(num):
    try:
        nm = int(num)
    except ValueError:
        try:
            nm = float(num)
        except ValueError:
            return False
        else:
            return True
    else:
        return True


error = True

while error:
    lst = get_input()
    x = lst[0]
    oper = lst[1]
    y = lst[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if not is_num(x) or not is_num(y):
        print(msg_1)
        error = True
    else:
        x = float(x)
        y = float(y)
        if not (oper in ["+", "-", "*", "/"]):
            print(msg_2)
            error = True
        else:
            check(x, y, oper)
            if oper == "+":
                result = x + y
                error = False
            elif oper == "-":
                result = x - y
                error = False
            elif oper == "*":
                result = x * y
                error = False
            elif oper == "/" and y != 0:
                result = x / y
                error = False
            else:
                print(msg_3)
                error = True
    if not error:
        print(result)
        readable_response = False
        while not readable_response: # save to memory
            print(msg_4)
            save_to_mem = input()
            if save_to_mem == "y":
                if is_one_digit(result):
                    msg_index = 10
                    loop = True
                    while loop:
                        msg = "print(msg_" + str(msg_index) + ")"
                        eval(msg)
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index += 1
                                loop = True
                            else:
                                loop = False
                                memory = result
                                readable_response = True
                        elif answer == "n":
                            loop = False
                            #memory = 0.0
                            readable_response = True
                        else:
                            loop = True
                else:
                    memory = result
                    readable_response = True
            elif save_to_mem == "n":
                #memory = 0.0
                readable_response = True
        readable_response = False
        while not readable_response:
            print(msg_5)
            recalculate = input()
            if recalculate == "y":
                error = True
                readable_response = True
            elif recalculate == "n":
                readable_response = True
