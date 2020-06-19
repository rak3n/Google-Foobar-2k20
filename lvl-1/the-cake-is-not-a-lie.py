def solution(s):
    # Your code here
    ans=''
    for i in range(len(s)):
        ans+=s[i]
        j=i+1
        while j<len(s):
            if ans==s[j:j+len(ans)]:
                j+=len(ans)
            else:
                break
        if j>=len(s):
            break

    print(s.count(ans))

solution("abcabcabcabc")
