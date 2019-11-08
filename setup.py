import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='tfrecords_creator',  
     version='0.1',
     scripts=['tfrecords_creator'] ,
     author="Daniel Carrera",
     author_email="daniel.r.carrera@outlook.com",
     description="A TFRecords file creator utility",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )