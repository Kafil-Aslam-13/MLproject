# this setup.py will be responsible for creating my ml application as a package
from setuptools import find_packages ,setup
from typing import List
HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this fn will return the list of requirements
    '''
    # requirements=[]
    # with open(file_path) as file_obj:
    #     requirements=file_obj.readlines()
    #     requirements= [req.replace("\n","")for req in requirements]
        
    #     if HYPEN_E_DOT in requirements:
    #         requirements.remove(HYPEN_E_DOT)
    # return requirements
    with open(file_path) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("-e")
        ]


setup(
    name='mlproject',
    version='0.0.1',
    author='Kafil',
    author_email='aslamkafil13@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    )
# suppose we want to find a folder named src by ourself to be found as a package . inside source we need to create file named __init__.py
# our setup.py will try to find in how many folders we have __init__.py and consiter them as a package itself 
## then it will try to build this after which we can import it anywhere we want
## here our entire project development will happen inside this src folder