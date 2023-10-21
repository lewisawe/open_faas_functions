import socket
import json

def check_port_status(event, context):
    try:
        port = int(event['body'])  # Get the port number from the request data
        hostname = socket.gethostname()  # Get the hostname
        ip_address = socket.gethostbyname(hostname)  # Get the IP address

        # Check if the port is open or closed
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        sock.close()

        if result == 0:
            status = f"Port {port}: OPEN"
        else:
            status = f"Port {port}: CLOSED"

        # Prepare the response JSON
        response = {
            "status": status
        }

        # Return the JSON response
        return json.dumps(response)

    except Exception as e:
        # Handle exceptions and return an error response
        error_response = {
            "error": str(e)
        }
        return json.dumps(error_response)
