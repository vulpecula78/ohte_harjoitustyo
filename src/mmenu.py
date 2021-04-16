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
        mid = self.scr_width / 2

        #menu item y locations
        item_1 = self.scr_height / 4
        item_2 = self.scr_height / 4 + 50
        item_3 = self.scr_height / 4 + 100

        #Menu texts
        title = title_font.render('Another Pong Clone Again', True, TITLE)
        game_type_1 = font.render('Player1 vs. Player2', True, TEXT)
        game_type_2 = font.render('Player1  vs. computer', True, TEXT)
        exit_game = font.render('Exit Game', True, TEXT)
        #Center texts
        title_rect = title.get_rect(center=(mid, self.scr_height / 8))
        game_type_1_rect = game_type_1.get_rect(center=(mid, item_1))
        game_type_2_rect = game_type_2.get_rect(center=(mid, item_2))
        exit_rect = exit_game.get_rect(center=(mid, item_3))

        #menu loop
        while True:
            mouse = pygame.mouse.get_pos()
            for action in pygame.event.get():
                if action.type == pygame.QUIT: # pylint: disable=no-member
                    return "quit"

                #mouse click on menu item
                if action.type == pygame.MOUSEBUTTONDOWN:   # pylint: disable=no-member
                    if mid - 220 < mouse[0] < mid + 220 and item_1 - 20 < mouse[1] < item_1 + 20:
                        return "PvP"
                    if mid - 220 < mouse[0] < mid + 220 and item_2 < mouse[1] < item_2 + 40:
                        return "computer"
                    if mid - 220 < mouse[0] < mid + 220 and item_3 < mouse[1] < item_3 + 40:
                        return "quit"

            self.screen.fill((BCKGRD))

            #Highlight areas
            if mid - 220 <= mouse[0] <= mid + 220 and item_1 - 20 <= mouse[1] <= item_1 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_1 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_2 - 20 <= mouse[1] <= item_2 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_2 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_3 - 20 <= mouse[1] <= item_3 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_3 - 20, 440, 40])

            #update screen
            self.screen.blit(title, title_rect)
            self.screen.blit(game_type_1, game_type_1_rect)
            self.screen.blit(game_type_2, game_type_2_rect)
            self.screen.blit(exit_game, exit_rect)
            pygame.display.update()
