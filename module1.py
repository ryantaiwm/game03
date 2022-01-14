import random

class Horse:
    def __init__(self, id, name, sp, hp, dist, rank=0, time=0):
      self.id = id
      self.name = name
      self.sp = sp
      self.hp = hp
      self.dist = dist
      self.rank = rank
      self.time = time
      self.score = 50
      self.rid = 0

    def Ready(self):
      print(self.name + " "+str(self.rank) + " Time: " + str(self.time))

    def SetDist(self, dist):
        self.dist = dist
    
    def Update(self):
        if self.dist >= 0:
            self.dist -= random.randint(1, self.sp)

    def Finish(self, rank, time):
        if self.rank == 0:
            self.rank = rank
            self.time = time


class fixture:
    def __init__ (self, rid):
        self.rid = rid
        self.dist = random.randint(1,5)*400 + 600
        self.score = random.randint(0,100)
        self.racelist = []

    def check(self, hid, score):
        # if full return 0
        if len(self.racelist) >= 14:
            return 0
        if self.score > score:
            return 0
        # if already existing return Rid    
        for h in self.racelist:
            if h == hid:
                return self.rid
        # otherwise app hid to racelist and reture Rid        
        self.racelist.append(hid)
        return self.rid

def SystemInit():
    AllHorseList = []
    for i in range (1,1000):
        AllHorseList.append(Horse(i,str(i),random.randint(3,7),100,1000))

    FixtureList = []
    for i in range(1,10):
        FixtureList.append(fixture(i))
    for f in FixtureList:
        for h in AllHorseList:
            if h.rid <= 0:
                rid = f.check(h.id, h.score)
                if rid != 0:
                    h.rid = rid
        print("Rid " + str(f.rid) +" Dist "+str(f.dist)+" Score "+str(f.score) + " " +str(len(f.racelist)))
        print(f.racelist)
    

def racing():
    HorseList = []
    for i in range (1,15):
        HorseList.append(Horse(i,str(i),20,160,2200)) 

    KeepGoing = True
    j = 0
    finished = 0
    while KeepGoing:
        j += 1
    #print(j)
    #for y in HorseList:
    #    y.Ready()

        for x in HorseList:
            x.Update()
            if x.dist <= 0:
                if x.rank == 0:
                    finished += 1
                    x.Finish(finished, j)
            
            if finished >= 14:
                KeepGoing = False

        # end of racing
        for x in HorseList:
            x.Ready()

SystemExit = False
while SystemExit == False:
    print("Simulation 2022")
    print("1 - System Init")
    print("2 - Racing")
    print("3 - Exit")
    choiceitem = int(input('option : '))
    if choiceitem == 1:
        SystemInit()
    if choiceitem == 2:
        racing()
    if choiceitem == 3:
        exit()
