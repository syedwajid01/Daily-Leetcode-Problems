class Solution(object):
    def movesToStamp(self, stamp, target):
        #reverse search all subarray that matching stamp
        #mark the matched subarry with '?'
        res = deque()
        move,maxmove = 0, 10*len(target)
        premove = 0
        while move < maxmove: #O(N), maximum check all element in target one by one
            premove = move
            for i in range(len(target)-len(stamp)+1): #O(N-S)
                substr = target[i:i+len(stamp)]
                if self.check(substr, stamp): #O(S) 
                    move += 1
                    res.appendleft(i)
                    target = target[:i] + '?'*len(stamp) + target[i+len(stamp):]  #update the target string when there is a match #O(N)
                    if target == "?"*len(target):
                        return res
            if premove == move:
                return []
        return res
        
    def check(self,substr, stamp):
        res = False
        for c1, c2 in zip(substr, stamp): 
            if c1 == c2:
                res = True
            elif c1 == '?': 
                continue #tricky part, we shouldn't put res = True here, because all "?" case will happen, they shouldn't be considered again
            else:
                return False
        return res