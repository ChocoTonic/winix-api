import os
from pprint import pprint
from dotenv import load_dotenv
from winix_api.winix_account import WinixAccount

def main():
    """Entry point for Winix device listing."""
    load_dotenv()
    username = os.getenv("WINIX_USERNAME")
    password = os.getenv("WINIX_PASSWORD")
    if not username or not password:
        username = input("Enter Winix username: ")
        password = input("Enter Winix password: ")

    account = WinixAccount.from_credentials(username, password)
    devices = account.devices
    print(f"Found {len(devices)} devices:")
    for device in devices:
        pprint(device.__dict__)

if __name__ == "__main__":
    main()
