import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=600
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("tower.png").convert_alpha()
images["ghost"] = pygame.image.load("ghost-standing.png").convert_alpha()
images["window"] = pygame.image.load("door.png").convert_alpha()
groundy=-50

score=0
score_font=pygame.font.Font('freesansbold.ttf', 25)

class Ghost:
    speed=10
    g=0.3
    rect= pygame.Rect(270,250,50,80)
   
    def gravity(self):
        self.speed=self.speed+self.g
        self.rect.y= self.rect.y + self.speed

            
    def moveLeft(self):
        self.rect.x-=30
   
    def moveRight(self):
        self.rect.x+=25
    def jump(self):
        self.speed=-9
        

    def display(self):
        pygame.draw.rect(screen,(25,190,170),self.rect)
        
class Window:
   
    def __init__(self,y): 
        self.speed=5
        self.gap=random.randint(100, 400)
        self.rect1=pygame.Rect(self.gap,y+100,40,120)
        self.rect2=pygame.Rect(self.gap,y+240,100,5)
        
    def display(self):  
        screen.blit(images["window"],self.rect1)
       
    def move(self):
        self.rect1.y+=self.speed
        self.rect2.y+=self.speed
        if(self.rect1.y>600):
            self.rect1.y =-200
            self.rect2.y=-80
            self.rect1.x=random.randint(200, 600)
            self.rect2.x=self.rect1.x

          

state="play"
ghost= Ghost()

w1=Window(-200) 
w2=Window(-500)     
while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg"],[0,groundy])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ghost.moveLeft()
            if event.key == pygame.K_RIGHT:
                ghost.moveRight()
            if event.key == pygame.K_SPACE:
                ghost.jump()
    w1.move()
    w2.move()
    w1.display()
    w2.display()
        
    
    ghost.gravity()
    ghost.display()
    
    if state=="over":
        over_text=score_font.render("Game Over", False, (255,255,0))  
        screen.blit(over_text,[230,250]) 
    
        screen.blit()
    

    pygame.display.update() 
    clock.tick(30) 
    
    
    
    

 
