import pygame
from bat import Bat

def main():
    screen_width = 800
    screen_height = 600
    FPS = 100
    GREEN = (0, 255, 0)

    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("APCA")

    screen = pygame.display.set_mode((screen_width, screen_height))
    all_sprites = pygame.sprite.Group()

    bat1 = Bat(5, 300)
    bat2 = Bat(775, 300)
    
    all_sprites.add(bat1)
    all_sprites.add(bat2)
    
    screen.fill(GREEN)
    all_sprites.draw(screen)    

    pygame.display.flip()
    pygame.key.set_repeat(1, 2)
    running = True
    # main loop
    while running:
        clock.tick(FPS)
        #pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                bat1.moveUp()
            if keys[pygame.K_z]:
                bat1.moveDown()

            if keys[pygame.K_UP]:
                bat2.moveUp()
            if keys[pygame.K_DOWN]:
                bat2.moveDown()
                
                
            #all_sprites.update()
            screen.fill(GREEN)
            all_sprites.draw(screen)
            print(bat1.rect.x)
            pygame.display.flip()
            
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
    print("Hello World")

if __name__ == "__main__":
    main()
