
from md2dm import get_environment_filename, \
                  get_environment_template_filename, \
                  get_default_input_folder, \
                  get_default_output_folder
from able import EnvString, StringReader, TemplateString, Stack, ProjectModel

def get_value(dictionary, stack):
    print('get_value', dictionary)
    print('  stack', stack)
    rc = dictionary
    if stack.size() == 0:
        print('  get_value1')
        rc = dictionary
    elif stack.size() == 1:
        rc = dictionary[stack[0]]
        print('  get_value2')

    elif stack.size() == 2:
        rc = dictionary[stack[0]][stack[1]]
        print('  get_value3')

    elif stack.size() == 3:
        rc = dictionary[stack[0]][stack[1]][stack[2]]
        print('  get_value4')

    elif stack.size() == 4:
        rc = dictionary[stack[0]][stack[1]][stack[2]][stack[3]]
        print('  get_value5')

    return rc

#def get_resources(project):

def main():
    from pprint import pprint
    ##1. Setup environment
    #env_folder_filename =
    #template_folder_filename = get_environment_template_filename()
    print('environment_filename         ',get_environment_filename())
    print('environment_template_filename',get_environment_template_filename())
    print('default_input_folder         ',get_default_input_folder())
    print('default_output_folder        ', get_default_output_folder())

    env_string = EnvString(StringReader(get_environment_filename())
                       or
                       TemplateString(StringReader(get_environment_template_filename())) \
                       .merge('<<MD2DM_INPUT_FOLDER>>', get_default_input_folder()) \
                       .merge('<<MD2DM_OUTPUT_FOLDER>>', get_default_output_folder())
                       )
    print('env_string', env_string)

    resource_stack = Stack('project/resource')
    ff =  '{}/source/data/md2dm.project.md'.format(get_default_input_folder())
    print('ff',ff)
    print('md',StringReader(ff))
    project_model = ProjectModel(StringReader(ff))
    print('project', project_model)
    print('resource_stack', resource_stack)

    owners = get_value(dictionary=project_model, stack=Stack('project/owner'))
    claims = get_value(dictionary=project_model, stack=Stack('project/claim'))
    resources = get_value(dictionary=project_model, stack=resource_stack)
    model = [resources[r]['model'] for r in resources]
    methods = [resources[r]['methods'] for r in resources]

    print('owners   ', owners)
    print('claims   ', claims)
    print('resources', resources)
    print('model    ', model)
    print('methods  ', methods)



if __name__ == "__main__":
    # execute as docker
    main()