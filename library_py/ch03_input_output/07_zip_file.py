## zipfile module
import zipfile

## open and list
zip = zipfile.ZipFile('archive.zip', 'r')
## it will list out the files in it
print(zip.namelist())

## metadata in the zip folder
for meta in zip.infolist():
    print(meta)

## getting the individual file metadata
info = zip.getinfo('purchased.txt')
print(info)

## access file in zip folder
print(zip.read('purchased.txt'))

## you can do this way to
with zip.open('purchased.txt') as f:
    print(f.read())

## extract single individual files
# zip.extract('wishlist.txt')

## extract the whole zip file
# zip.extractall()

## close the file
zip.close()

