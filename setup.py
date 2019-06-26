from setuptools import setup

clfs = []
clfs.append("Development Status :: 5 - Production/Stable")
clfs.append("Intended Audience :: Developers")
clfs.append("License :: OSI Approved :: MIT License")
clfs.append("Operating System :: Microsoft :: Windows :: Windows XP")
clfs.append("Operating System :: Microsoft :: Windows :: Windows Vista")
clfs.append("Operating System :: Microsoft :: Windows :: Windows 7")
clfs.append("Operating System :: Microsoft :: Windows :: Windows 8")
clfs.append("Operating System :: Microsoft :: Windows :: Windows 8.1")
clfs.append("Operating System :: Microsoft :: Windows :: Windows 10")
clfs.append("Operating System :: MacOS :: MacOS X")
clfs.append("Operating System :: POSIX :: Linux")
clfs.append("Programming Language :: Python :: 3")

setup(name="pyfmodex", version="0.5.4", author="Lukas Tyrychtr", author_email="lukastyrychtr@gmail.com", url="https://www.github.com/tyrylu/pyfmodex", packages=["pyfmodex", "pyfmodex.studio"], long_description=open("readme.md", "r").read(), description="Python bindings to the Fmod Ex library.", license="MIT", classifiers=clfs, install_requires=["py-flags"])