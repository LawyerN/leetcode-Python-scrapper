class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordcount={}
        for word in words:
            wordcount[word]=1+wordcount.get(word,0)
        result=[]
        substringlength=len(words)*len(words[0])
        for i in range(len(s)-substringlength+1):
            substr=s[i:i+substringlength]
            substrcount={}
            for j in range(0,len(substr),len(words[0])):
                word=substr[j:j+len(words[0])]
                substrcount[word]=1+substrcount.get(word,0)
            if substrcount==wordcount:
                result.append(i)
        return result

#         m=\'\'.join(words)
#         pcount=dict()
#         scount=dict()
#         if len(m)>len(s):
#             print([])
#         for i in range(len(m)):
#                  pcount[m[i]]=1+pcount.get(m[i],0)
#                  scount[s[i]]=1+scount.get(s[i],0)
# # print(pcount)
# # print(scount)
#         res=[0]if pcount==scount else []
#         l=0
#         for i in range(len(m),len(s),1):
#               scount[s[i]]=1+scount.get(s[i],0)
#               scount[s[l]]-=1 
#               if scount[s[l]]==0:
#                   del scount[s[l]]
#               l+=1 
#               if scount==pcount:
#                 res.append(l)
# #@print(res)
#         return res