'''
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
'''

def biggest (x):
    l = [str(_) for _ in x]
    r = len(max(l, key = len))
    u = [_+_*(r-len(_)) for _ in l]
    i = [_[0] for _ in sorted(enumerate(u), key=lambda x:x[1], reverse=True)]
    l = [l[_] for _ in i]
    ans = ''.join(l)
    ans = int (ans)

    return ans

'''
Official solution
'''

def get_largest_value(nums):
    nums = [str(x) for x in nums]
    length = len(max(nums, key=len))

    normalized = []
    for i, x in enumerate(nums):
        element = x * (length // len(x) + 1)
        normalized.append(element[:length])

    ordered = sorted(zip(nums, normalized), key=lambda x: x[1], reverse=True)

    return ''.join([x[0] for x in ordered])
