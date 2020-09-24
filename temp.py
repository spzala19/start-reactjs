import subprocess
import re
from subprocess import CalledProcessError
result,error = subprocess.getstatusoutput(f"npm install -D parcel-bundler")
print(result,error)
