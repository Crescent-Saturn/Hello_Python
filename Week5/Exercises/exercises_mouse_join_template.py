# String list joining problem

###################################################
# Student should enter code below
#f = ""
def string_list_join(s):
    global f
    f = ""
    for i in s:
        f += i
    return f


###################################################
# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd
