import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art
def display_banner():
    banner = """
         _    _ __  __  _____          _____ 
     /\   | |  | |  \/  |/ ____|  /\    / ____|
    /  \  | |__| | \  / | (___   /  \  | (___  
   / /\ \ |  __  | |\/| |\___ \ / /\ \  \___ \ 
  / ____ \| |  | | |  | |____) / ____ \ ____) |
 /_/    \_\_|  |_|_|  |_|_____/_/    \_\_____/ 

 Pixelcraftch
                                               
    """
    print(banner)

# Function to test the connection to the host
def test_connection(url):
    print("Testing connection...")
    for attempt in range(3):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Testing connection... [{Fore.GREEN}{response.status_code}{Style.RESET_ALL}]")
                return True
            else:
                print(f"Testing connection... [{Fore.RED}{response.status_code}{Style.RESET_ALL}]")
        except requests.RequestException:
            print(f"Testing connection... [{Fore.RED}Failed{Style.RESET_ALL}]")
    print("Host down.")
    return False

# Function to send requests with different HTTP methods
def send_requests(url):
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']
    responses = []
    for method in methods:
        response = requests.request(method, url)
        status_code = response.status_code
        color = Fore.GREEN if status_code == 200 else Fore.YELLOW if status_code == 403 else Fore.RED
        print(f"{method} Request [{color}{status_code}{Style.RESET_ALL}]")
        responses.append((method, status_code))
        if method == 'POST' and status_code == 200:
            check_http_pollution(url)
    return responses

# Function to attempt request smuggling for 403 responses
def smuggle_request(url, method, level=1):
    print(f"Attempting to smuggle {method} request...")
    smuggle_methods = [
        'X-HTTP-Method-Override', 'X-HTTP-Method', 'X-Method-Override', 'X-Method',
        'X-HTTP-Method-Override-2', 'X-HTTP-Method-Override-3', 'X-HTTP-Method-Override-4', 'X-HTTP-Method-Override-5'
    ]
    if level == 2:
        smuggle_methods.extend(['X-HTTP-Method-Override-6', 'X-HTTP-Method-Override-7'])

    for smuggle_method in smuggle_methods:
        headers = {smuggle_method: method}
        response = requests.post(url, headers=headers)
        status_code = response.status_code
        color = Fore.GREEN if status_code == 200 else Fore.RED
        print(f"Smuggled {method} Request with {smuggle_method} [{color}{status_code}{Style.RESET_ALL}]")
        if status_code != 403:
            return True
    return False

# Function to check for HTTP pollution vulnerability
def check_http_pollution(url):
    payload = {'param': 'value', 'param': 'pollution'}
    response = requests.post(url, data=payload)
    if 'pollution' in response.text:
        user_input = input("A Potential HTTP Pollution vuln found. Do you want to scan for that also? Y/n: ")
        if user_input.lower() in ['y', '']:
            print("Scanning for HTTP pollution vulnerability...")
            # Add detailed scanning logic here
        else:
            print("Skipping HTTP pollution scan.")

def main():
    display_banner()
    url = input("Enter the target URL with http/https: ")
    if test_connection(url):
        responses = send_requests(url)
        print("Scan COMPLETED")
        for method, status_code in responses:
            if status_code == 403:
                success = smuggle_request(url, method)
                if not success:
                    user_input = input("Do you want to extend the injection level? level=2 Y/n: ")
                    if user_input.lower() in ['y', '']:
                        smuggle_request(url, method, level=2)
                    break

if __name__ == "__main__":
    main()
