"""
Documentation for entire pypiv module
"""


def print_log(message):
    """
    Print to screen and in log file
    :param message: a string to be displayed on screen and logged in the log file
    :return: None
    """
    import os

    if not os.path.isfile('log.txt'):
        os.mknod('log.txt')

    print(message)
    with open('log.txt', "a") as f:
        f.write(message + '\n')


class Config:
    """
    Doc for the config object
    """

    def __init__(self):
        import os
        import json

        if os.path.isfile('config.json'):
            with open('config.json', 'r') as fp:
                config = json.load(fp)
        else:
            here = os.getcwd()
            os.mkdir(os.path.join(here, 'piv'))
            sources = os.path.join(here, 'piv', 'sources')
            os.mkdir(sources)

            projects = os.path.join(here, 'piv', 'projects')
            os.mkdir(projects)

            config = {'pypiv': here, 'sources': sources, 'projects': projects}

            with open('config.json', 'w') as fp:
                json.dump(config, fp)

    def print(self):
        import os
        import json

        if os.path.isfile('config.json'):
            with open('config.json', 'r') as fp:
                config = json.load(fp)

            print_log('Parameters in the configuration file: ')
            for key in config.keys():
                print_log(key + ': ' + config[key])

    def save(self, config):
        import json
        with open('config.json', 'w') as fp:
            json.dump(config, fp)


class Project:

    def create(self, name):
        """
        Creates a new project and its directory
        :param name: name of the project to be created
        :return: None
        """
        import json
        import os

        # read the path to projects from config file

        print_log(name)
