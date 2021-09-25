import os
def makeFile(name, data):
  file = open(name, 'w')
  file.write(data)

def makeFolder(name):
  try:
    os.makedirs(name)
  except:
    x = 1