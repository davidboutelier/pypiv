"""
Documentation for entire pypiv module
"""


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
