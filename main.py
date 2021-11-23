import dropbox
class TransferData:
  def _init_(self,access_token):
    self.access_token=access_token
  def upload_file(self,file_from,file_to):
      dbx=dropbox.DropBox(self.access_token)
      r=open(file_from,'rb')
      dbx.files_upload(f.read(),file_to)
def main():
      access_token='sl.A80646NNNHeT67tGACnbZjbl2pr1cUX96y-bVUFz8WEHZJKzegJ2_k7ibCyRj9exXtNiXALOqVb34ULu7veNl0zagFGz1Pfb0HCrFg1a4dpOUAFmlb_lH-aKx0qt7H1kbriowxGR8HZf'
      transferData= TransferData(access_token)
      file_from=input("enter the file path to transfer:")
      file_to=input("enter the full path to upload to dropbox")
      transferData.upload_file(file_from,file_to)
      print("file has been moved")

main()