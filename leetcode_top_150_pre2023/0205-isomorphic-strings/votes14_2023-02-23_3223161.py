class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        if s[i] not in s_to_t and t[i] not in t_to_s:
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        elif s[i] in s_to_t and s_to_t[s[i]] == t[i]:
            continue
        else:
            return False
            
    return True