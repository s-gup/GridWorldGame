import random
import time
import os

grid=[]   #defines a list which will form grid. it will contain n lists so as to define each coordinate in a grid
#it will be in the form of [[],[],[]],each sublist contain n strings


class Grid():

    def __init__(self,N,start,goal,myObstacles,myRewards):
        self.N=N
        self.start=start
        self.goal=goal
        self.myObstacles=myObstacles
        self.myRewards=myRewards

    def showGrid(self):
        global grid
        grid=[]

        #define a grid with all "."
        for i in range(self.N):
            gridinsidelist=[]
            for j in range(self.N):

                gridinsidelist.append(" . ")
            grid.append(gridinsidelist)


        #to define placements of start,goal,obstacles and rewards in a grid

        #goal represented by "$""
        for i in range(self.N):
            for j in range(self.N):

                if (i,j)==self.goal:
                    grid[i][j]=" $ "
                #if (i,j)==(self.myObstacles[j].x,self.myObstacles[j].y):
                for a in self.myObstacles:
                    if (a.x,a.y)==(i,j):
                        grid[i][j]=" # "

                #if (i,j)==(self.myRewards[j].x,self.myRewards[j].y):
                for a in self.myRewards:
                    if (a.x,a.y)==(i,j):

                        grid[i][j]=" "+str(a.value)+" "

                if (i,j)==(playerobject.x,playerobject.y):
                    grid[i][j]=" O "



        # to print grid
        for i in range(self.N):
            for j in range(self.N):

                print(grid[i][j],end="")
            print()
    def rotateClockwise(self,n):
        #if after rotation the player’s position will coincide with that of an
#obstacle, you have to print a message saying that the grid can’t be rotated.
        global grid
#        changedgrid=[]
        for a in range(n):
            os.system('cls')
            k=0
            for m in self.myObstacles:

                m.x,m.y=m.y,self.N-1-m.x
                if (m.x,m.y)==(playerobject.x,playerobject.y):
                    k=1
            if k==1:


                print("grid cannot be rotated")
                for m in self.myObstacles:

                    m.x,m.y=self.N-1-m.y,m.x
                self.showGrid()
                playerobject.showenergy()
                return 0 #to end function call
            for n in self.myRewards:
                n.x,n.y=n.y,self.N-1-n.x
            playerobject.energy=playerobject.energy-(self.N//3)
            playerobject.showenergy()
            self.showGrid()

            time.sleep(0.5)

            #for i in range(self.N):
                #for j in range(self.N):
                    #changedgrid[i][j]=grid[self.N-1-j][i]
            #grid=changedgrid
    #if we make changes in original list then wrong result





    def rotateAnticlockwise(self,n):
        #if after rotation the player’s position will coincide with that of an
#obstacle, you have to print a message saying that the grid can’t be rotated.
        global grid
        for a in range(n):
            k=0
            os.system('cls')
            for m in self.myObstacles:
                m.x,m.y=self.N-1-m.y,m.x

                if (m.x,m.y)==(playerobject.x,playerobject.y):
                    k=1
            if k==1:


                print("grid cannot be rotated")
                for m in self.myObstacles:
                    m.x,m.y=m.y,self.N-1-m.x
                self.showGrid()
                playerobject.showenergy()
                return 0 #to end function call
            for n in self.myRewards:
                n.x,n.y=self.N-1-n.y,n.x
            playerobject.energy=playerobject.energy-(self.N//3)
            playerobject.showenergy()
            self.showGrid()

            time.sleep(0.5)




class Obstacle():
    def __init__(self,x,y):
        self.x=x
        self.y=y



class Reward():
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value


class Player():
    def __init__(self,x,y,energy):
        self.x=x
        self.y=y
        self.energy=energy


    #function to search the number of a move
    def searchnumber(self,s):
        n=""
        for i in range(len(s)):
            try:
                a=int(s[i])
                n=n+s[i]
            except:
                break
        return n

    def hitobstacle(self):
        if grid[self.x][self.y]==" # ":
            self.energy=self.energy-4*(gridobject.N)
    def consumenumber(self):
        try:
            a=int(grid[self.x][self.y][1])
            self.energy=self.energy+a*(gridobject.N)
            #to remove number after consuming
            for i in gridobject.myRewards:
                if i.x==self.x and i.y==self.y and i.value==a:
                    gridobject.myRewards.remove(i)
        except:
            pass
    def showenergy(self):
        print("energy",self.energy)
    def up(self,n):

        k=0
        while k<n:
            os.system('cls')
            if self.x==0:
                self.x=(gridobject.N)-1
            else:
                self.x=self.x-1
            k=k+1
            self.energy=self.energy-1
            self.hitobstacle()
            self.consumenumber()
            self.showenergy()
            gridobject.showGrid()

            time.sleep(0.5)


    def down(self,n):

        k=0
        while k<n:
            os.system('cls')
            if self.x==(gridobject.N)-1:
                self.x=0
            else:
                self.x=self.x+1
            k=k+1
            self.energy=self.energy-1
            self.hitobstacle()
            self.consumenumber()

            self.showenergy()
            gridobject.showGrid()
            time.sleep(0.5)


    def right(self,n):

        k=0
        while k<n:
            os.system('cls')
            if self.y==(gridobject.N)-1:
                self.y=0
            else:
                self.y=self.y+1
            k=k+1
            self.energy=self.energy-1
            self.hitobstacle()
            self.consumenumber()
            self.showenergy()
            gridobject.showGrid()

            time.sleep(0.5)



    def left(self,n):

        k=0
        while k<n:
            os.system('cls')
            if self.y==0:
                self.y=(gridobject.N)-1
            else:
                self.y=self.y-1
            k=k+1
            self.energy=self.energy-1
            self.hitobstacle()
            self.consumenumber()
            self.showenergy()
            gridobject.showGrid()
            time.sleep(0.5)



    def makeMove(self,s):
        for k in range(len(s)):
            try:
                a=int(s[k])   # if k is integer it will go to next iteration
                continue       #if  k is a string it will go to except condition
            except:
                n=int(self.searchnumber(s[k+1:]))
                if s[k]=="U":
                    self.up(n)
                if s[k]=="D":
                    self.down(n)

                if s[k]=="L":
                    self.left(n)
                if s[k]=="R":
                    self.right(n)
                if s[k]=="A":
                    gridobject.rotateAnticlockwise(n)
                if s[k]=="C":
                    gridobject.rotateClockwise(n)











os.system('cls')
N=int(input("enter grid size: "))

#generating start and goal position on boundary

start=(1,1)
while start[0]!=0 and start[0]!=N-1 and start[1]!=0 and start[1]!=N-1:
    start=(random.randrange(0,N),random.randrange(0,N))

goal=(1,1)
while goal[0]!=0 and goal[0]!=N-1 and goal[1]!=0 and goal[1]!=N-1 or goal==start:
    goal=(random.randrange(0,N),random.randrange(0,N))


#generating myObstacles
myObstacles=[]    # list of objects of type Obstacle
listobstacles=[]    #list of tuples containg (x,y) of each obstacle

a=0 #counter to produce n obstacles
while a<=N:

    x=random.randrange(0,N)
    y=random.randrange(0,N)
    if (x,y)!=goal and (x,y)!=start and (x,y) not in listobstacles:
        obstacleobject=Obstacle(x,y)
        myObstacles.append(obstacleobject)
        listobstacles.append((x,y))
        a=a+1


#generating myRewards
myRewards=[] # list of objects of type reward
listrewards=[] #list of tuples containg (x,y) of each obstacle
b=0
while b!=N :

    x=random.randrange(0,N)
    y=random.randrange(0,N)
    val=random.randrange(1,10)
    if (x,y)!=goal and (x,y)!=start and (x,y) not in listobstacles and (x,y) not in listrewards:
        rewardobject=Reward(x,y,val)
        listrewards.append((x,y))
        myRewards.append(rewardobject)
        b=b+1

#creating object of class Grid
gridobject=Grid(N,start,goal,myObstacles,myRewards)


playerobject=Player(gridobject.start[0],gridobject.start[1],2*N)
os.system('cls')
playerobject.showenergy()
gridobject.showGrid()

while playerobject.energy>0 and (playerobject.x,playerobject.y)!=gridobject.goal:
    move=input("enter next move : ")
    playerobject.makeMove(move)
