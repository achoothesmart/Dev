class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = ''
        s2 = ''
        if(len(str1) < len(str2)):
            s1 = str1
            s2 = str2
        else:
            s1 = str2
            s2 = str1
        if(s1 != s2[:len(s1)]):
            return ''
        while(s1 != ''):
            if(len(s2)//len(s1) == len(s2)/len(s1)):
                # if its a while number
                if(s1*(len(s2)//len(s1)) == s2):
                    return s1
                else:
                    s1 = s1[:-1] # removing last char
                # else:
                #     return 'x2 ' + str(len(s2)//len(s1)) + ' s1=' + s1 + ' s2=' + s2
            else:
                s1 = s1[:-1] # removing last char
        return s1
