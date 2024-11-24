class Solution:
    def isPalindrome(_self, s: str) -> bool:
        news=""
        for i in s:
            if i.isalnum():
                news += i.lower()
        i=0
        j=len(news)-1
        while i < j:
            if news[i] != news[j]:
                return False
            i+=1
            j-=1
        return True  