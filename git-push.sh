#!bin/bash

git add .
read -p "Enter commit message: " choice
git commit -m "$choice"
git push origin main
