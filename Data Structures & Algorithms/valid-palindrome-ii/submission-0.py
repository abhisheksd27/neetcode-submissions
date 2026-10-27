class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                skipl,skipr=s[l+1:r+1] ,s[l:r]
                if skipl==skipl[::-1] or skipr==skipr[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True