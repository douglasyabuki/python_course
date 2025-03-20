# Environment variables with Python
# Setting environment variables:
#   Windows PowerShell: $env:VARIABLE="VALUE" | dir env:
#   Linux and Mac: export VARIABLE_NAME="VALUE" | echo $VARIABLE_NAME
#
# To access environment variables in Python:
#   os.getenv('VARIABLE') or os.environ['VARIABLE']
#
# To set environment variables in Python:
#   os.environ['VARIABLE'] = 'value'
#
# Alternatively, use python-dotenv with a .env file:
#   pip install python-dotenv
#   from dotenv import load_dotenv
#   load_dotenv()
# https://pypi.org/project/python-dotenv/
#
# IMPORTANT: Always remember to create a ".env-example" file.

import os
from dotenv import load_dotenv  # type: ignore

# Loads variables from the .env file into the environment
load_dotenv()

# Prints the value of the 'DB_PASSWORD' environment variable
print(os.getenv('DB_PASSWORD'))
