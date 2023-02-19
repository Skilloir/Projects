import requests
import threading
import webbrowser

data = {
    "username": "#######",
    "password": "#######"
}

url = "https://3328.mykidsbank.org/"

def login():
    while True:
        loginRequest = requests.post(url, data=data)
        if loginRequest.status_code == 200:
            print(loginRequest.text)
            print("Login success")
        else:
            print(loginRequest.status_code)
            print("Login Failed")

threads = []

for i in range(1):
    t = threading.Thread(target=login)
    t.daemon = True
    threads.append(t)

for i in range(1):
    threads[i].start()

for i in range(1):
    threads[i].join()




# NEW TESTING STUFF
def browserLogin():
    webbrowser.open("https://3328.mykidsbank.org/login")
    web

browserLogin()








