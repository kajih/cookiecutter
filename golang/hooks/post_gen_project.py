"""
Does the following:
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)


def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]

    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file(".gitignore")
