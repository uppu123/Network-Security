from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """This function will return the list of requirements"""
    requirements_lst = []
    try:
        with open("requirements.txt",'r') as file_obj:
            lines = file_obj.readlines()

            ##process each line in the requirements.txt file
            for line in lines:
                line = line.strip()
                ## ignore empty lines and -e.
                if line and line != "-e .":
                    requirements_lst.append(line)


    except FileNotFoundError:
        print(f"File not found")
    return requirements_lst



setup(
    name="Network Security",
    version="0.0.1",
    author="Upendra",
    author_email="uk8530@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



