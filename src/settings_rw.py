import os

dirname = os.path.dirname(__file__)

class SettingsRW:
    '''Reads and writes setup file
    setup is a list: [screen_width, screen_height, sounds, ai level,
    small screen hiscore, medium screen hiscore, large screen hiscore].
    If setup fi does not exist, default setup will be written.
    Default = [800, 600, False, "easy", 0, 0 ,0] is given by main.py.
    '''
    def __init__(self, file):
        '''Initializes SettingsRW.

        Args: file, filename of the file to be handled.
        '''
        self.settings_file = file

    def load_settings(self, setup):
        """Loads settings from apca_settings.txt or filename given file. If file doesn't exist,
        it will be created with default values from setup.

        Args:
            setup: List of default values. These will be used,
            if apca_settings.txt not exists.

        Returns:
            lsetup: list of game settings
        """
        try:
            game_setup_file = os.path.join(dirname, self.settings_file)
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
        except FileNotFoundError:
            lsetup = self.write_settings(setup)
        return lsetup

    #Write file.
    def write_settings(self, setup):
        """Writes setting into apca_settings.txt file.

        Args:
            setup: list of values to be written into a file.

        Returns:
            setup: list of setup values.
        """
        game_setup_file = os.path.join(dirname, self.settings_file)
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
