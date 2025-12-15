def roman_integer(roman_dict, roman_str):
    total = 0
    for i in range(len(roman_str)-1):
        current = roman_dict[roman_str[i]]
        next = roman_dict[roman_str[i+1]]
        if current < next:
            total -= current
        else:
            total += current
    total += roman_dict[roman_str[-1]]
    return total

roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
roman_str = "XIV"
print(roman_integer(roman_dict, roman_str))
