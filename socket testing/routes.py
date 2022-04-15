# Internal dependencies (should ship with python)
import socket

# third party dependencies (need to be installed via pip)
from ezcv.core import generate_site # Used to generate the static html pages

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 6969

# Define the template settings
templates_foler = "site"

generate_site(templates_foler) # Generate site

# ================================ Create the socket with a context manager ================================

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM)  as server_socket: # AF_INET == IPV4, SOCK_STREAM == TCP
    ## SOL_Socket details can be found here https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
    ## This basically sets the internal options of the socket itself to say that SO_REUSEADDR is set to 1 or true which permits reuse of local addresses for this socket 
    ## If you enable this option, you can actually have two sockets with the same Internet port number; but the system won't allow you to use the two identically-named sockets in a way that would confuse the Internet.
    ## The reason for this option is that some higher-level Internet protocols, including FTP, require you to keep reusing the same port number.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Set internal socket to allow SO_REUSEADDR
    server_socket.bind((SERVER_HOST, SERVER_PORT)) # Bind the configured socket to the server (assign ip address and port number to the socket instance)
    server_socket.listen(1) # Listen for incoming connections
    print('Listening on port %s ...' % SERVER_PORT)

    for index in range(100000):
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(4096).decode()
        print(request)

        # Parse HTTP headers
        headers = request.split('\n')
        filename = headers[0].split()[1]

        response_type = "" # Will be replaced with the mime type of the file returned

        # Get the content of the file
        ## if at index
        if filename == '/':
            filename = 'index.html'

        try:
            if filename.endswith(".html"):
                response_type = "text/html"
                with open(f"{templates_foler}/{filename}", "r") as html_file:
                    content = html_file.read()
                response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

            elif filename.endswith(".css"):
                response_type = "text/css"
                with open(f"{templates_foler}/{filename}", "r") as html_file:
                    content = html_file.read()
                response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

            elif filename.endswith(".js"):
                response_type = "text/js"
                with open(f"{templates_foler}/{filename}", "r") as html_file:
                    content = html_file.read()
                response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

            # Images
            elif filename.endswith(".jpg"):
                response_type = "image/jpeg"
                with open(f"{templates_foler}/{filename}", "rb") as image:
                    content = image.read()
                response = content
                
            elif filename.endswith(".png"):
                response_type = "image/png"
                with open(f"{templates_foler}/{filename}", "rb") as image:
                    content = image.read()
                response = content

            # Fonts
            elif filename.endswith(".ttf"):
                response_type = "font/ttf"
                with open(f"{templates_foler}/{filename}", "rb") as font:
                    content = font.read()
                response = content
            
            elif filename.endswith(".woff"):
                response_type = "font/woff"
                with open(f"{templates_foler}/{filename}", "rb") as font:
                    content = font.read()
                response = content

            elif filename.endswith(".woff2"):
                response_type = "font/woff2"
                with open(f"{templates_foler}/{filename}", "rb") as font:
                    content = font.read()
                response = content

        except FileNotFoundError: # Could not find the file
            response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

        # Send HTTP response

        if type(response) == bytes:
            header_config = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n'
            client_connection.send(header_config.encode())
            client_connection.send(response)
        else:
            client_connection.sendall(response.encode())

        client_connection.close()


# ================================ Manually create the socket ================================

# # Create socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET == IPV4, SOCK_STREAM == TCP

# ## SOL_Socket details can be found here https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
# ## This basically sets the internal options of the socket itself to say that SO_REUSEADDR is set to 1 or true which permits reuse of local addresses for this socket 
# ## If you enable this option, you can actually have two sockets with the same Internet port number; but the system won't allow you to use the two identically-named sockets in a way that would confuse the Internet.
# ## The reason for this option is that some higher-level Internet protocols, including FTP, require you to keep reusing the same port number.
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Set internal socket to allow SO_REUSEADDR
# server_socket.bind((SERVER_HOST, SERVER_PORT)) # Bind the configured socket to the server (assign ip address and port number to the socket instance)
# server_socket.listen(1) # Listen for incoming connections
# print('Listening on port %s ...' % SERVER_PORT)

# for index in range(100000):
#     # Wait for client connections
#     client_connection, client_address = server_socket.accept()

#     # Get the client request
#     request = client_connection.recv(4096).decode()
#     print(request)

#     # Parse HTTP headers
#     headers = request.split('\n')
#     filename = headers[0].split()[1]

#     response_type = "" # Will be replaced with the mime type of the file returned

#     # Get the content of the file
#     ## if at index
#     if filename == '/':
#         filename = 'index.html'

#     try:
#         if filename.endswith(".html"):
#             response_type = "text/html"
#             with open(f"{templates_foler}/{filename}", "r") as html_file:
#                 content = html_file.read()
#             response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

#         elif filename.endswith(".css"):
#             response_type = "text/css"
#             with open(f"{templates_foler}/{filename}", "r") as html_file:
#                 content = html_file.read()
#             response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

#         elif filename.endswith(".js"):
#             response_type = "text/js"
#             with open(f"{templates_foler}/{filename}", "r") as html_file:
#                 content = html_file.read()
#             response = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n' + content

#         # Images
#         elif filename.endswith(".jpg"):
#             response_type = "image/jpeg"
#             with open(f"{templates_foler}/{filename}", "rb") as image:
#                 content = image.read()
#             response = content
            
#         elif filename.endswith(".png"):
#             response_type = "image/png"
#             with open(f"{templates_foler}/{filename}", "rb") as image:
#                 content = image.read()
#             response = content

#         # Fonts
#         elif filename.endswith(".ttf"):
#             response_type = "font/ttf"
#             with open(f"{templates_foler}/{filename}", "rb") as font:
#                 content = font.read()
#             response = content
        
#         elif filename.endswith(".woff"):
#             response_type = "font/woff"
#             with open(f"{templates_foler}/{filename}", "rb") as font:
#                 content = font.read()
#             response = content

#         elif filename.endswith(".woff2"):
#             response_type = "font/woff2"
#             with open(f"{templates_foler}/{filename}", "rb") as font:
#                 content = font.read()
#             response = content

#     except FileNotFoundError: # Could not find the file
#         response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

#     # Send HTTP response

#     if type(response) == bytes:
#         header_config = f'HTTP/1.0 200 OK\ncontent-type: {response_type}\n\n'
#         client_connection.send(header_config.encode())
#         client_connection.send(response)
#     else:
#         client_connection.sendall(response.encode())

#     client_connection.close()

# # Close socket
# server_socket.close()

