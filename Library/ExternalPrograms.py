# with subprocess module, we can spot a child process.
# a process is a basically an instance of a running program

import subprocess
import os

# excuting this other.py as a child process
# it's going to be a different memory space.
# different from importing that script and executing it here.

completed = subprocess.run(
    ["python", "Library\\other.py"], capture_output=True, text=True)

print(type(completed))
print("returncode", completed.returncode)
print("args", completed.args)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
