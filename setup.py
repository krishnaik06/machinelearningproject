from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return a list of requirements mentioned in the
    requirements.txt file.

    Returns: List of requirements.
    """
    with open("requirements.txt") as f:
        return f.readlines().remove("-e .")


setup(
name="housing-prediction",
version="0.2",
description="Housing price prediction",
author="KRish",
author_email="krishnaik06@gmail.com",
packages=find_packages(),
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())
    

