from colorama import Fore, Back, Style
import time, json, amino
import threading
import aminofix


with open('accounts.json') as f:
    accounts = json.load(f)

with open('info.json') as json_file:
    data = json.load(json_file)

com_link = data['community']
color = data["color"]
autocollection = data['automatic_collection']
blog_link = data['blog']
infernal_mode = data['infernal_mode']
proxy = data['proxy_list']
timer_infernal_mode = data['infernal_mode_time']
timer_default_mode = data['default_mode_time']

if infernal_mode:
    def collection():
        time.sleep(4)
    def generate():
        try:
            time.sleep(int(timer_infernal_mode))
        except:
            time.sleep(4.5)
    def cycle():
        time.sleep(60)
else:
    def collection():
        time.sleep(3)
    def generate():
        try:
            time.sleep(int(timer_default_mode))
        except:
            time.sleep(2)
    def cycle():
        time.sleep(30)

if color == 'red':
    visual = Back.RED
elif color == 'blue':
    visual = Back.BLUE
elif color == 'black':
    visual = Back.BLACK
elif color == 'cyan':
    visual = Back.CYAN
elif color == 'green':
    visual = Back.GREEN
elif color == 'white':
    visual = Back.WHITE
elif color == 'purple' or color == 'pink':
    visual = Back.MAGENTA
elif color == 'yellow' or color == 'orange':
    visual = Back.YELLOW
elif color == 'white':
    visual = Back.WHITE



erro = visual + Style.BRIGHT + Fore.WHITE + f"  ERRO  "
sucess = visual + Style.BRIGHT + Fore.WHITE + f"  SUCESS  "
join = visual + Style.BRIGHT + Fore.WHITE + f"  JOIN  "
logout = visual + Style.BRIGHT + Fore.WHITE + f"  LOGOUT  "

client_fix = aminofix.Client()
com_id = client_fix.get_from_code(code=com_link).comId


def tz_filter():
    localhour = time.strftime("%H", time.gmtime())
    localminute = time.strftime("%M", time.gmtime())
    UTC = {"GMT0": '+0', "GMT1": '+60', "GMT2": '+120', "GMT3": '+180', "GMT4": '+240', "GMT5": '+300', "GMT6": '+360',
        "GMT7": '+420', "GMT8": '+480', "GMT9": '+540', "GMT10": '+600', "GMT11": '+660', "GMT12": '+720',
        "GMT13": '+780', "GMT-1": '-60', "GMT-2": '-120', "GMT-3": '-180', "GMT-4": '-240', "GMT-5": '-300',
        "GMT-6": '-360', "GMT-7": '-420', "GMT-8": '-480', "GMT-9": '-540', "GMT-10": '-600', "GMT-11": '-660'}
    hour = [localhour, localminute]
    if hour[0] == "00": tz = UTC["GMT-1"]; return int(tz)
    if hour[0] == "01": tz = UTC["GMT-2"]; return int(tz)
    if hour[0] == "02": tz = UTC["GMT-3"]; return int(tz)
    if hour[0] == "03": tz = UTC["GMT-4"]; return int(tz)
    if hour[0] == "04": tz = UTC["GMT-5"]; return int(tz)
    if hour[0] == "05": tz = UTC["GMT-6"]; return int(tz)
    if hour[0] == "06": tz = UTC["GMT-7"]; return int(tz)
    if hour[0] == "07": tz = UTC["GMT-8"]; return int(tz)
    if hour[0] == "08": tz = UTC["GMT-9"]; return int(tz)
    if hour[0] == "09": tz = UTC["GMT-10"]; return int(tz)
    if hour[0] == "10": tz = UTC["GMT13"]; return int(tz)  # UTC["GMT-11"]
    if hour[0] == "11": tz = UTC["GMT12"]; return int(tz)
    if hour[0] == "12": tz = UTC["GMT11"]; return int(tz)
    if hour[0] == "13": tz = UTC["GMT10"]; return int(tz)
    if hour[0] == "14": tz = UTC["GMT9"]; return int(tz)
    if hour[0] == "15": tz = UTC["GMT8"]; return int(tz)
    if hour[0] == "16": tz = UTC["GMT7"]; return int(tz)
    if hour[0] == "17": tz = UTC["GMT6"]; return int(tz)
    if hour[0] == "18": tz = UTC["GMT5"]; return int(tz)
    if hour[0] == "19": tz = UTC["GMT4"]; return int(tz)
    if hour[0] == "20": tz = UTC["GMT3"]; return int(tz)
    if hour[0] == "21": tz = UTC["GMT2"]; return int(tz)
    if hour[0] == "22": tz = UTC["GMT1"]; return int(tz)
    if hour[0] == "23": tz = UTC["GMT0"]; return int(tz)

while True:
    def execute_account(account, number):
        try:
            client = amino.Client(account['device'], proxies=proxy)
            if client.login(account['email'], account['password']):
                print("\n\n" + Back.WHITE + f" {account['email']} I succeeded to enter: " + visual + Style.BRIGHT + f"  Cycle: {number}  "  + Style.RESET_ALL)
            if client.join_community(comId=com_id):
                print("\n\n" + Back.WHITE + Fore.BLACK + f" {account['email']} Joined the community {com_link}  " + sucess  + Style.RESET_ALL)

            sub_client = amino.SubClient(comId=com_id, profile=client.profile, autoChangeDev=False)
            try:
                if autocollection == True:
                    total_coins = client.get_wallet_info().totalCoins
                    blog_id = client.get_from_code(blog_link).objectId
                    zero = int("0")
                    quinhentos = int("500")
                    while total_coins > zero:
                        if total_coins >= quinhentos:
                            sub_client.send_coins(blogId=blog_id, coins=500)
                            print(Back.WHITE + Fore.BLACK + f" Sent 500 coins! " + sucess + Style.RESET_ALL)
                            total_coins -= 500
                            collection()
                        else:
                            sub_client.send_coins(blogId=blog_id, coins=total_coins)
                            print(Back.WHITE + Fore.BLACK + f" Sent {total_coins} coins! " + sucess + Style.RESET_ALL)
                            total_coins = 0
                            collection()
            except:
                pass

            tzf = tz_filter()
            for i in range(24):
                t = int(time.time() * 1000)
                try:
                    response = sub_client.send_active_obj(optInAdsFlags=2147483647, ts=t, tz=tzf, timers=[{"start": t, "end": t + 300} for _ in range(50)])
                    generate()
                except Exception as error:
                    print(Back.WHITE + Fore.BLACK + f" {account['email']} was not able to generate. {error}" + Style.RESET_ALL + erro + Style.RESET_ALL)
                    for j in range(3):
                        time.sleep(10)
                        try:
                            response = sub_client.send_active_obj(optInAdsFlags=2147483647, ts=t, tz=tzf, timers=[{"start": t, "end": t + 300} for _ in range(50)])
                            break
                        except Exception as error:
                            print(Back.WHITE + Fore.BLACK + f" {account['email']} was not able to generate after retry {j + 1}. {error}" + Style.RESET_ALL + erro + Style.RESET_ALL)
                            if j == 2:
                                print(Back.WHITE + Fore.BLACK + f" {account['email']} was not able to generate after {j + 1} retries. Moving on." + Style.RESET_ALL + erro + Style.RESET_ALL)
                print(Back.WHITE + Fore.BLACK + f" {account['email']} managed to generate! OK: {i+1} | {response} " + sucess + Style.RESET_ALL)

            client.logout()
            number += 1
            print(Back.WHITE + Fore.BLACK + f" {account['email']} finished its cycle " + visual + Style.BRIGHT +  Fore.WHITE + f"  LOGOUT  "  + Style.RESET_ALL)
            cycle()
        except json.JSONDecodeError:
            print(e)
            print(Back.WHITE + Fore.BLACK + f" Error in info.json or accounts information" + Style.RESET_ALL + erro + Style.RESET_ALL)
            exit()
        except aminofix.exceptions.TooManyRequests:
            print(Back.WHITE + Fore.BLACK + f" You have encountered the Too many requests error, please try again later." + Style.RESET_ALL + erro + Style.RESET_ALL)
            exit()
        except aminofix.exceptions.InvalidDevice:
            print(Back.WHITE + Fore.BLACK + f" The devices associated with your accounts are corrupted. Please delete a file on your device called 'device' or contact support." + Style.RESET_ALL + erro + Style.RESET_ALL)
            pass
        except Exception as e:
            print(Back.WHITE + Fore.BLACK + f" {account['email']} was not able to generate. {e}" + Style.RESET_ALL + erro + Style.RESET_ALL)
            pass

    number = 1
    if infernal_mode:
        threads = []
        for i in range(0, len(accounts), 2):
            t1 = threading.Thread(target=execute_account, args=(accounts[i], number))
            t2 = threading.Thread(target=execute_account, args=(accounts[i+1], number+1)) if i+1 < len(accounts) else None
            threads.append(t1)
            if t2:
                threads.append(t2)

            for thread in threads:
                if thread:
                    thread.start()

            for thread in threads:
                if thread:
                    thread.join()

            threads = []
            number += 2

    else:
        for account in accounts:
            execute_account(account=account, number=number)
            number += 1 