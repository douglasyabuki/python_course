# Using subprocess to execute external commands
# subprocess is a Python module for running external
# processes and commands within your program.
# The simplest method to achieve this is using subprocess.run().
# Main arguments of subprocess.run():
# - stdout, stdin, stderr → Redirect output, input, and errors
# - capture_output → Captures the output and errors for later use
# - text → If True, inputs and outputs are treated as text and
#   automatically encoded or decoded using the platform's default charset
#   (usually UTF-8).
# - shell → If True, enables shell access. When using shell=True,
#   it's recommended to pass the command and its arguments as a single string.
# - executable → Allows specifying the exact executable to use when
#   starting the subprocess.
# Returns:
# stdout, stderr, returncode, and args
#
# Important: Windows may use a different encoding like cp1252, cp852, or cp850.
# On Linux and macOS, typically utf-8 is appropriate.
#
# Example commands:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import sys

# sys.platform values: linux, linux2, darwin, win32

cmd = ['ls -lah /']
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encoding,
    shell=True,
)

print()

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)
