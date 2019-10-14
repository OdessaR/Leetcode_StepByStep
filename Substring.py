#Substring study

a_string = "0123456789"
print("Original string:", a_string)

substr1 = a_string [4:17]
print("Substring:", substr1)

substr2 = a_string[1:7:2]
print("Substring with 2 steps:", substr2)

slice_string = "The slice object to get substring"
obj_slice = slice(3,17,1)
print("Original string:", slice_string)
print("Sliced substring with slice(3,17,1):", slice_string[obj_slice])

#---------------------#

#Longest substring without repeating characters

#1. Bruteforce: runtime exceeded
#list all substrings and compare lenth.
o_string = "pwwkew"
def UniqueString(string):
    i = 0
    tmp_string = {}
    sub_string = {}

    for i in range(len(string)):
        tmp_string = string[i]
        sub_string = string[i+1:len(string)]
        if tmp_string in sub_string:
            return False
    return True    

start = 0
end = 1
count_substring_lenth = 0

for start in range(len(o_string)+1) :
    for end in range(len(o_string)+1):
        end = end +1
        substr = o_string[start: end]   
        if substr:
            if UniqueString(substr):
                if count_substring_lenth < len(substr):
                  count_substring_lenth = len(substr)
    start = start+1

print(count_substring_lenth)