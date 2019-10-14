s = "abcabcbb"

str_list = []
max_length = 0
for x in s:
    if x in str_list:
        print(x)
        print(str_list.index(x))
        str_list = str_list[str_list.index(x)+1:]
        print(str_list)
    
    str_list.append(x)
    print(str_list)
    max_length = max(max_length, len(str_list))
