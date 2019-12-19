import gitlab


gl = gitlab.Gitlab('https://gitlab.com/', private_token='rbxzs2WK-vhBnFSRhbn3')
projects = gl.projects.list()
for project in projects:
    print(project)
