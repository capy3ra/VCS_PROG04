import socket
import argparse
import os
import subprocess
import re
from subprocess import run

# Create CLI for program
def cre_args():
    args = argparse.ArgumentParser(description='The program to download file')
    args.add_argument("--url", dest="url", help="URL dest", default="http://blogtest.vnprogramming.com/")
    args.add_argument("--remote-file", help="file", dest="remoteFile")
    return args.parse_args()

def main():
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Init args
    args = cre_args()
    url = args.url
    remoteFile = args.remoteFile
    url = url[7:len(url) - 1]
    
    # Download
    downloadCommand = "nohup wget " + url + remoteFile
    os.system(downloadCommand)
    # outputDl = run(downloadCommand, capture_output=True).stdout
    
    #Get name
    fileName = downloadCommand[downloadCommand.rfind('/')+1:len(downloadCommand)]
    extFile = fileName[fileName.find('.')+1:len(fileName)]
	
    # Conclusion
    if(extFile == "jpg" or extFile == "png" or extFile == "gif" or extFile == "jpeg"):
    	getSizeCommand = str(subprocess.check_output("ls -l | grep " + fileName +" | awk '{print $5}'", shell=True))
    	sizeOfFile = re.findall(r'\d+', getSizeCommand)[0]
    	print("Kich thuoc cua anh la: " + str(sizeOfFile) + " bytes")
    else :
    	print("Khong ton tai file anh")
    
if __name__ == "__main__":
    main()
