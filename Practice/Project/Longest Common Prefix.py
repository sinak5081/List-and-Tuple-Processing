def longest(word):
    first_word = word[0]
    PerFix = ""
    for i in range(len(first_word)):
        char = first_word[i]
        for w in word[1:]:
            if i >= len(w) or w[i] != char:
                return PerFix
        else:
            PerFix += char
    return PerFix

word = ["flower", "flow", "flight"]
print(longest(word))