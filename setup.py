from typing import List
from setuptools import find_packages, setup



# Declaring the variables for setup fucntions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1",
AUTHOR = "Shubham Kamble",
DESCRIPTION = "This is the demo of Machine Learning Project"
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This fucntion is going to return list of requirements
    mentioned in the requiremts.txt file
    
    return This fucntion is going to return a list  which contain name
    of libraries mentioned in requiremnts.txt files
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME, 
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
    
)


# if __name__=="__main__":
#     print(get_requirements_list())



