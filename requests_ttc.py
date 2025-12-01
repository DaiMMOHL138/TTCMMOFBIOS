import cloudscraper

class requests_ttc:
    def __init__(self):

        self.httpx = cloudscraper.create_scraper(
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                    'mobile': False
                }
            )

    def get_accout(self,access_token,url = "https://tuongtaccheo.com/logintoken.php"):
        data = {
            "access_token": access_token,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = self.httpx.post(url,data=data, headers=headers)

        if response.json()['status'] == "success":
            cookie = response.headers['Set-Cookie']
            main_cookie = cookie.split(';')[0]
            return response.json()['data'],main_cookie
        else:
            main_cookie = ""
            return "Nhập sai access_token hoặc tài khoản không tồn tại",main_cookie
    def datnick(self,idfb,cookie,url = "https://tuongtaccheo.com/cauhinh/datnick.php"):
        data = {
            "iddat[]": idfb,
            "loai": "fb",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.httpx.post(url, data=data, headers=headers)
    def get_jobs_like_vip(self,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_like_re(self,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipre/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_camxu_vip(self,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_camxu_re(self,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipre/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_comment(self,cookie,url = "https://tuongtaccheo.com/kiemtien/cmtcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    
    #GET coin

    def get_coin_jobs_like_vip(self,idpost,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/nhantien.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {
            "id": f"{idpost}",
        }
        response = self.httpx.post(url, headers=headers,data=data)
        return response.json()
    def get_coin_jobs_like_re(self,idpost,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipre/nhantien.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {
            "id": f"{idpost}",
        }
        response = self.httpx.post(url, headers=headers,data=data)
        return response.json()
    def get_coin_jobs_camxu_vip(self,type,idpost,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipcheo/nhantien.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {
            "id": f"{idpost}",
            "loaicx": type,
        }
        response = self.httpx.post(url, headers=headers,data=data)
        return response.json()
    def get_coin_jobs_camxu_re(self,type,idpost,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipre/nhantien.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {
            "id": f"{idpost}",
            "loaicx": type,
        }
        response = self.httpx.post(url, headers=headers,data=data)
        return response.json()
    def get_coin_jobs_comment(self,idpost,cookie,url = "https://tuongtaccheo.com/kiemtien/cmtcheo/nhantien.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {
            "id": f"{idpost}",
        }
        response = self.httpx.post(url, headers=headers,data=data)
        return response.json()
    