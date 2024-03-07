# Md2dm
 Convert a markdown document to a project model

## Process
### Expected
```
 setup env ...........   + create md2dm.env
                         |     + use template when template is available
                         |         + use <<template>> style
                         |
 confirm env .........   + confirm <<HARVEST_INPUT_FOLDER>>
                         + confirm <<HARVEST_OUTPUT_FOLDER>>
                         + confirm <<HARVEST_OUTPUT_FILENAME>>
                         |
 convert .............   + find all files ending in '.py' or '.env'
                         |   + find all lines that start with '##'
                         |       + convert lines to markdown
                         |
 save .................. + save compiliation to 'README.md'
                         + save ".env"
                         + save "project_model.json"
```
### Actual
1. Setup environment
    1. Initialize "md2dm.env" using template when "md2dm.env" is not found
    1. Load environment variables from "md2dm.env" when "md2dm.env" is found
    1. Collect or Confirm MD2DM_INPUT_FOLDER
    1. Collect or Confirm MD2DM_OUTPUT_FOLDER
    1. Collect or Confirm MD2DM_OUTPUT_FILENAME
    1. Confirm the saving of "md2dm.env"
1. Convert markdown to project model
    1. Include files ending with ".md"
    1. Save "md2dm.env"
        1. Save in the same folder as md2dm.py
        1. Preserve user's manual changes
        1. Update changes to existing environment variables
    1. Save Data Model
## The Idea
 Reference tree branch with a stack

 eg markdown

```
# A
1. B
    1. C
    1. D
1. E
    1. F
```

 Convert markdown line into a stack

| line | level (lv) | size (sz) | (sz-lv)+1 | ss         | stack   |
|----|----|----|-----------|------------|---------|
| "# A"     | 1  | 0  | 0  |  pop(0), push(A)  |  [A]
| "1. B"    | 2  | 1  | 0  |  pop(0), push(B)  |  [A,B]
| "----1. C"  | 3  | 2  | 0  |  pop(0), push(C)  |  [A,B,C]
| "----1. D"  | 3  | 3  | 1  |  pop(1), push(D)  |  [A,B,D]
| "1. E"    | 2  | 3  | 2  |  pop(2), push(E)  |  [A,E]
| "----1. F"  | 3  | 2  | 0  |  pop(0), push(F)  |  [A,E,F]

 "-" is a placeholder for a space
* make bin folder
* make data folder
* makes template folder

## The RecursionList

__RecursionList__

 List of files, folders and subfolders

* Ignore specific files and/or folders (eg ['.DS_Store', '.git', '.gitignore', '.idea']) on evaluation
* List of folders, subfolder and files in a given folder on request