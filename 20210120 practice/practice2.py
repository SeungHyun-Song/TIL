def string_middle(str):
    t = len(str) // 2
    return str[t] if len(str) % 2 else str[t -1 : t + 1]

print(string_middle('coding'))