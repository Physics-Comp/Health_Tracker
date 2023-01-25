from setuptools import find_packages, setup


setup(
name="Health_API",
version = '0.1',
packages= find_packages(),
install_requires = [
    'health_path',
    'path'
]
)