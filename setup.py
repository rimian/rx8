from setuptools import setup, find_packages

setup(
    name='rx8',
    version='0.1.1',
    description='RX8 project for CAN bus interaction',
    author='Rimian Perkins',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'can',
        'cantools'
    ],
    scripts=[
        'bin/kiosk.sh',
    ],
    include_package_data=True,
    package_data={
        'rx8': ['rx8.dbc']
    },
    entry_points={
        'console_scripts': [
            'rx8=rx8.__main__:main',
        ]
    }
)