class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str1=""
        for i in s:
            if i.isalnum():
                str1+=i.lower()

        i=0
        j=len(str1)-1

        while i<=j:
            if str1[i] !=str1[j]:
                return False
            i+=1
            j-=1
        return True