from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    from the given requirements file.
    """
    requirements = []

    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ml-project-aws-azure",
    version="0.0.1",
    author="Andrew-Adel",
    author_email="andrewadellabib77@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)