
def convert(s: str, numRows: int) -> str:
    zigzag = ["" for i in range(0, numRows)]
    
    s_length = len(s)
    idx = 0   # in dex for input string
    i = 0   # index for zigzag map
    while(idx < s_length):
        zigzag[i] += s[idx]
        i += 1
        idx += 1
        # adding element in reverse order
        if i == numRows and idx < s_length:
            for k in range(i-2, 0, -1):
                if idx == s_length:
                    break
                zigzag[k] += s[idx]
                idx += 1
            i = 0  # further start adding character from begin
    
    ans = ""
    # combine all the zigzag strings
    for item in zigzag:
        ans += item
    return ans


result = convert("ABCDE", 4)
print(result)
