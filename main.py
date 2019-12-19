import gitlab
import json


gl = gitlab.Gitlab('https://gitlab.com/', private_token='rbxzs2WK-vhBnFSRhbn3')

project = gl.projects.create({'name': 'project2'})
