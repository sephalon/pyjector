import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Pyjector',
    version='0.2.3',
    author='John Brodie',
    author_email='john@brodie.me',
    description='Control your projector over a serial port',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://www.github.com/JohnBrodie/pyjector',
    packages=setuptools.find_packages(),
    install_requires=['pyserial'],
    package_data={
        'pyjector': ['projector_configs/*.json'],
    },
)
