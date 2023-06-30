class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:      
            list1 = []
            list1[:0] = s
            for i in t:
                if i not in list1:
                    return False      
                list1.remove(i)
            return True          