# Author : Maid SULTANOVIC
# This script will create a gitlab repository for you and it will save its URL in the clipboard
# It use gitlab API so you will have to change your private_token
# You will need gitlab module and pyperclip module
# Usage in cmd : python gitSync.py name [description]


import gitlab
import sys
import pyperclip


# change the private_token for ur purpose
gl = gitlab.Gitlab('https://gitlab.com/', private_token='putYourPrivateTokenHere')


def createProjet(pName, pDescription):
    try:
        project = gl.projects.create(
            {'name': pName, 'description': pDescription})
        return 0
    except:
        print("Unexcepted error ///")
        return 1


def urlGive(pName, pDescription):
    #Change to your gitlab's account
    url = "https://gitlab.com/YourGitLabAccount/" 
    if createProjet(pName, pDescription) == 0:
        url = url + str.lower(str(pName)) + ".git"

        print(url)
        pyperclip.copy(url)  # copy the git's url in clipboard
    else:
        print("Error project creation failed")


def projectList(pName):
    projects = gl.projects.list(search=pName, owned=True)
    projects = projects[0]
    gitUrl = projects.__getattr__("http_url_to_repo")
    print(gitUrl)
    pyperclip.copy(gitUrl)


if len(sys.argv) < 2:
    print("Error : You need to add project's name")
    print("Usage : python gitSync.py name [description]")
elif len(sys.argv) < 3:
    urlGive(str(sys.argv[1]), "")
else:

    if str(sys.argv[1]) == "1":
        projectList(str(sys.argv[2]))
    else:
        urlGive(str(sys.argv[1]), str(sys.argv[2]))
