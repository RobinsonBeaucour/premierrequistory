import re

#pattern = r"pam"
#
#match = re.search(pattern, "eggspamsausage")
#if match:
#    print(match.group())
#    print(match.start())
#    print(match.end())
#    print(match.span())

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy",num,) #remplace pattern par Amy
print(newstr)
