import requests
import json
import sys

class requests_fb:
    def __init__(self,cookie):
        self.httpx = requests.Session()
        for item in cookie.split(";"):
            if "=" in item:
                name,value = item.strip().split("=",1)
                if "c_user" == name:
                    self.id_fb = value
                self.httpx.cookies.set(name,value)
        self.httpx.headers.update({
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
            'dpr': '1',
            'referer': 'https://www.facebook.com',
            'priority':'u=0, i',
            'sec-ch-prefers-color-scheme':'light',
            'sec-ch-ua':'"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-full-version-list':'"Chromium";v="142.0.7444.176", "Google Chrome";v="142.0.7444.176", "Not_A Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-model':'cors',
            'sec-ch-ua-platform':'"Windows"',
            'sec-ch-ua-platform-version':'"10.0.0"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        })

        self.header_post = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
        }


    def auto_like(self,id,type,proxies):
        
        id_ads = id
        type_id = "1635855486666999"
        if (type == "LOVE"):
            type_id = "1678524932434102"
        elif (type == "CARE"):
            type_id = "613557422527858"
        elif (type == "HAHA"):
            type_id = "115940658764963"
        elif (type == "WOW"):
            type_id = "478547315650144"
        elif (type == "SAD"):
            type_id = "908563459236466"
        elif (type == "ANGRY"):
            type_id = "444813342392137"
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',proxies=proxies).text
        try:
            fb_dtsg = form.split('"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return
        

        data = {
            "av": f"{self.id_fb}",
            "__user": f"{self.id_fb}",
            "fb_dtsg": f"{fb_dtsg}",
            "jazoest": f"{jazoest}",
            "lsd": f"{lsd}",
            "doc_id": "29333620026283566",  # Mã doc dùng cho CometUFIFeedbackReactMutation
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CometUFIFeedbackReactMutation",
            '__dyn': '',
            "variables": json.dumps({
                "input": {
                    "feedback_id": f"{feelback}",
                    "feedback_reaction_id": f"{type_id}",  # reaction type (VD: Like)
                    "feedback_source": "TAHOE",
                    "is_tracking_encrypted": True,
                    "tracking": [],
                    "actor_id": f"{self.id_fb}",
                    "client_mutation_id": "1"
                },
                "useDefaultActor": False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
            }),
            "server_timestamps": True
        }
        try:
            response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies,timeout=1)
        except:
            pass

    def auto_comment(self,id,Text, proxies):

        id_ads = id
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',proxies=proxies).text
        try:
            fb_dtsg = form.split('"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return

        data = {
            "av": f"{self.id_fb}",
            "__user": f"{self.id_fb}",
            "fb_dtsg": f"{fb_dtsg}",
            "jazoest": f"{jazoest}",
            "lsd": f"{lsd}",
            "doc_id": "9761804193899543",  # Mã doc dùng cho CometUFIFeedbackReactMutation
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "useCometUFICreateCommentMutation",
            '__dyn': '',
            "variables": json.dumps({
                "feedLocation":"NEWSFEED","feedbackSource":1,"groupID":None,
                "input": {
                    "feedback_id": f"{feelback}",
                    "feedback_source": "TAHOE",
                    "is_tracking_encrypted": True,
                    "tracking": [],
                    "actor_id": f"{self.id_fb}",
                    "client_mutation_id": "1",
                    "message":{"ranges":[],"text":f"{Text}"}
                },
                "useDefaultActor": False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
            }),
            "server_timestamps": True
        }
        

        try:
            response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies,timeout=1)
        except:
            pass