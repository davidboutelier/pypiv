"""
Documentation for entire pypiv module
"""

def printlog(message):
    # check if log.txt exist
    # if does not exist create log.txt
    # print message in both display and log file

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

            print('Parameters in the configuration file: ')
            for key in config.keys():
                print(key + ': ' + config[key])

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

        print(name)
