# chapter 1 exercise 1 
# function that checks if all chars in a string are unique 
# linear time and linear space 
# O(n), O(m)

def unique_string(string):
    char_set = set()
    char_set_size = len(char_set)
    for char in string:
        char_set.add(char)
        new_set_len = len(char_set)
        if(new_set_len > char_set_size):
            char_set_size = new_set_len
        else:
            return False
    return True

# part 2
# do it without data structures 
# O(n*logn) + O(n)
# sorting should take log time 
# sort the string then use exor to check if the current and
# last string are the same 
 
def unique_string_mem(string):
    startval = 0 
    lastval = 0
    sorted_string = sorted(string)
    for char in sorted_string:
        value = ord(char)
        temp_val = lastval ^ value
        if temp_val == 0:
            return False
        lastval = temp_val
    return True
    


print unique_string("adfafage")
print unique_string("ohman")
print unique_string_mem("adfafage")
print unique_string_mem("ohman")