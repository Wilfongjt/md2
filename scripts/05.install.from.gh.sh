#!/bin/sh
export DISTUTILS_DEBUG=ok
cd ..
## Syntax: pip install "Package" @ git+"URL of the repository"
# run this script in the client project
pip install able@git+https://github.com/Wilfongjt/abilities#egg=able-1.8.2
