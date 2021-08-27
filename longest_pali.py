s = "babad"
#s = "aabbaa"
#s = "racecar"

if s == "":
    print("")

def searchPalindromic(s, left, right) -> int:
    if s is None or left > right:
        return 0
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1

start = 0
end = 0

for i in range(len(s)):
    max1 = searchPalindromic(s, i, i)
    max2 = searchPalindromic(s, i, i + 1)
    max_b = max(max1, max2)

    if max_b > (end - start):
        start = i - (max_b - 1) // 2
        end = i + max_b // 2

print(s[start:end + 1])
    
