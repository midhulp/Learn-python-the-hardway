import unittest


def freq(s):

    tcount={}

    for i in s:
        if i not in tcount:
            tcount[i]=1
        else:
            tcount[i]+=1

    return tcount

s='aaabbdyhgfguuu'
print(freq(s))

class Testfreq(unittest.TestCase):
    def test_freq(self):
        if __name__ == '__main__':
            unittest.main()

  
    
    


