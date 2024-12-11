## tempfile module
import tempfile

## create temporary file
temp_file = tempfile.TemporaryFile()

## write to temporary file
## it takes byte as input, so use b""
temp_file.write(b'Save this special number for me: 567890')
## setting seek point to zero to read from beginning
temp_file.seek(0)

## Read the temporary file
print(temp_file.read())

## now close the file
temp_file.close()
