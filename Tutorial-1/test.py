def countSubset(str):
    l = []
    c = 0
    for s in str:
        if s in l:
            c = max(c,len(l))
            l.clear()
            l.append(s)
        else:
            l.append(s)
    return c

if __name__ == "__main__":
    str = "abcdabcb"
    print(countSubset(str))
    str = "ABDEFGABEF"
    print(countSubset(str))
