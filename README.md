# ecg-images
Convert ecg signals to images

### This repository contains six different modules, each module creates a different type of an image. The reason is to investigate different possible results in a CNN using different inputs.


#### Explanation of image types

| Image Type    |Description    | Dimensions| Status |
| ------------- |:-------------:| ---------:| ------:|
| A_2D | Images with same size but different population | two | 100% |
| A_1D | Images with same size but different population | one | 95%  |
| B_2D | Images with different size but same population | two | not selected for development |
| B_1D | Images with different size but same population | one | not selected for development |
| C_2D | Images with same size and same population | two | not selected for development |
| C_1D | Images with same size and same population | one | not selected for development |


# How to run the project.

## Create virtual environment

Navigate to the project files were you can find.
* ecg-images-environment.yml
* ecg-images-requirements.txt

#### For Conda environments 
1. Create the environment: `conda env create -f ecg-images-environment.yml`
2. Activate it :`conda activate`
3. Make sure that the environment was installed correctly: `conda env list`

#### For Venv
1. Create a virtual environment
`python3 -m venv ecg-images`

2. Activate the environment
`source ecg-images/bin/activate`

3. Check that the environment is activated
`which python` (Excpected result: `.../ecg-images/bin/python`)

4. Install all the dependencies
`pip install -r requirements.txt`

5. To leave the environment
`deactivate`

### Using Pycharm 
1. File > Open > "ecg-images"
2. "Add Configuration" (top right)
3. Press "+" icon at the new window that appears.
4. Select Python
5. Configuration:
    * Script Path: absolute path to ecg_to_images module i.e. `/home/george/Dropbox/personal/thesis/repos/ecg-images/ecg_to_images/`
    * Parameters: -c and the absolute path to the config file i.e. -c `/home/george/Dropbox/personal/thesis/repos/ecg-images/config.ini`
    * Python Interpreter: Select the interpreter from the conda environment created.
6. Click ok

### Using the terminal

