import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydiscotool',
    version='0.1.2',
    author="Daniel Carrera",
    author_email="daniel.r.carrera@outlook.com",
    description="A suite of python tools to help with Disco",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wundr-Disco/pydiscotool",

    packages=["pydiscotool"],

    install_requires=[
        'click',
    ],

    entry_points='''
        [console_scripts]
        pydiscotool=pydiscotool.init:main
    ''',

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
)
