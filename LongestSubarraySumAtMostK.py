def LongestSubarraySumAtMostK(v, target):
    n = len(v)
    s=0
    res=0
    T = []
    for i in range(n):
        s+=v[i]
        if s<=target:
            res=i+1
        else:
            while i - res > 0 and T[i-res-1] >= s-target:
                res+=1
        if i == 0:
            T.append(s)
        else:
            T.append(max(T[i-1],s))
    return res
LongestSubarraySumAtMostK([5,-10,7,-20,57],-22)
