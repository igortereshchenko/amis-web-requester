import setuptools

setuptools.setup(
     name='amis-web-requester',
     version='0.3',

     author="Igor Tereshchenko",
     author_email="tereshchenko.igor@gmail.com",
     description="A web requester utility package",
     long_description="A web requester utility package",
     long_description_content_type="text/markdown",
     url="https://github.com/igortereshchenko/amis-web-requester",
     packages=setuptools.find_packages(),
     include_package_data=True,
     install_requires=['beautifulsoup4>=4.8.1','selenium>=3.141.0','soupsieve>=1.9.4','urllib3>=1.25.6'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )