import pygame, random
pygame.init()  #pygame初始化

# 創建顏色(三個參數為RGB)
GREEN = (0,255,0) # 綠色
RED = (255,0,0) # 紅色
BLUE = (0,0,255) # 藍色
WHITE = (255,255,255) # 白色
BLACK = (0,0,0) # 黑色
YELLOW = (255,255,0) #黃色

class Ball(pygame.sprite.Sprite):  #球體角色
 
    # 參數為「球速」、「球x,y座標」、「半徑」、「球顏色」
    def __init__(self, sp, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.color = color
        self.image = pygame.Surface([radium*2, radium*2])  #繪製球體
        self.image.fill(BLACK) # 畫布背景同背景色
        pygame.draw.circle(self.image, self.color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)  #初始位置
 
    def update(self):  #球體移動
        self.rect.y += self.speed # 改變球的位置


# 設定視窗
width, height = 640, 320
screen = pygame.display.set_mode((width, height))  #建立繪圖視窗
pygame.display.set_caption("基本架構")  #繪圖視窗標題

#建立畫布 (書上說通常不會直接在繪圖視窗畫圖)
background = pygame.Surface(screen.get_size())  
background = background.convert() #為畫布建立副本，加快顯示速度
background.fill(BLACK)  #畫布為黑色(三個參數為RGB)

#建立全部角色群組
allsprite = pygame.sprite.Group()  

# 遊戲主要無窮迴圈
clock = pygame.time.Clock() #重要，計時物件
running = True
while running:  #無窮迴圈
    clock.tick(30)  #每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #使用者按右上角的關閉鈕
            running = False
    
    # 隨機添加雪球
    a = random.randint(1,3) #random which color
    sz = random.randint(1,5) #random which size and speed
    if a == 1:
     ball = Ball(sz, random.randint(0,screen.get_width()), 0, sz+5, WHITE)  #建立白色球物件
    if a == 2:
     ball = Ball(sz, random.randint(0,screen.get_width()), 0, sz+5, RED)  #建立白色球物件
    if a == 3:
     ball = Ball(sz, random.randint(0,screen.get_width()), 0, sz+5, BLUE)  #建立白色球物件
    allsprite.add(ball)  #加入全部角色群組
    
    screen.blit(background, (0,0))  #在繪圖視窗繪製畫布
    # 更新所有角色的狀態
    for spr in allsprite:
        spr.update()
    allsprite.draw(screen)  #繪製所有角色
    pygame.display.update()  #更新繪圖視窗
    
pygame.quit()  #關閉繪圖視窗