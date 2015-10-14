#!/bin/bash
echo "Starting cartodbclean"
source $HOME/.bash_profile
workon alley
django-admin cartodbclean
echo "Finishing cartodbclean"
