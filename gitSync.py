import gitlab
import json
import urlFinder
import sys


gl = gitlab.Gitlab('https://gitlab.com/', private_token='rbxzs2WK-vhBnFSRhbn3')

##urlGive(str(sys.argv[1], str(sys.argv[2])))


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
    else:
        print("Error project creation failed")


urlGive(str(sys.argv[1]), str(sys.argv[2]))
