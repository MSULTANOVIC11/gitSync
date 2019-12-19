# Author : Maid SULTANOVIC
# This script will create a gitlab repository for you and it will save its URL in the clipboard
# It use gitlab API so you will have to change your private_token
# Usage in cmd : python gitSync.py [project's name] [project's description]


import gitlab
import sys
import pyperclip


# change the private_token for ur purpose
gl = gitlab.Gitlab('https://gitlab.com/', private_token='rbxzs2WK-vhBnFSRhbn3')


def createProjet(pName, pDescription):
    try:
        project = gl.projects.create(
            {'name': pName, 'description': pDescription})
        return 0
    except:
        print("Unexcepted error ///")
        return 1


def urlGive(pName, pDescription):
    url = "https://gitlab.com/MSD11/"
    if createProjet(pName, pDescription) == 0:
        url = url + str.lower(str(pName)) + ".git"

        print(url)
        pyperclip.copy(url)  # copy the git's url in clipboard
    else:
        print("Error project creation failed")


urlGive(str(sys.argv[1]), str(sys.argv[2]))
