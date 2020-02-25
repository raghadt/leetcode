from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec = Counter(secret)
        gu = Counter(guess)

        bull=0
        cow=0
        # print(gu)
        for i in range(len(guess)):

            if guess[i]==secret[i]:
                bull+=1

        for i in range(len(guess)):    
            if gu[guess[i]]!=0 and guess[i] in sec.keys() and sec[guess[i]]>0:
                cow+=1
                sec[guess[i]]-=1
        #         print(sec)



        return ("{}A{}B".format(bull, cow-bull))