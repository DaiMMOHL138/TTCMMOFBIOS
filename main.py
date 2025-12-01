import sys
import colorama
import time
from random import randint
# -*- coding: utf-8 -*-

from requests_ttc import requests_ttc
from requests_fb import requests_fb
from setting import *

class Main():

    def __init__(self):
        colorama.init(autoreset=True)
        self.TTC = requests_ttc()
        self.list_cookie = []
        self.list_proxy = []
        self.tong_jobs = 0
        self.save_jobs = 0

    def input_access_token(self):
        access_token = input(f"{colorama.Fore.MAGENTA}Nhập access_token: ")
        if not access_token:
            print("Access token không được để trống.")
            sys.exit()
        else:
            return access_token
        
    def get_info_account(self, access_token):
        account_info, cookie = self.TTC.get_accout(access_token)
        if account_info == "Nhập sai access_token hoặc tài khoản không tồn tại":
            print(colorama.Fore.RED + account_info)
            sys.exit()
        else:
            user = account_info["user"]
            coin = account_info["sodu"]
            return cookie,user,coin
        
    def print_info_account(self, user, coin):
        print(colorama.Fore.GREEN + f"Tài khoản: {user}")
        print(colorama.Fore.GREEN + f"Coin: {coin}")

    def input_cookie_facebook_and_proxy(self):
        cookie_facebook = input(f"{colorama.Fore.MAGENTA}Nhập cookie facebook: ")
        proxy = input(f"{colorama.Fore.MAGENTA}Nhập proxy (nếu không có thì để trống): ")
        if proxy:
            try:
                ip, port, user, pwd = proxy.split(":")
                proxy_url = f"http://{user}:{pwd}@{ip}:{port}"
                print("Proxy URL:", proxy_url)
                proxies = {
                    "http": proxy_url,
                    "https": proxy_url
                }
            except ValueError:
                print("❌ Sai định dạng proxy. Định dạng đúng: ip:port:user:pass")
                sys.exit()
        else:
            proxies = {}
        if not cookie_facebook:
            print("Cookie facebook không được để trống.")
            sys.exit()
        else:
            return cookie_facebook, proxies
        
    def input_type_jobs(self):
        print(colorama.Fore.YELLOW + "Chọn loại công việc:")
        print(colorama.Fore.YELLOW + "1. Like bài viết VIP")
        print(colorama.Fore.YELLOW + "2. Like bài viết RE")
        print(colorama.Fore.YELLOW + "3. Cảm xúc bài viết VIP")
        print(colorama.Fore.YELLOW + "4. Cảm xúc bài viết RE")
        print(colorama.Fore.YELLOW + "5. Bình luận chéo")
        print(colorama.Fore.YELLOW + "VD:1,2,3,4,5")
        choice = input(f"{colorama.Fore.MAGENTA}Nhập lựa chọn của bạn (1-5):")
        
        if not choice:
            print("Lựa chọn không được để trống.")
            sys.exit()
        choices = choice.split(",")
        return choices
    def processes(self,choice,cookie, list_cookie, list_proxy, user, coin, sll = 1):
        self.coin = coin
        while True:
            for i in range(0,len(list_cookie)):
                cookie_fb = list_cookie[i]
                proxy = list_proxy[i]
                uid = cookie_fb.split("c_user=")[1].split(";")[0]
                print(colorama.Fore.GREEN + f"Đang đặt nick: {uid}...")
                time.sleep(2)
                self.TTC.datnick(uid, cookie)
                self.strat_sll(choice, cookie,cookie_fb, proxy, user, coin)
                self.save_jobs = 0
                print(colorama.Fore.GREEN + "Nghỉ 10s rồi mới chuyển acc mới...")
                delay(10)


    def strat_sll(self,choice,cookie,cookie_facebook, proxies,user,coin):
        while True:
            try:
                if self.save_jobs >= self.jobs_len:
                    print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                    break
                else:
                    if "1" in choice:
                        print(colorama.Fore.GREEN + "Đang lấy công việc Like bài viết VIP...",end="\r")
                        time.sleep(2)
                        data = self.TTC.get_jobs_like_vip(cookie)
                        
                        max = len(data)
                        if data == []:
                            print(colorama.Fore.RED + "Không có công việc Like bài viết VIP nào.",end="\r")
                            time.sleep(3)
                        else:
                            try:
                                for n in range(0,max):
                                    idpost = data[n]["idpost"]
                                    link = data[n]["link"]
                                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                    print(colorama.Fore.GREEN + f"Đang Like bài viết: {idpost}",end="\r")
                                    self.FB.auto_like(cookie_facebook, idfb,type = "",proxies = proxies)
                                    response = self.TTC.get_coin_jobs_like_vip(idpost,cookie)
                                    if response == {"mess": "Thành công, bạn đã được cộng 1100 xu"}:
                                        self.coin += 1100
                                        self.tong_jobs += 1
                                        self.save_jobs += 1
                                        print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{self.coin}{colorama.Fore.GREEN}|+1100|{colorama.Fore.MAGENTA}LIKE VIP        ')
                                        delay(randint(min_delay,max_delay))
                                    if self.save_jobs >= int(self.jobs_len):
                                        print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                                        return
                                
                            except KeyboardInterrupt:
                                print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                                sys.exit()
                            except:
                                delay(int(data["countdown"]+3))
                    if "2" in choice:
                        print(colorama.Fore.GREEN + "Đang lấy công việc Like bài viết RE...",end="\r")
                        time.sleep(2)
                        data = self.TTC.get_jobs_like_re(cookie)
                        max = len(data)
                        if data == []:
                            print(colorama.Fore.RED + "Không có công việc Like bài viết RE nào.",end="\r")
                            time.sleep(3)
                        else:
                            try:
                                for n in range(0,max):
                                    idpost = data[n]["idpost"]
                                    link = data[n]["link"]
                                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                    print(colorama.Fore.GREEN + f"Đang Like bài viết: {idpost}",end="\r")
                                    self.FB.auto_like(cookie_facebook, idfb,type = "",proxies = proxies)
                                    response = self.TTC.get_coin_jobs_like_re(idpost,cookie)
                                    if response == {"mess": "Thành công, bạn đã được cộng 400 xu"}:
                                        self.coin += 400
                                        self.tong_jobs += 1
                                        self.save_jobs += 1
                                        print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{self.coin}{colorama.Fore.GREEN}|+400|{colorama.Fore.MAGENTA}LIKE RE        ')
                                        delay(randint(min_delay,max_delay))
                                    if self.save_jobs >= int(self.jobs_len):
                                        print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                                        return
                            except KeyboardInterrupt:
                                print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                                sys.exit()
                            except:
                                delay(int(data["countdown"]+3))
                    if "3" in choice:
                        print(colorama.Fore.GREEN + "Đang lấy công việc CX bài viết VIP...",end="\r")
                        time.sleep(2)
                        data = self.TTC.get_jobs_camxu_vip(cookie)
                        max = len(data)
                        if data == []:
                            print(colorama.Fore.RED + "Không có công việc CX bài viết VIP nào.",end="\r")
                            time.sleep(3)
                        else:
                            try:
                                for n in range(0,max):
                                    idpost = data[n]["idpost"]
                                    link = data[n]["link"]
                                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                    type = data[n]["loaicx"]
                                    print(colorama.Fore.GREEN + f"Đang CX bài viết: {idpost}",end="\r")
                                    self.FB.auto_like(cookie_facebook, idfb,type = type,proxies = proxies)
                                    response = self.TTC.get_coin_jobs_camxu_vip(type,idpost,cookie)
                                    if response == {"mess": "Thành công, bạn đã được cộng 1100 xu"}:
                                        self.coin += 1100
                                        self.tong_jobs += 1
                                        self.save_jobs += 1
                                        print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{self.coin}{colorama.Fore.GREEN}|+1100|{colorama.Fore.MAGENTA}CX VIP        ')
                                        delay(randint(min_delay,max_delay))
                                    if self.save_jobs >= int(self.jobs_len):
                                        print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                                        return
                                
                            except KeyboardInterrupt:
                                print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                                sys.exit()
                            except:
                                delay(int(data["countdown"]+3))
                    if "4" in choice:
                        print(colorama.Fore.GREEN + "Đang lấy công việc CX bài viết RE...",end="\r")
                        time.sleep(2)
                        data = self.TTC.get_jobs_camxu_re(cookie)
                        max = len(data)
                        if data == []:
                            print(colorama.Fore.RED + "Không có công việc CX bài viết RE nào.",end="\r")
                            time.sleep(3)
                        else:
                            try:
                                for n in range(0,max):
                                    idpost = data[n]["idpost"]
                                    link = data[n]["link"]
                                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                    type = data[n]["loaicx"]
                                    print(colorama.Fore.GREEN + f"Đang CX bài viết: {idpost}",end="\r")
                                    self.FB.auto_like(cookie_facebook, idfb,type = type,proxies = proxies)
                                    response = self.TTC.get_coin_jobs_camxu_re(type,idpost,cookie)
                                    if response == {"mess": "Thành công, bạn đã được cộng 400 xu"}:
                                        self.coin += 400
                                        self.tong_jobs += 1
                                        self.save_jobs += 1
                                        print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{self.coin}{colorama.Fore.GREEN}|+400|{colorama.Fore.MAGENTA}CX RE         ')
                                        delay(randint(min_delay,max_delay))
                                    if self.save_jobs >= int(self.jobs_len):
                                        print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                                        return
                                
                            except KeyboardInterrupt:
                                print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                                sys.exit()
                            except:
                                delay(int(data["countdown"]+3))
                    if "5" in choice:
                
                        print(colorama.Fore.GREEN + "Đang lấy công việc CMT chéo...",end="\r")
                        time.sleep(2)
                        data = self.TTC.get_jobs_comment(cookie)
                        max = len(data)
                        if data == []:
                            print(colorama.Fore.RED + "Không có công việc CMT chéo nào.",end="\r")
                            time.sleep(3)
                        else:
                            try:
                                for n in range(0,max):
                                    idpost = data[n]["idpost"]
                                    link = data[n]["link"]
                                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                    type = data[n]["nd"]
                                    text = type.split('"')[1].split('"')[0]
                                    print(colorama.Fore.GREEN + f"Đang CMT chéo bài viết: {idpost}",end="\r")
                                    self.FB.auto_comment(cookie_facebook, idfb,text, proxies = proxies)
                                    response = self.TTC.get_coin_jobs_comment(idpost,cookie)
                                    if response == {'mess': 'Thành công, bạn được cộng 1400 xu'}:
                                        self.coin += 1400
                                        self.tong_jobs += 1
                                        self.save_jobs += 1
                                        print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{self.coin}{colorama.Fore.GREEN}|+1400|{colorama.Fore.MAGENTA}CMT          ')
                                        delay(randint(min_delay,max_delay))
                                    if self.save_jobs >= int(self.jobs_len):
                                        print(colorama.Fore.GREEN + f"Đã hoàn thành {self.save_jobs} jobs, chuyển acc mới...")
                                        return
                            except KeyboardInterrupt:
                                print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                                sys.exit()
                            except:
                                delay(int(data["countdown"]+3))
            except TimeoutError as e:
                print(e)
                print(colorama.Fore.RED + "Lỗi kết nối. Vui lòng kiểm tra lại mạng.")
                time.sleep(5)
            except Exception as e:
                print(e)
                print(colorama.Fore.RED + "Đã xảy ra lỗi trong quá trình lấy công việc. Vui lòng thử lại sau.")
                pass
        
    def strat(self,choice,cookie,cookie_facebook, proxies,user,coin):
        while True:
            if "1" in choice:
                print(colorama.Fore.GREEN + "Đang lấy công việc Like bài viết VIP...",end="\r")
                time.sleep(2)
                data = self.TTC.get_jobs_like_vip(cookie)
                max = len(data)
                if data == []:
                    print(colorama.Fore.RED + "Không có công việc Like bài viết VIP nào.",end="\r")
                    time.sleep(3)
                else:
                    try:
                        for n in range(0,max):
                            idpost = data[n]["idpost"]
                            link = data[n]["link"]
                            idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                            print(colorama.Fore.GREEN + f"Đang Like bài viết: {idpost}",end="\r")
                            requests_fb(cookie_facebook).auto_like(idfb,type = "",proxies = proxies)
                            delay(randint(min_delay,max_delay))
                            response = self.TTC.get_coin_jobs_like_vip(idpost,cookie)
                            if response == {"mess": "Thành công, bạn đã được cộng 1100 xu"}:
                                coin += 1100
                                self.tong_jobs += 1
                                print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{coin}{colorama.Fore.GREEN}|+1100|{colorama.Fore.MAGENTA}LIKE VIP        ')
                            
                                
                        
                    except KeyboardInterrupt:
                        print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                        sys.exit()
                    except:
                        delay(int(data["countdown"]+3))
            if "2" in choice:
                print(colorama.Fore.GREEN + "Đang lấy công việc Like bài viết RE...",end="\r")
                time.sleep(2)
                data = self.TTC.get_jobs_like_re(cookie)
                max = len(data)
                if data == []:
                    print(colorama.Fore.RED + "Không có công việc Like bài viết RE nào.",end="\r")
                    time.sleep(3)
                else:
                    try:
                        for n in range(0,max):
                            idpost = data[n]["idpost"]
                            link = data[n]["link"]
                            idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                            print(colorama.Fore.GREEN + f"Đang Like bài viết: {idpost}",end="\r")
                            requests_fb(cookie_facebook).auto_like(idfb,type = "",proxies = proxies)
                            delay(randint(min_delay,max_delay))
                            response = self.TTC.get_coin_jobs_like_re(idpost,cookie)
                            if response == {"mess": "Thành công, bạn đã được cộng 400 xu"}:
                                coin += 400
                                self.tong_jobs += 1
                                print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{coin}{colorama.Fore.GREEN}|+400|{colorama.Fore.MAGENTA}LIKE RE        ')
                            
                        
                    except KeyboardInterrupt:
                        print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                        sys.exit()
                    except:
                        delay(int(data["countdown"]+3))
            if "3" in choice:
                print(colorama.Fore.GREEN + "Đang lấy công việc CX bài viết VIP...",end="\r")
                time.sleep(2)
                data = self.TTC.get_jobs_camxu_vip(cookie)
                max = len(data)
                if data == []:
                    print(colorama.Fore.RED + "Không có công việc CX bài viết VIP nào.",end="\r")
                    time.sleep(3)
                else:
                    try:
                        for n in range(0,max):
                            idpost = data[n]["idpost"]
                            link = data[n]["link"]
                            idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                            type = data[n]["loaicx"]
                            print(colorama.Fore.GREEN + f"Đang CX bài viết: {idpost}",end="\r")
                            requests_fb(cookie_facebook).auto_like(idfb,type = type,proxies = proxies)
                            delay(randint(min_delay,max_delay))
                            response = self.TTC.get_coin_jobs_camxu_vip(type,idpost,cookie)
                            if response == {"mess": "Thành công, bạn đã được cộng 1100 xu"}:
                                coin += 1100
                                self.tong_jobs += 1
                                print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{coin}{colorama.Fore.GREEN}|+1100|{colorama.Fore.MAGENTA}CX VIP        ')
                            
                        
                    except KeyboardInterrupt:
                        print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                        sys.exit()
                    except:
                        delay(int(data["countdown"]+3))
            if "4" in choice:
                print(colorama.Fore.GREEN + "Đang lấy công việc CX bài viết RE...",end="\r")
                time.sleep(2)
                data = self.TTC.get_jobs_camxu_re(cookie)
                max = len(data)
                if data == []:
                    print(colorama.Fore.RED + "Không có công việc CX bài viết RE nào.",end="\r")
                    time.sleep(3)
                else:
                    try:
                        for n in range(0,max):
                            idpost = data[n]["idpost"]
                            link = data[n]["link"]
                            idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                            type = data[n]["loaicx"]
                            print(colorama.Fore.GREEN + f"Đang CX bài viết: {idpost}",end="\r")
                            requests_fb(cookie_facebook).auto_like(idfb,type = type,proxies = proxies)
                            delay(randint(min_delay,max_delay))
                            response = self.TTC.get_coin_jobs_camxu_re(type,idpost,cookie)
                            if response == {"mess": "Thành công, bạn đã được cộng 400 xu"}:
                                coin += 400
                                self.tong_jobs += 1
                                print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{coin}{colorama.Fore.GREEN}|+400|{colorama.Fore.MAGENTA}CX RE         ')
                            
                        
                    except KeyboardInterrupt:
                        print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                        sys.exit()
                    except:
                        delay(int(data["countdown"]+3))
            if "5" in choice:
                    print(colorama.Fore.GREEN + "Đang lấy công việc CMT chéo...",end="\r")
                    time.sleep(2)
                    data = self.TTC.get_jobs_comment(cookie)
                    max = len(data)
                    print(data)
                    if data == []:
                        print(colorama.Fore.RED + "Không có công việc CMT chéo nào.",end="\r")
                        time.sleep(3)
                    else:
                        try:
                            for n in range(0,max):
                                idpost = data[n]["idpost"]
                                link = data[n]["link"]
                                idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                                type = data[n]["nd"]
                                text = type.split('"')[1].split('"')[0]
                                print(colorama.Fore.GREEN + f"Đang CMT chéo bài viết: {idpost}",end="\r")
                                requests_fb(cookie_facebook).auto_comment(idfb,text, proxies = proxies)
                                delay(randint(min_delay,max_delay))
                                response = self.TTC.get_coin_jobs_comment(idpost,cookie)
                                if response == {'mess': 'Thành công, bạn được cộng 1400 xu'}:
                                    coin += 1400
                                    self.tong_jobs += 1
                                    print(f'{colorama.Fore.GREEN}{self.tong_jobs}|{colorama.Fore.YELLOW}{time.strftime("%H:%M:%S", time.localtime())}{colorama.Fore.GREEN}|{colorama.Fore.RED}{user}{colorama.Fore.GREEN}|{colorama.Fore.CYAN}{coin}{colorama.Fore.GREEN}|+1400|{colorama.Fore.MAGENTA}CMT          ')
                                
                        except KeyboardInterrupt:
                            print(colorama.Fore.RED + "Người dùng đã dừng lại.")
                            sys.exit()
                        except:
                            delay(int(data["countdown"]+3))     

    def run(self):
        clear_screen()
        print(colorama.Fore.GREEN+title)
        access_token = self.input_access_token()
        print(colorama.Fore.GREEN + "Đang lấy thông tin tài khoản...")
        time.sleep(3)
        cookie, user, coin = self.get_info_account(access_token)
        clear_screen()
        print(colorama.Fore.GREEN + title)
        self.print_info_account(user, coin)
        ask_sll = input(f"{colorama.Fore.MAGENTA}Bạn có muốn chạy nhiều nick không? (y/n): ").strip().lower()
        if ask_sll not in ["y", "n"]:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")
            sys.exit()
        elif ask_sll == "n":
            cookie_facebook,proxy = self.input_cookie_facebook_and_proxy()
            print(colorama.Fore.GREEN + "Đang đặt nick...")
            time.sleep(3)
            uid = cookie_facebook.split("c_user=")[1].split(";")[0]
            self.TTC.datnick(uid, cookie)
            clear_screen()
            print(colorama.Fore.GREEN + title)
            choice = self.input_type_jobs()
            self.strat(choice, cookie, cookie_facebook, proxy, user, coin)
        elif ask_sll == "y":
            print(colorama.Fore.GREEN + "Tối đa nick có thể chạy là 35 nick.")
            while True:
                cookie_facebook, proxy = self.input_cookie_facebook_and_proxy()
                self.list_cookie.append(cookie_facebook)
                self.list_proxy.append(proxy)
                ask = input(f"{colorama.Fore.MAGENTA}Bạn có muốn thêm nick khác không? (y/n): ").strip().lower()
                if ask not in ["y", "n"]:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")
                    sys.exit()
                elif ask == "n":
                    break
                elif ask == "y":
                    continue
                elif len(self.list_cookie) >= 35:
                    print(colorama.Fore.RED + "Đã đạt giới hạn tối đa 35 nick.")
                    break
        clear_screen()
        print(colorama.Fore.GREEN + title)
        choice = self.input_type_jobs()
        self.jobs_len = int(input(f"{colorama.Fore.MAGENTA}Bao nhiêu jobs thì chuyển acc:"))
        self.processes(choice,cookie,list_cookie=self.list_cookie, list_proxy=self.list_proxy, user=user, coin=coin, sll= 1)

if __name__ == "__main__":
    main = Main()
    main.run()