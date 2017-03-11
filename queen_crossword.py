import random
class Vezir :
    def __init__(self):
        self.str = random.randint(0, 7)
        self.stn=stn = random.randint(0, 7)
        self.alan=[]
    def FirstQueen(self):
        # alan=[["*" for i in range(8)]for i in range(8) ]
        print (self.str, self.stn)
        for i in range(8):
            self.alan.append([])
        for j in self.alan:
            for k in range(8):
                j.append(1)
        for l in range(8):
            for t in range(8):
                if l == self.str and t == self.stn:
                    self.alan[l][t] = 0
        for s in self.alan:
            print (s)
    def QueenMove(self):
        satir=self.str
        sutun=self.stn
        degis=[0,2,4,6,3,1,5,7]
        q=0
        change=satir
        while(q<=len(degis)):

            if satir==degis[q]:
                p=q+1
                t=sutun+1
                while(t<=len(self.alan[0])):
                    if t==8:
                        t=0
                    while(p<=len(degis)):

                        if(p==8):
                            p=0
                        elif(t==8):
                            t=0
                        elif(change==degis[p]):
                            break
                        else:

                            satir=degis[p]
                            sutun=t
                            self.alan[satir][sutun]=0
                            p = p + 1
                            t = t + 1
                    break
                break

            else:
                q=q+1

        for c in self.alan:
            print (c)

if __name__ =='__main__':
    queen=Vezir()
    queen.FirstQueen()
    print ("############################\n")
    print("ilk vezir yerlestiii!!\n")
    queen.QueenMove()
    print ("###########################\n")
    print ("8 Vezir Basariyla Yerlestirildi!!!")











