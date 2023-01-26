import dropbox
access_token = '<token value here>'
dbx = dropbox.Dropbox(access_token)
with open("C:\Test.txt", "w") as f:
metadata, res = dbx.files_download(path="/Test.txt")
f.write(res.content)
