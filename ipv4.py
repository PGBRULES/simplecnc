import socket
def valid(address):#Check if an ipv4 address is valid. See: https://stackoverflow.com/a/4017219 for credits. 
    address = str(address)
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  
        return False

    return True
