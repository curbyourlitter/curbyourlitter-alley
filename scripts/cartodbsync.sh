#!/bin/bash
echo "Starting cartodbsync"
source $HOME/.bash_profile
source `which virtualenvwrapper.sh`
workon $ALLEY_VIRTUAL_ENV
# TODO ARGHGEGEGEGEJJKSLDFJKL
django-admin cartodbsync
echo "Finishing cartodbsync"
