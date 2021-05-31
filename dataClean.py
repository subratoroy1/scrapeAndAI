from shutil import copyfile

rawFile = "rightMove.json"
cleansedFile = "rightMove1.json"

copyfile(src=rawFile, dst=cleansedFile)

with open(cleansedFile,'r') as file:
    filedata = file.read()
    filedata = filedata.replace('\\u00a3','GBP')
    filedata = filedata.replace('\\u00a0','GBP')
    filedata = filedata.replace('<div>','')
    filedata = filedata.replace('</div>','')
    filedata = filedata.replace('<strong>','')
    filedata = filedata.replace('</strong>','. ')
    filedata = filedata.replace('<br>','. ')
    filedata = filedata.replace('<p>','. ')
    filedata = filedata.replace('</p>','. ')

with open(cleansedFile,'w') as file:
    file.write(filedata)