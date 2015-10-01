#!/bin/bash
echo "Starting cleancanrequests"
source $HOME/.bash_profile
workon alley
django-admin cleancanrequests
echo "Finishing cleancanrequests"
