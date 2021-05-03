import os

dirname = os.path.dirname(__file__)

class Settings_rw:
    '''Reads and writes setup file
    setup is a list: [screen_width, screen_height, sounds, ai level,
    small scr hi, mid scr hi, large scr hi].
    If setup fi does not exist, default setup will be written.
    Default = [800, 600, False, "easy", 0, 0 ,0] is given by main.py.
    '''

    def load_settings(self, setup):
        try:
            game_setup_file = os.path.join(dirname, "apca_settings.txt")
            with open(game_setup_file) as game_setup:
                i = 0
                lsetup = []
                for line in game_setup:
                    line = line.replace("\n", "")
                    if i % 2 != 0: #only every second line
                        lsetup.append(line)
                    i = i + 1
                if i < 14:
                    lsetup = self.write_settings(setup)
        except:
            lsetup = self.write_settings(setup)
        return lsetup

    #Write file.
    def write_settings(self, setup):
        game_setup_file = os.path.join(dirname, "apca_settings.txt")
        game_setup = open(game_setup_file, "w")
        game_setup.write("screen width: \n")
        game_setup.write(str(setup[0]))
        game_setup.write("\nscreen height: \n")
        game_setup.write(str(setup[1]))
        game_setup.write("\nsounds: \n")
        game_setup.write(str(setup[2]))
        game_setup.write("\nai level: \n")
        game_setup.write(str(setup[3]))
        game_setup.write("\nhiscore in small screen: \n")
        game_setup.write(str(setup[4]))
        game_setup.write("\nhiscore in medium screen: \n")
        game_setup.write(str(setup[5]))
        game_setup.write("\nhiscore in large screen: \n")
        game_setup.write(str(setup[6]))
        game_setup.write("\n")
        game_setup.close()
        return setup
