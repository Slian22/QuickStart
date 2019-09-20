from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()
VERSION = '0.0.1'

setup(
    name='QuickStart',
    version=VERSION,
    description='Easier to perform general operations!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='',
    author='RhythmLian',
    author_mail='RhythmLian@outlook.com',
    url="https://github.com/Rhythmicc/QuickStart",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['pyperclip', 'requests'],
    entry_points={
        'console_scripts': [
            'qs = QuickStart.main:main'
        ]
    },
)