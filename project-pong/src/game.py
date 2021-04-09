import pygame
import random
from wait import Wait

class Game():
    def __init__(self, FPS, render, score, ball, bat1, bat2, display, clock, scr_width, scr_height):
        self.FPS = FPS
        self.render = render
        self.bat1 = bat1
        self.bat2 = bat2
        self.ball = ball
        self.score = score
        self.display = display
        self.clock = clock
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.wait = Wait()
        self.running = True
        
        
    def launch(self, player):
        
        if player != 0:
            self.running = self.wait.wait(player)
        yVelocity = random.randint(-4, 5)
        xVelocity = random.randint(1, 5)
        
        if player == 0:
            if random.randint(1, 3) == 2:
                player = 2
                
        if player == 2:
            xVelocity = xVelocity * -1
            xpos = self.scr_width - 80
        else:
            xpos = 80
        
        ypos = random.randint(20, self.scr_height - 65)
        self.ball.setPosition(xpos, ypos)
        self.ball.setVelocity(xVelocity, yVelocity)
        
        
    def main(self):
        self.running = True
        p1_score = 0
        p2_score = 0
        self.launch(0)
        
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    self.bat1.moveUp()
                if keys[pygame.K_z]:
                    self.bat1.moveDown()
                if keys[pygame.K_UP]:
                    self.bat2.moveUp()
                if keys[pygame.K_DOWN]:
                    self.bat2.moveDown()            
                if event.type == pygame.QUIT:
                    self.running = False
                
            if pygame.sprite.collide_rect(self.ball, self.bat1) or pygame.sprite.collide_rect(self.ball, self.bat2):
                x = random.randint(0, 2)
                y = random.randint(-1, 2)
                xvel = self.ball.getXvelocity()
                yvel = self.ball.getYvelocity()
                if pygame.sprite.collide_rect(self.ball, self.bat1):
                    self.ball.setPosition(26, self.ball.rect.y)
                else:
                    self.ball.setPosition(self.scr_width - 66, self.ball.rect.y)
                    if -xvel + x == 0:
                        xvel = xvel + 1
                self.ball.setVelocity(-xvel + x, yvel + y)
                
            if self.ball.rect.x < -20:
                p2_score += 1
                self.launch(1)
                    
            if self.ball.rect.x > self.scr_width:
                p1_score += 1
                self.launch(2)
                
            self.ball.update()        
            self.render.update()
            self.score.scores(p1_score, p2_score)
            pygame.display.update()
