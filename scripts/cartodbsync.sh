#!/bin/bash
echo "Starting cartodbsync"
source $HOME/.bash_profile
workon alley
django-admin cartodbsync
echo "Finishing cartodbsync"
