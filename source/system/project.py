import os

class Project(str):
    #def __init__(self, owner, workspace, project ):

    def __new__(cls, owner, workspace, project):

        contents = '{}/Development/{}/{}/{}'.format(os.environ['HOME'],owner, workspace, project)

        instance = super().__new__(cls, contents)
        #print('project out', instance)
        return instance

    def getBinFolder(self):
        return '{}/bin'.format(self)

    def getDataFolder(self):
        return '{}/source/data'.format(self)

    def getTemplateFolder(self):
        return '{}/source/template'.format(self)

    def makeDirs(self):
        ##* make bin folder
        if not os.path.isdir(self.getBinFolder()):
            os.makedirs(self.getBinFolder())
        ##* make data folder
        if not os.path.isdir(self.getDataFolder()):
            os.makedirs(self.getDataFolder())
        ##* makes template folder
        if not os.path.isdir(self.getTemplateFolder()):
            os.makedirs(self.getTemplateFolder())
        return self


def main():
    owner = 'test-org'
    workspace = '00-project'
    project_name = 'some-project'
    expected_folder = '{}/Development/{}/{}/{}'.format(os.environ['HOME'], owner,workspace,project_name)
    expected_binfolder = '{}/Development/{}/{}/{}/bin'.format(os.environ['HOME'], owner,workspace,project_name)
    expected_datafolder = '{}/Development/{}/{}/{}/source/data'.format(os.environ['HOME'], owner,workspace,project_name)
    expected_templatefolder = '{}/Development/{}/{}/{}/source/template'.format(os.environ['HOME'], owner,workspace,project_name)

    assert(Project(owner, workspace, project_name)==expected_folder)
    assert(Project(owner, workspace, project_name).getBinFolder()==expected_binfolder)
    assert(Project(owner, workspace, project_name).getDataFolder()==expected_datafolder)
    assert(Project(owner, workspace, project_name).getTemplateFolder()==expected_templatefolder)
    assert(Project(owner, workspace, project_name).makeDirs())

if __name__ == "__main__":
    # execute as docker
    main()