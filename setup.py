from setuptools import setup, find_packages

setup(
    name='2220674062',
    version='0.1.0',
    author='Azra Sugeç',
    author_email='azrasugec@example.com',
    description='Finds the shortest path between two points using OpenStreetMap data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/azrasugec/assignment6',
    packages=find_packages(),
    install_requires=[
        'osmnx',
        'networkx',
        'folium',
        'geopy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
