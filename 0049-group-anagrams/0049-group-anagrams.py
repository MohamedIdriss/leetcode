class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 :
            return [[strs[0]]]
        else:
            anagram_groups = defaultdict(list)
    
            for word in strs:
  
                sorted_word = ''.join(sorted(word))
        
                anagram_groups[sorted_word].append(word)
    
            result = list(anagram_groups.values())
    
            return result
        