size=3
class Board():
    def __init__(self) -> None:
        self.data=[['' for _ in range(size)] for _ in range(size)]
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            self.index=0
            raise StopIteration
        result=self.data[self.index]
        self.index+=1
        return result
    def copy(self,other):
        for i in range(size):
            for j in range(size):
                other.data[i][j]=self.data[i][j]
    def win_check_m(self):
        if self.data[0][0]==self.data[1][1] and self.data[1][1]==self.data[2][2] and self.data[1][1]!='':
            return [True,self.data[0][0]]
        elif self.data[1][0]==self.data[1][1] and self.data[1][0]==self.data[1][2] and self.data[1][1]!='':
            return [True,self.data[1][0]]
        elif self.data[2][0]==self.data[2][1] and self.data[2][0]==self.data[2][2] and self.data[2][0]!='':
            return [True,self.data[2][0]]
        elif self.data[0][0]==self.data[1][0] and self.data[0][0]==self.data[2][0] and self.data[0][0]!='':
            return [True,self.data[0][0]]
        elif self.data[0][1]==self.data[1][1] and self.data[0][1]==self.data[2][1] and self.data[2][1]!='':
            return [True,self.data[1][1]]
        elif self.data[0][2]==self.data[1][2] and self.data[1][2]==self.data[2][2] and self.data[2][2]!='':
            return [True,self.data[1][2]]
        elif self.data[0][2]==self.data[1][1] and self.data[1][1]==self.data[2][0] and self.data[1][1]!='':
            return [True,self.data[1][1]]
        elif self.data[0][0]==self.data[0][1] and self.data[0][1]==self.data[0][2] and self.data[0][1]!='':
            return [True,self.data[0][1]]
        return [False,""]
    def tie_check_m(self):
        cc=self.win_check_m()
        if not cc[0]:
            for i in self:
                for j in i:
                    if j=='':
                        return False
        return True
                    
    
    
    
    