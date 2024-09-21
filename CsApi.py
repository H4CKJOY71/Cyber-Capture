import requests

def capture_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('/sdcard/api_capture.txt', 'w') as file:
            file.write(response.text)
        print("API captured successfully and saved to /sdcard/api_capture.txt")
    else:
        print("Failed to capture API. Status code:", response.status_code)
print("\033[34;1m[YOUR LOGO]\033[34;1m")

print("""
 
    _______         __                    _______  __                                     
|   _   |.--.--.|  |--..-----..----.  |   _   ||  |.---.-..--.--..-----..----..-----.  
|.  1___||  |  ||  _  ||  -__||   _|  |   1___||  ||  _  ||  |  ||  -__||   _||__ --|  
|.  |___ |___  ||_____||_____||__|    |____   ||__||___._||___  ||_____||__|  |_____|  
|:  1   ||_____|                      |:  1   |           |_____|                      
|::.. . |                             |::.. . |                                        
`-------'                             `-------'                                        
                                                                                       
                                                            
       
                 
""")

print("\033[31;1mAuthor  :Joyonto Barua\033[34;1m")
print("\033[31;1mGithub  :H4CKJOY71\033[34;1m")
print("\033[31;1mPage Name. :Cyber Slayer\033[34;1m")
print("\033[31;1mFacebook profile. :https://www.facebook.com/profile.php?id=100094606141428")
print("\033[34;1mFacebook Name:Joyonto Barua\033[34;1m")

if __name__ == "__main__":
    website_url = input("Please enter the website URL: ")
    capture_api(website_url)
