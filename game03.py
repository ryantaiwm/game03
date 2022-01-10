import pygame,sys,random

class Horse:
   def __init__(self, name, sp, hp):
      self.name = name
      self.sp = sp
      self.hp = hp

   def Ready(self):
      print(self.name)

pygame.init()#初始化操作
#儲存視窗大小
width,height=1024,768

h1 = Horse("Lucky",7,10)
h1.Ready()


screen=pygame.display.set_mode([width,height])#建立遊戲視窗

#設定視窗標題
pygame.display.set_caption("Snoopy")

#載入小鳥素材
player=pygame.image.load("horse.gif")
player2=pygame.image.load("horse.gif")
#獲取影象矩形位置
rect=player.get_rect()
rect2=player.get_rect()

#宣告XY運動速度的列表
speed = [random.randint(1,3),0]
speed2 = [random.randint(1,3),0]

left_head = pygame.transform.flip(player,True,False)
right_head = player
rect.left = 20
rect2.left = 10
rect.top = 100
rect2.top = 150
#無限迴圈
while True:
 for event in pygame.event.get():
  if event.type ==pygame.QUIT:
   exit()
  if event.type ==pygame.KEYDOWN:
   if event.key == pygame.K_LEFT:
    player = left_head #小鳥的頭向左
    speed=[-2,1]
   if event.key == pygame.K_RIGHT:
    player = right_head #小鳥的頭向左
    speed=[2,1]
   if event.key == pygame.K_UP:
    player = left_head #小鳥的頭向左
    speed=[2,-1]
   if event.key == pygame.K_DOWN:
    player = right_head #小鳥的頭向左
    speed=[2,1]
   if event.key == pygame.K_q:
    exit()

 rect =rect.move(speed)
 rect2 = rect2.move(speed2)
 

 if rect.right>width or rect.left<0:
  #將圖片水平翻轉    反轉物件 是否水平反轉 是否垂直翻轉
  player = pygame.transform.flip(player,True,False)
  speed[0]=-speed[0]

 if rect.bottom>height or rect.top<0:
  speed[1]=-speed[1]

 #screen.fill((255,255,255))
 screen.fill((0,128,0))
 screen.blit(player,rect)
 screen.blit(player2,rect2)
 pygame.display.update()
 pygame.time.delay(10)