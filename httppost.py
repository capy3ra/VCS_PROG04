import socket
import argparse

PORT = 80

# Create CLI for program
def cre_args():
    args = argparse.ArgumentParser(description='The program to verify login')
    args.add_argument('--url', dest="url", help="URL dest", default="http://blogtest.vnprogramming.com/")
    args.add_argument('--username', dest="username", help="Enter your username", default="test")
    args.add_argument('--password', dest="password", help="Enter your password", default="test123QWE@AD")
    return args.parse_args()

def main():
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Init args
    args = cre_args()
    url = args.url
    username = args.username
    password = args.password

    # Create request
    url = url[7:len(url) - 1]
    client.connect((url, PORT))
    requestBody = "log=" + username + "&pwd=" + password + "&wp-submit=Log+In&redirect_to=http://blogtest.vnprogramming.com/wp-admin/&testcookie=1"
    contentLength = str(len(requestBody))
    header = "POST /wp-login.php HTTP/1.1\r\nHost: " + url + "\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept-Encoding: gzip, deflate\r\nCookie: wordpress_test_cookie=WP Cookie check\r\nConnection: close\r\nContent-Length: " + contentLength + "\r\n\r\n" + requestBody + "\r\n"
    # print(header)

    #Send and recv
    client.sendall(header.encode())
    response = client.recv(256).decode()

    #Conclusion
    if (response.strip().find("HTTP/1.1 302 Found") == 0):
        print("User " + username + " dang nhap thanh cong")
    else:
        print("User " + username + " dang nhap that bai")

if __name__ == "__main__":
    main()