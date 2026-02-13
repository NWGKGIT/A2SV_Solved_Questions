def restoreString(s, indices):
    res=[0]*len(s)
    for i in range(len(s)):
        res[indices[i]]=s[i]
    return "".join(res)

