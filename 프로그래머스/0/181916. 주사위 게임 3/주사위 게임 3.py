def solution(a, b, c, d):
    from collections import Counter
    counts = Counter([a, b, c, d])

    nums = list(counts.keys())
    freq = list(counts.values())
    
    if len(counts) == 1:
        return 1111 * nums[0]
    
    if 3 in freq:
        p = nums[freq.index(3)]
        q = nums[freq.index(1)]
        return (10 * p + q) ** 2
    
    if len(counts) == 2 and freq[0] == freq[1] == 2:
        p, q = nums
        return (p + q) * abs(p - q)
    
    if 2 in freq:
        p = nums[freq.index(2)]
        q, r = [x for x in nums if x != p]
        return q * r
    
    return min(nums)