# https://www.geeksforgeeks.org/command-line-scripts-python-packaging/

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'More ergonomic wrapper around TogglCli for continuing Toggl time entries.'

setup(
        name ='Pit2ya',
        version ='0.1.1',
        author ='Exr0n',
        author_email ='mail@exr0n.com',
        url ='https://github.com/Exr0nProjects/pit2ya',
        description ='Ergonomic continuation of Toggl time entries',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'pt=pit2ya.user_start:user_start'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords ='toggl togglcli wrapper',
        install_requires = requirements,
        zip_safe = False
)

