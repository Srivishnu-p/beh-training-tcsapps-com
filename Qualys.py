import requests

# Qualys API credentials and endpoint
QUALYS_API_URL = "https://qualysapi.qualys.com/api/2.0/fo/"
USERNAME = "your_username"
PASSWORD = "your_password"

# Function to authenticate and get a session token
def get_session_token():
    auth_url = f"{QUALYS_API_URL}/session/"
    payload = {
        "action": "login",
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.post(auth_url, data=payload)
    if response.status_code == 200:
        return response.headers["X-Session-Token"]
    else:
        raise Exception(f"Authentication failed: {response.status_code} - {response.text}")

# Function to logout and invalidate the session token
def logout_session(session_token):
    logout_url = f"{QUALYS_API_URL}/session/"
    headers = {
        "X-Requested-With": "Python Script",
        "Authorization": f"Bearer {session_token}",
    }
    payload = {
        "action": "logout",
    }
    response = requests.post(logout_url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Session logged out successfully.")
    else:
        print(f"Logout failed: {response.status_code} - {response.text}")

# Function to launch a scan
def launch_scan(session_token, scan_title, target_ip):
    scan_url = f"{QUALYS_API_URL}/scan/"
    headers = {
        "X-Requested-With": "Python Script",
        "Authorization": f"Bearer {session_token}",
    }
    payload = {
        "action": "launch",
        "scan_title": scan_title,
        "ip": target_ip,
        "option_title": "Your_Scan_Profile",  # Replace with your scan profile
    }
    response = requests.post(scan_url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.text  # Returns XML with scan reference number
    else:
        raise Exception(f"Scan launch failed: {response.status_code} - {response.text}")

# Main function
def main():
    session_token = None
    try:
        # Step 1: Authenticate and get session token
        session_token = get_session_token()
        print("Session token obtained.")

        # Step 2: Launch a scan
        scan_title = "My_Scan_Title"
        target_ip = "192.168.1.1"  # Replace with your target IP or range
        scan_response = launch_scan(session_token, scan_title, target_ip)
        print("Scan launched successfully.")

        # Extract scan reference number from the response
        scan_ref = scan_response.split("<REFERENCE>")[1].split("</REFERENCE>")[0]
        print(f"Scan reference: {scan_ref}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Step 3: Logout and invalidate the session token
        if session_token:
            logout_session(session_token)

if __name__ == "__main__":
    main()
