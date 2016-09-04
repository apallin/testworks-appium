#!/bin/bash -e

# Parse last commit message and version
commit_msg=$(git log -1 --pretty=%B)
version=$(awk '/^__version__/{print $NF}')

# Create tag from message
git tag "$version" -m "$commit_msg"

# Push tags
git push --tags origin master

# Test register to pypitest
python setup.py register -r pypitest

# Test upload to pypitest
python setup.py sdist upload -r pypitest

# Register to pypi
python setup.py register -r pypi

# Upload to pypi
python setup.py sdist upload -r pypi
