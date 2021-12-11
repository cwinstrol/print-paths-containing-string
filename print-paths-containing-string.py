#p=''

import os

for root, dirs, files in os.walk(p):
 if '\\n' in root:
  print(root)
