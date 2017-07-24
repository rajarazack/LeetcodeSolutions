class Solution(object):
    def bigNumber(self, s):
        li =[]
        ss=s.__str__()
        big = ''
        big2=''
        for n in ss:
            li.append(n)
        li.sort(reverse=True)
        li2=li[:]
        length = len(li2)
        i = 1
        while True:
            li2[length-i],li2[length-(i+1)]=li2[length-(i+1)],li2[length-i]
            if li2[length-(i+1)] != li2[length-i]:
                break
            i = i+1
        for l,l2 in zip(li,li2):
            big = big+l
            big2 = big2+l2
        return int(big),int(big2)
if __name__ == '__main__':
    sol = Solution()
    print sol.bigNumber(122000)
