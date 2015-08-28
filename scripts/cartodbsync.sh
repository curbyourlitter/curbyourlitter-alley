#!/bin/bash
source $HOME/.bash_profile
source `which virtualenvwrapper.sh`
workon $ALLEY_VIRTUAL_ENV
django-admin cartodbsync
