# Stage 5/5: Saving memory

messages = {'msg_0': "Enter an equation",
            'msg_1': "Do you even know what numbers are? Stay focused!",
            'msg_2': "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            'msg_3': "Yeah... division by zero. Smart move...",
            'msg_4': "Do you want to store the result? (y / n):",
            'msg_5': "Do you want to continue calculations? (y / n):",
            'msg_6': " ... lazy",
            'msg_7': " ... very lazy",
            'msg_8': " ... very, very lazy",
            'msg_9': "You are",
            'msg_10': "Are you sure? It is only one digit! (y / n)",
            'msg_11': "Don't be silly! It's just one number! Add to the memory? (y / n)",
            'msg_12': "Last chance! Do you really want to embarrass yourself? (y / n)"}


# check if value is a float
def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


# check if the number is one digit
def is_one_digit(v):
    return - 10 < v < 10 and v.is_integer()


# laziness test function
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages[f'msg_{6}']
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg = msg + messages[f'msg_{7}']
    if (v1 == 0 or v2 == 0) and v3 in ['*', '+', '-']:
        msg = msg + messages[f'msg_{8}']
    if msg != "":
        msg = messages[f'msg_{9}'] + msg
        print(msg)


memory = 0
result = 0

while True:
    print(messages[f'msg_{0}'])
    x, operator, y = input().split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    if not isfloat(x) or not isfloat(y):
        print(messages[f'msg_{1}'])
        continue
    else:
        if operator in ['+', '-', '*', '/']:
            check(float(x), float(y), operator)
            if operator == '+':
                result = float(x) + float(y)
            elif operator == '-':
                result = float(x) - float(y)
            elif operator == '*':
                result = float(x) * float(y)
            elif operator == '/':
                try:
                    result = float(x) / float(y)
                except ZeroDivisionError:
                    print(messages[f'msg_{3}'])
                    continue
            print(result)
            print(messages[f'msg_{4}'])
            answer = input()
            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(messages[f'msg_{msg_index}'])
                        answer = input()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                    print(messages[f'msg_{5}'])
                    answer = input()
                    if answer == 'y':
                        continue
                    if answer == 'n':
                        break
                memory = result
                print(messages[f'msg_{5}'])
                answer = input()
                if answer == 'y':
                    continue
                if answer == 'n':
                    break
            if answer == 'n':
                print(messages[f'msg_{5}'])
                answer = input()
                if answer == 'y':
                    continue
                if answer == 'n':
                    break
        else:
            print(messages[f'msg_{2}'])
            continue
