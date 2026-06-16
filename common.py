class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in "!?',;.": paragraph = paragraph.replace(i, " ")
        a=paragraph.lower().split()
        l=[]
        for i in a:
            if i not in banned:
                l.append(i)
        dic={}
        for word in l:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
        max=0
        words=""
        for word in dic:
            if dic[word]>max:
                max=dic[word]
                words=word
        return words




        