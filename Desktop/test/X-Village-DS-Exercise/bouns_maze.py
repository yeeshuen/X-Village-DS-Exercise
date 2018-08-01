#references
#https://openhome.cc/Gossip/AlgorithmGossip/MouseGoMaze.htm#Python
#https://github.com/Bryukh/labyrinth-algorithms
#http://bryukh.com/labyrinth-algorithms/

class mapp:
    def set_map(self,n):
        self.a = []
        self.size = n
        for i in range(n):
            self.a.append([0]*n)
            
    def set_pattern(self,p):
        if p == 1 and self.size == 10:
            for i in range(10):
                self.a[0][i]=8
                self.a[9][i]=8
                self.a[i][0]=8
                self.a[i][9]=8
                
            self.a[1][6]=8
            self.a[2][1]=8
            self.a[2][3]=8
            self.a[2][4]=8
            self.a[2][5]=8
            self.a[2][7]=8
            self.a[3][1]=8
            self.a[4][1]=8
            self.a[4][2]=8
            self.a[4][3]=8
            self.a[4][4]=8
            self.a[4][5]=8
            self.a[4][6]=8
            self.a[4][7]=8
            self.a[5][1]=8
            self.a[5][3]=8
            self.a[5][7]=8
            self.a[6][1]=8
            self.a[6][5]=8
            self.a[7][3]=8
            self.a[7][4]=8
            self.a[7][5]=8
            self.a[7][7]=8
            self.a[8][2]=8
            
    def movchoice(self,nox,noy):
        keepmov = True
        while keepmov:
            if not(nox == 8 and noy == 1):
                choi = [self.a[nox+1][noy],self.a[nox][noy+1],self.a[nox-1][noy],self.a[nox][noy-1]]
                choi.remove(8)
                c = choi.index(max(choi))
                self.a[nox][noy] -= 1 
                if c == 0:
                    nox = nox+1
                    noy = noy
                elif c == 1:
                    nox = nox
                    noy = noy+1
                elif c == 2:
                    nox = nox-1
                    noy = noy
                elif c == 3:
                    nox = nox
                    noy = noy-1
                RouteHistory.append([nox,noy])
            else:
                print("escape")
                keepmov = False
            
            self.display()
        
            
    
    def display(self):
        for i in range(self.size):
            print(self.a[i])
        print("="*120)

RouteHistory = [[1,1]]
            
mymap = mapp()
mymap.set_map(10)
mymap.set_pattern(1)
mymap.movchoice(1,1)

print(RouteHistory)