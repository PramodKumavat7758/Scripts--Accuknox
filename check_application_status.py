import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.ConnectionError:
        return 'down'

def main():
    url = input("Enter the URL of the application: ")
    while True:
        status = check_application_status(url)
        print(f"Application status: {status}")
        time.sleep(60)  

if __name__ == "__main__":
    main()
