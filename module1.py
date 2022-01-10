import random

class Horse:
    def __init__(self, name, sp, hp, dist, rank=0, time=0):
      self.name = name
      self.sp = sp
      self.hp = hp
      self.dist = dist
      self.rank = rank
      self.time = time

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


HorseList = []
for i in range (1,15):
    HorseList.append(Horse(str(i),20,160,1200))

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

