def first(str):
    for i in str:
        if str.count(i) == 1:
            return i
print(first('abbbvccaa'))