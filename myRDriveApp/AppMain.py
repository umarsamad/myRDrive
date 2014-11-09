# Include the Dropbox SDK
import dropbox
import webbrowser

# Get your app key and secret from the Dropbox developer website
app_key = 'XXXXXXXXX'
app_secret = 'XXXXXXXX'

access_type = "dropbox"
session = dropbox.session.DropboxSession(app_key, app_secret, access_type)
request_token = session.obtain_request_token()
url = session.build_authorize_url(request_token)
msg = "Opening %s. Kindly Confirm Working Internet Connection with Dropbox access is Available."
print msg % url
webbrowser.open(url)
raw_input("Press enter to confirm")

access_token = session.obtain_access_token(request_token)

client = dropbox.client.DropboxClient(session)#access_token)

print 'linked account: ', client.session.is_linked()

myFile = open('SimpleFile.txt', 'rb')
response = client.put_file('/SimpleFile.txt', myFile)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

myFile, metadata = client.get_file_and_metadata('/SimpleFile.txt')
out = open('SimpleFile.txt', 'wb')
out.write(myFile.read())
out.close()
print metadata

del myFile
del session
del client
del response
del folder_metadata
