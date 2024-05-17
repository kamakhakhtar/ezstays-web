#!/bin/bash

# Navigate to the directory containing your repository
cd /home/arfa/ezstays/ezstays-web

# Add all changes to the staging area
git add .

# Commit changes with a timestamp
git commit -m "Auto commit $(date +'%Y-%m-%d %H:%M:%S')"

# Push changes to the 'main' branch on GitHub
git push origin main >> /home/arfa/cronlog/logfile.log 2>&1
