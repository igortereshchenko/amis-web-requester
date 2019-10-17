import setuptools

setuptools.setup(
     name='amis-web-requester',
     version='0.1',
     scripts=['InfinityRequester.py','InfinityScroller.py','Requester.py','RequesterException.py','Response.py','test.py'] ,
     author="Igor Tereshchenko",
     author_email="tereshchenko.igor@gmail.com",
     description="A web requester utility package",
     long_description="A web requester utility package",
     long_description_content_type="text/markdown",
     url="https://github.com/igortereshchenko/amis-web-requester",
     packages=setuptools.find_packages(),
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )