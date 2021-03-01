class Player():
    def __init__(self,playername,playerage,playercountry,noofmatch,noofruns,noofwick):    # the constructor init method with the attributes
        self.playername=playername
        self.playerage=playerage
        self.playercountry=playercountry
        self.noofmatch=noofmatch
        self.noofruns=noofruns
        self.noofwickets=noofwickets

    

class Team():                            # second class Team

    def __init__(self,l):
        self.l=l
    
    def getMinruns(self,l):                           # first method name, it will return the details of the player with the minimum runs
        x=[]
        
        for i in self.l:
            x.append(i.noofruns)                       # creating a list and finding the minimum element from it

        
        m=min(x)
        for i in self.l:
            if(i.noofruns==m):
                print(i.playername)                     # displaying player details who has the least runs
                print(i.noofruns)
                print(i.playercountry)

    def getMaxWickets(self,l):                       # second method, it will return the details of the player with the maximum wickets
        y=[]
        
        for i in self.l:
            y.append(i.noofwickets)

    
        n=max(y)
        for i in self.l:
            if(i.noofwickets==n):               # displaying the player details who has the most wickets
                print(i.playername)
                print(i.noofwickets)
                print(i.playercountry)
    

if __name__=='__main__':                              # the main function
    x=int(input())
    playername=''
    playercountry=''
    playerage=0
    noofmatch=0
    noofruns=0
    noofwickets=0
    l=[]                                      # l is the list of player objects
    
    for i in range(x):
        playername=input()
        playercountry=input()
        playerage=int(input())
        noofmatch=int(input())
        noofruns=int(input())
        noofwickets=int(input())
        p1=Player(playername,playerage,playercountry,noofmatch,noofruns,noofwickets)               # we append the details of the player along with the player object
        l.append(p1)                                            # we append the list of player objects to a list 'l'
    
    
    p2=Team(l)                        # we make object of second class and call the methods to get the output
    p2.getMinruns(l)
    p2.getMaxWickets(l)
