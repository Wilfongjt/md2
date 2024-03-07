### Md2dm
## Convert a markdown document to a project model
##
import os
import json
from pprint import pprint
from source.recursive_list import RecursionList

from able import EnvString, \
                 Inputable, \
                 StringReader, \
                 StringWriter, \
                 UpdaterString, \
                 TemplateString,\
                 ProjectModel, \
                 Stack


#### Process
##### Expected
##```
## setup env ...........   + create md2dm.env
##                         |     + use template when template is available
##                         |         + use <<template>> style
##                         |
## confirm env .........   + confirm <<HARVEST_INPUT_FOLDER>>
##                         + confirm <<HARVEST_OUTPUT_FOLDER>>
##                         + confirm <<HARVEST_OUTPUT_FILENAME>>
##                         |
## convert .............   + find all files ending in '.py' or '.env'
##                         |   + find all lines that start with '##'
##                         |       + convert lines to markdown
##                         |
## save .................. + save compiliation to 'README.md'
##                         + save ".env"
##                         + save "project_model.json"
##```

def get_bin_folder():
    return os.getcwd()
def get_default_input_folder():
    return os.getcwd().replace('/bin', '')
def get_default_output_folder():
    return os.getcwd()
def get_template_folder():
    return os.getcwd().replace('/bin', '/source/template')
def get_data_folder():
    return os.getcwd().replace('/bin', '/source/data')

def get_environment_filename():
    return '{}/md2dm.env'.format(get_bin_folder())


def get_environment_template_filename():
    return '{}/md2dm.env.tmpl'.format(get_template_folder())


## Model Postgrest
def main():
    ##### Actual
    ##1. Setup environment

    env_folder_filename = get_environment_filename() #'{}/md2dm.env'.format(get_bin_folder())
    ##    1. Initialize "md2dm.env" using template when "md2dm.env" is not found

    template_folder_filename = get_environment_template_filename() # '{}/md2dm.env.tmpl'.format(get_template_folder())

    ##    1. Load environment variables from "md2dm.env" when "md2dm.env" is found

    env_string = EnvString(StringReader(env_folder_filename)
                           or
                           TemplateString(StringReader(template_folder_filename)) \
                           .merge('<<MD2DM_INPUT_FOLDER>>', get_default_input_folder()) \
                           .merge('<<MD2DM_OUTPUT_FOLDER>>', get_default_output_folder())
                           )

    ##    1. Collect or Confirm MD2DM_INPUT_FOLDER

    os.environ['MD2DM_INPUT_FOLDER'] = Inputable().get_input('MD2DM_INPUT_FOLDER',
                                         os.environ['MD2DM_INPUT_FOLDER'],
                                         hardstop=True)

    ##    1. Collect or Confirm MD2DM_OUTPUT_FOLDER

    os.environ['MD2DM_OUTPUT_FOLDER'] = Inputable().get_input('MD2DM_OUTPUT_FOLDER',
                                          os.environ['MD2DM_OUTPUT_FOLDER'],
                                          hardstop=True)

    ##    1. Collect or Confirm MD2DM_OUTPUT_FILENAME

    os.environ['MD2DM_OUTPUT_FILENAME'] =  Inputable().get_input('MD2DM_OUTPUT_FILENAME',
                                            os.environ['MD2DM_OUTPUT_FILENAME'],
                                            hardstop=True)
    ##    1. Confirm the saving of "md2dm.env"
    save_env = Inputable().get_input('save env changes',
                                     'N',
                                     hardstop=False)

    # user feedback
    print('MD2DM_INPUT_FOLDER:   ', os.environ['MD2DM_INPUT_FOLDER'])
    print('MD2DM_OUTPUT_FOLDER:  ', os.environ['MD2DM_OUTPUT_FOLDER'])
    print('MD2DM_OUTPUT_FILENAME:',os.environ['MD2DM_OUTPUT_FILENAME'])
    ##1. Convert markdown to project model
    ##    1. Include files ending with ".md"
    rlist = RecursionList(folder=os.environ['MD2DM_INPUT_FOLDER'],
                          ext=['.project.md']).traverse_folder()
    project = {}
    stack = Stack()
    # read all the lines in all the files that end with '.data.md'
    project_model = {}
    for ff in rlist:
        project_model = ProjectModel(StringReader(ff))
        pprint(project_model)
    #print('type', type(str(project)))
    print('project_model', project_model)
    #pprint(project_model)
    print('---')

    if save_env.upper() == 'Y':
        ##    1. Save "md2dm.env"
        ##        1. Save in the same folder as md2dm.py

        changelist = ['{}={}'.format(el, os.environ[el]) for el in os.environ if el.startswith('MD2DM_')]

        ##        1. Preserve user's manual changes
        contents = EnvString(StringReader(env_folder_filename))

        ##        1. Update changes to existing environment variables

        contents = UpdaterString(contents).updates('\n'.join(changelist))
        StringWriter(folder_filename=env_folder_filename,
                     content_string=contents)
        #contents = CreatorString(folder_filename=env_folder_filename, default_contents=contents,overwrite=True)
        ##    1. Save Data Model

if __name__ == "__main__":
    # execute as docker
    main()