import pygame
from settings_rw import SettingsRW

BCKGRD = (55, 185, 75)
TITLE = (255, 215, 55)
TEXT = (190, 195, 255)
HBUTTON = (175, 185, 175)

class Mmenu:
    '''Main menu for APC'''
    def __init__(self, scr_width, scr_height, screen):
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.screen = screen
        self.title_font = pygame.font.Font(pygame.font.match_font('arial'), 38)
        self.font = pygame.font.Font(pygame.font.match_font('arial'), 32)
        self.middle = self.scr_width / 2
        self.setupfile = SettingsRW()

    def menu(self, lsetup):
        mid = self.middle

        #menu item y locations
        item_1 = self.scr_height / 4
        item_2 = self.scr_height / 4 + 50
        item_3 = self.scr_height / 4 + 100
        item_4 = self.scr_height / 4 + 180
        item_5 = self.scr_height / 4 + 230

        #Menu texts
        title = self.title_font.render('Another Pong Clone Again', True, TITLE)
        game_type_1 = self.font.render('Player1 vs. Player2', True, TEXT)
        game_type_2 = self.font.render('Player1  vs. computer', True, TEXT)
        game_type_3 = self.font.render('Against the wall', True, TEXT)
        settings = self.font.render('Settings', True, TEXT)
        exit_game = self.font.render('Exit Game', True, TEXT)

        #Center texts
        title_rect = title.get_rect(center=(mid, self.scr_height / 8))
        game_type_1_rect = game_type_1.get_rect(center=(mid, item_1))
        game_type_2_rect = game_type_2.get_rect(center=(mid, item_2))
        game_type_3_rect = game_type_3.get_rect(center=(mid, item_3))
        settings_rect = settings.get_rect(center=(mid, item_4))
        exit_rect = exit_game.get_rect(center=(mid, item_5))

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
                    if mid - 220 < mouse[0] < mid + 220 and item_2 - 20 < mouse[1] < item_2 + 20:
                        return "computer"
                    if mid - 220 < mouse[0] < mid + 220 and item_3 - 20 < mouse[1] < item_3 + 20:
                        return "wall"
                    if mid - 220 < mouse[0] < mid + 220 and item_4 - 20 < mouse[1] < item_4 + 20:
                        self._settings(lsetup)
                        return "settings"
                    if mid - 220 < mouse[0] < mid + 220 and item_5 - 20 < mouse[1] < item_5 + 20:
                        return "quit"

            self.screen.fill((BCKGRD))

            #Highlight areas
            if mid - 220 <= mouse[0] <= mid + 220 and item_1 - 20 <= mouse[1] <= item_1 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_1 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_2 - 20 <= mouse[1] <= item_2 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_2 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_3 - 20 <= mouse[1] <= item_3 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_3 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_4 - 20 <= mouse[1] <= item_4 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_4 - 20, 440, 40])
            elif mid - 220 <= mouse[0] <= mid + 220 and item_5 - 20 <= mouse[1] <= item_5 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, item_5 - 20, 440, 40])

            #update screen
            self.screen.blit(title, title_rect)
            self.screen.blit(game_type_1, game_type_1_rect)
            self.screen.blit(game_type_2, game_type_2_rect)
            self.screen.blit(game_type_3, game_type_3_rect)
            self.screen.blit(settings, settings_rect)
            self.screen.blit(exit_game, exit_rect)
            pygame.display.update()

    def _settings(self, lsetup):
        mid = self.middle
        #Setting menu items y locations
        sett1 = self.scr_height / 4
        sett2 = self.scr_height / 4 + 50
        sett3 = self.scr_height / 4 + 100
        sett5 = self.scr_height / 4 + 220

        #Settings texts
        soundeff = self.font.render('Sound effects: ON / OFF', True, TEXT)
        scrnsize = self.font.render('Screen size: Small / Med / Large', True, TEXT)
        ai_level = self.font.render('Computer Level: Easy / Average' ,True, TEXT)
        back_to_main = self.font.render('Return to main menu', True, TEXT)

        #center texts
        setting1_rect = soundeff.get_rect(center=(mid, sett1))
        setting2_rect = scrnsize.get_rect(center=(mid, sett2))
        setting3_rect = ai_level.get_rect(center=(mid, sett3))
        setting5_rect = back_to_main.get_rect(center=(mid, sett5))

        while True:
            mouse = pygame.mouse.get_pos()
            for action in pygame.event.get():

                if action.type == pygame.MOUSEBUTTONDOWN:   # pylint: disable=no-member
                    if mid + 50 < mouse[0] < mid + 100 and sett1 - 20 < mouse[1] < sett1 + 20:
                        lsetup[2] = "True"
                    if mid + 130 < mouse[0] < mid + 190 and sett1 - 20 < mouse[1] < sett1 + 20:
                        lsetup[2] = "False"
                    if mid - 55 < mouse[0] < mid + 40 and sett2 -20 < mouse[1] < sett2 + 20:
                        lsetup[0] = "640"
                        lsetup[1] = "480"
                    if mid + 70 < mouse[0] < mid + 140 and sett2 -20 < mouse[1] < sett2 + 20:
                        lsetup[0] = "800"
                        lsetup[1] = "600"
                    if mid + 160 < mouse[0] < mid + 260 and sett2 -20 < mouse[1] < sett2 + 20:
                        lsetup[0] = "1024"
                        lsetup[1] = "768"
                    if mid + 15 < mouse[0] < mid + 100 and sett3 -20 < mouse[1] < sett3 + 20:
                        lsetup[3] = "easy"
                    if mid + 125 < mouse[0] < mid + 255 and sett3 -20 < mouse[1] < sett3 + 20:
                        lsetup[3] = "average"
                    if mid - 220 < mouse[0] < mid + 220 and sett5 - 20 < mouse[1] < sett5 + 20:
                        self.setupfile.write_settings(lsetup)
                        return #  and write new settings into settings file

            self.screen.fill((BCKGRD))

            #Highlight settings:
            #Sound setting on / off
            if mid + 50 <= mouse[0] <= mid + 100 and sett1 - 20 <= mouse[1] <= sett1 + 20 or lsetup[2] == "True":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 50, sett1 - 20, 50, 40]) # on
            if mid + 130 <= mouse[0] <= mid + 190 and sett1 - 20 <= mouse[1] <= sett1 + 20 or lsetup[2] == "False":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 130, sett1 - 20, 60, 40]) # off
            #Screen Size
            if mid - 55 <= mouse[0] <= mid + 40 and sett2 - 20 <= mouse[1] <= sett2 + 20 or lsetup[0] == "640":
                pygame.draw.rect(self.screen, HBUTTON, [mid - 55, sett2 - 20, 95, 40])
            if mid + 70 <= mouse[0] <= mid + 140 and sett2 - 20 <= mouse[1] <= sett2 + 20 or lsetup[0] == "800":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 70, sett2 - 20, 70, 40])
            if mid + 160 <= mouse[0] <= mid + 260 and sett2 - 20 <= mouse[1] <= sett2 + 20 or lsetup[0] == "1024":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 160, sett2 - 20, 100, 40])
            #AI level
            if mid + 15 <= mouse[0] <= mid + 100 and sett3 - 20 <= mouse[1] <= sett3 + 20 or lsetup[3] == "easy":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 15, sett3 - 20, 85, 40]) # easy
            if mid + 125 <= mouse[0] <= mid + 255 and sett3 - 20 <= mouse[1] <= sett3 + 20 or lsetup[3] == "average":
                pygame.draw.rect(self.screen, HBUTTON, [mid + 125, sett3 - 20, 130, 40]) # average

            #Back to main menu
            if mid - 220 <= mouse[0] <= mid + 220 and sett5 - 20 <= mouse[1] <= sett5 + 20:
                pygame.draw.rect(self.screen, HBUTTON, [mid - 220, sett5 - 20, 440, 40])

            #update screen
            self.screen.blit(soundeff, setting1_rect)
            self.screen.blit(scrnsize, setting2_rect)
            self.screen.blit(ai_level, setting3_rect)
            self.screen.blit(back_to_main, setting5_rect)
            pygame.display.update()
