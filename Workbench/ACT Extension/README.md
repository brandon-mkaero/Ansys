# Ansys Workbench ACT Extension

This repository contains an ACT extension that uses a Jinja2 template system to process input parameters and generate an output file.

## Repository Structure

- **BG_Template.bgd** - Template file used by `main.py`.
- **main.py** - The main script that processes the template using parameters from `params.json`.
- **run.py** - A script that executes `main.py`.
- **run.exe** - A compiled version of `run.py`, created using PyInstaller.
- **params.json** - JSON file containing input parameters for template processing.

## Extension Functionality

1. **Template Processing**: `main.py` loads `params.json`, applies its values to `BG_Template.bgd` using Jinja2, and generates an output file.
2. **Execution**: The script can be run via `run.py` (Python) or `run.exe` (standalone executable).
3. **Logging**: Execution logs are written to `log.txt` and `main_log.txt`.

## Overview of ACT Functionality

An ACT extension needs 3 files to function.
1. **Input File** (~)
2. **Output File** (~)
3. **Executable** (.exe)

The Input and Output files must be specified in Workbench along with the Executable's directory.

An easy way to create an Executable is to convert a python script (i.e. *run.py*) into an Executable (i.e. *run.exe*), after installing the *PyInstaller* module, run the following script in the python terminal:
```python
pyinstaller --onefile run.py  
```

Since the Executable file needs to be compiled after any changes have been made to the original script (*run.py*),  one could repurpose the Executable file such that it's only function is to run an external python script. The external script, which easily be modified by the user, then performs the necessary tasks.

## Usage

### 1. Creating a Workflow

To create an ACT Extension, follow the steps below:

1. Select "*Create a workflow...*" command in the ACT tab of Workbench's "*Toolbox*" panel.
2. Select "*Add a task group...*" in the "*Toolbox*" panel
	- Name the Task Group
	- Select an Icon (.png)
	- Give it an abbreviation
	- Select the Parametric check-box if applicable
3. Now Select "*Add a task...*"
	- Name the Task
	- Select an Icon (.png)
	- Select the application path 
4. Add more tasks if necessary
5. Under "*Workflow Actions*", select "*Publish Workflow*"

Although one can't change the name of the application/executable, you can replace it with an application with the same name when selecting the application path in Workbench.

Once you have created an extension, you cannot edit it in Workbench. To delete an extension, unload the applicable extension via "*Extensions*>*Manage Extensions*", and then navigate to the following path where you can find and delete the extension.

```
"C:\Users\...\AppData\Roaming\Ansys\v241\ACT\extensions"
```

### 2. Running the Extension

Once the extension has been created, the executable and input/output files must be specified, even if they aren't necessary for the functionality of the extension. The external script updates all of the design points in the project folder. Since the `params.json` file is populated in each of the "*dp*" folders, the `main.py` script must be able to navigate the design point folders.

## Dependencies

Ensure you have the required Python packages installed:

```python
pip install jinja2
```

## Notes

- The script automatically deletes old output files before generating a new one.
- Ensure `params.json` is correctly formatted to avoid execution errors.
