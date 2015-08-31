#!/bin/bash
echo "Starting socratasync"
source $HOME/.bash_profile
workon alley
django-admin socratasync
echo "Finishing socratasync"
