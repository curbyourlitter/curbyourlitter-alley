#!/bin/bash
source $HOME/.bashrc
source $HOME/.virtualenvs/$ALLEY_VIRTUAL_ENV/bin/activate
django-admin cartodbsync
