#!/bin/bash
source $HOME/.bash_profile
workon $ALLEY_VIRTUAL_ENV && django-admin cartodbsync
