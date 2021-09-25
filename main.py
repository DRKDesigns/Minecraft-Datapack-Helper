import files
name = input('What is the packname you want? ')
print('Creating pack...')
files.makeFolder(name)
files.makeFile(name+'/pack.mcmeta','''{
	"pack":
	{
		"description": "This is a datapack using DRKDesigns' packhelper",
		"pack_format": 1
	}
}''')
files.makeFolder(name+'/data/pack/functions')
files.makeFolder(name+'/data/minecraft/tags/functions')
files.makeFile(name+'/data/minecraft/tags/functions/tick.json','''{
    "values":[
        "pack:repeat"
    ]
}''')
files.makeFile(name+'/data/minecraft/tags/functions/load.json','''{
    "values":[
        "pack:startup"
    ]
}''')
print('Pack made!')
oldOpen = ''
oldLoop = ''
while True:
  if not oldOpen == open('open.txt').read():
    oldOpen = open('open.txt').read()
    files.makeFile(name+'/data/pack/functions/startup.mcfunction', oldOpen)
    print('startup.mcfuntion updated!')
  if not oldLoop == open('loop.txt').read():
    oldLoop = open('loop.txt').read()
    files.makeFile(name+'/data/pack/functions/repeat.mcfunction', oldLoop)
    print('repeat.mcfuntion updated!')