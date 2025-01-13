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

    
    print("JEG PRØVER Å FÅ DETTE TIL Å FUNKE")


def skibid_calc_2(third_num:float):
    return third_num

def skibid_calc_3(um:float):
    print("Skibidi pop pop", skibid_calc_2(um)*68, "number of cho")

    
TALL1, OP, TALL2=map(str,input("Skriv inn et regnestykke").split())
print(skibidi_calc(float(TALL1),OP, float(TALL2)))
