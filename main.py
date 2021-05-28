"""
Description of the main file here
"""


def print_hi():
    import os

    name = os.getlogin()
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import sources.pypiv as pp

    print_hi()

    # instantiate the config object
    config = pp.Config()

    # show the config parameters
    config.print()



    # instantiate the project object
    project = pp.Project()

    # create new project
    project.create(name='test')



