def solution(code):
    mode = 0
    ret =""
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                ret += code[i]
            elif code[i] == '1':
                mode = 1 - mode
        elif mode == 1:
            if code[i] != '1' and i % 2 != 0:
                ret += code[i]
            elif code[i] == '1':
                mode = 1 - mode
    if not ret :
        ret = "EMPTY"
    return ret