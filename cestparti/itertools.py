from itertools import accumulate, takewhile

nums = list(accumulate(["a","b","c","d"]))
print(nums)
print(list(takewhile(lambda x: len(x)<= 3, nums)))
