class miss:
    def find(self,l):
        self.l = l
        self.m = max(self.l)
        self.n = (self.m*(self.m+1))/2
        print(int(self.n-sum(l)))
obj = miss()
obj.find([int(i) for i in input().split()])
