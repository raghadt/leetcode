class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-','')
        len_S = len(S)
        st=''
        
        if len_S%K==0:
            for i in range(0, len_S, K):
                st+= '-' + S[i: i+K]
            return (st[1:].upper())

        else:
            st = S[0:len_S%K]
            for i in range(len_S%K, len_S, K):
                st+= '-' + S[i: i+K]
            return (st.upper())    
    
        