# Elias, hevet knyttneve du

def skibidi_calc(first_num:float,operator:str,second_num:float):
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '/':
        return first_num / second_num
    else:
        return 'Invalid operator, do it again skibidi pop pop'