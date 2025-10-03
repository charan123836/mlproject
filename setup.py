from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]  # clean up newlines

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Charan',
    author_email='charanvenkat2005@gmail.com',  # ✅ fixed
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
