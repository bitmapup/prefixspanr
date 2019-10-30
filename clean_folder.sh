#!/bin/sh
echo "\e[1;31mDeleting *.pyc and __pycache__\e[0m"
echo "Cleaning in root folder"
rm *.pyc
rm -r __pycache__
echo "Cleaning in copper folder"
rm copper/*.pyc
rm -r copper/__pycache__
