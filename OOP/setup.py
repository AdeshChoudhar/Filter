from setuptools import find_packages, setup

setup(
    name='Filter',
    packages=find_packages(include=['Filter']),
    version='0.1.0',
    description='Filter',
    author='AdeshChoudhar',
    license='MIT',
    install_requires=['opencv-python', 'numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
