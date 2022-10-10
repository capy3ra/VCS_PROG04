import socket
import argparse

PORT = 80
# url = 'http://blogtest.vnprogramming.com/'

# Create CLI for program
def cre_args():
    args = argparse.ArgumentParser(description='The program to Get the title of the website')
    args.add_argument('--url', dest="url", help="Get the title with your url", default='http://blogtest.vnprogramming.com/')
    return args.parse_args()

def main():
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create request
    args = cre_args()
    url = args.url
    url = url[7:len(url)-1]
    client.connect((url, PORT))
    header = "GET / HTTP/1.1\r\nHost: " + url + "\r\nConnection: close\r\n\r\n"
    # print(header)

    # Send request
    client.sendall(header.encode())

    # Receive response
    response = client.recv(10000).decode()

    # Handle String
    indexTitle1 = response.find("<title>")
    indexTitle2 = response.find("</title>")
    title = response[indexTitle1 + 7:indexTitle2]
    print("Title:", title)

if __name__ == "__main__":
	main()