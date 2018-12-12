from setuptools import setup, find_packages
setup(
    name="clingen_interpretation",
    version="0.2",
    packages=find_packages(),
    install_requires=['requests>=2.17'],
    package_data={
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'clingen_interpretation': ['ValueSets/*'],
    }
)
