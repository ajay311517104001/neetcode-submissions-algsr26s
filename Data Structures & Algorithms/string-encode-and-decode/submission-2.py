class Solution:
    # attempt and understand after the mock
    def encode(self, strs: List[str]) -> str:
        encoded_str =  ''
        for s in strs:
            encoded_str+= str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # 5 # H e l l o 5 # W o  r  l  d
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13
        #                   i
        #  100#sfsadfsdfasdfas

        # iterate till end of the s length
        # get the length of the word
        # slice the word and add them to the result list
        result = []
        i =0 
        while i < len(s):
            str_len = ''

            while s[i]!='#':
                str_len += s[i]
                i+=1
            start = i+1
            end = i+int(str_len) +1
            result.append(s[start:end])

            i = i+int(str_len) +1
        return result



