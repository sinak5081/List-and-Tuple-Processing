def validation(code, businessLine, isActive):
    n = len(code)
    validCode = []
    allowedCategories = {"electronics", "grocery", "pharmacy", "restaurant"}
    
    for i in range(n):
        if not isActive[i]:
            continue
        if businessLine[i] not in allowedCategories:
            continue
        if code[i] == "":
            continue
        
        valid = True
        for c in code[i]:
            if not (c.isalnum() or c == '_'):
                valid = False
                break
        
        if not valid:
            continue
        
        validCode.append(code[i])
    
    if not validCode:
        output = ""
    else:
        output = ",".join(validCode)
    
    return output
codes = ["ABC_1", "B-2", "C_3"]
businessLines = ["electronics", "grocery", "pharmacy"]
isActives = [True, True, True]
result = validation(codes, businessLines, isActives)
print(result)

