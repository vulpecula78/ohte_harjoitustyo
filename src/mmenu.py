import pygame

BCKGRD = (55, 185, 75)
TITLE = (220, 205, 255)
TEXT = (190, 195, 255)
NBUTTON = (100, 100, 100)
HBUTTON = (175, 175, 175)

class Mmenu:
    '''Main menu for APC'''
    def __init__(self, scr_width, scr_height, screen):
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.screen = screen

    def menu(self):
        title_font = pygame.font.Font(pygame.font.match_font('arial'), 38)
        font = pygame.font.Font(pygame.font.match_font('arial'), 32)
        #height = self.scr_height
        width = self.scr_width

        #Menu texts
        title = title_font.render('Another Pong Clone Again', True, TITLE)
        game_type_1 = font.render('Player1 vs. Player2', True, TEXT)
        exit_game = font.render('Exit Game', True, TEXT)
        #Center texts
        title_rect = title.get_rect(center=(width/2, 100))
        game_type_1_rect = game_type_1.get_rect(center=(width/2, 200))
        exit_rect = exit_game.get_rect(center=(width/2, 300))

        #menu loop
        while True:
            mouse = pygame.mouse.get_pos()
            for action in pygame.event.get():
                if action.type == pygame.QUIT: # pylint: disable=no-member
                    return "quit"

                #mouse click on menu item
                if action.type == pygame.MOUSEBUTTONDOWN:   # pylint: disable=no-member
                    if width/2 - 220 < mouse[0] < width/2 + 220 and 180 < mouse[1] < 220:
                        return "PvP"
                    if width/2 - 220 < mouse[0] < width/2 + 220 and 280 < mouse[1] < 320:
                        return "quit"

            self.screen.fill((BCKGRD))

            #Highlight areas
            if width/2 - 220 <= mouse[0] <= width/2 + 220 and 180 <= mouse[1] <= 220:
                pygame.draw.rect(self.screen, HBUTTON, [width/2 - 220, 180, 440, 40])
            elif width/2 - 220 <= mouse[0] <= width/2 + 220 and 280 <= mouse[1] <= 320:
                pygame.draw.rect(self.screen, HBUTTON, [width/2 - 220, 280, 440, 40])

            #update screen
            self.screen.blit(title, title_rect)
            self.screen.blit(game_type_1, game_type_1_rect)
            self.screen.blit(exit_game, exit_rect)
            pygame.display.update()
