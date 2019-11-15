#!/bin/sh
echo "\e[1;31mDeleting *.pyc and __pycache__\e[0m"
echo "\e[1;95mCleaning in root folder\e[0m"
rm *.pyc
rm -r __pycache__
echo "\e[1;95mCleaning in copper folder\e[0m"
rm copper/*.pyc
rm -r copper/__pycache__
