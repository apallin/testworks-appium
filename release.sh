#!/bin/bash -e

# Test register to pypitest
python setup.py register -r pypitest

# Test upload to pypitest
python setup.py sdist upload -r pypitest

# Register to pypi
python setup.py register -r pypi

# Upload to pypi
python setup.py sdist upload -r pypi
