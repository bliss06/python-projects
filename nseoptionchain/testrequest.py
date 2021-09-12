import requests
urlval = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
cookieval = 'Cookie: _ga=GA1.2.1735051097.1517463640; RT="z = 1 & dm = nseindia.com & si = bd861a45-798a-413b-a8af-b1cc5598bf1b & ss = korl1dyy & sl = 3 & tt = 5nr & bcn = %2F % 2F684fc53d.akstat.io % 2F & ld = 31v3 & nu = ed8553192c8d124be55949cc1b2e99dc & cl = 91nw"; JSESSIONID=612DC35ACBB14EF169B200B757085DF9.tomcat2; NSE-TEST-1=1927290890.20480.0000; nsit=Muw7nlZ_8ibAr5wA5tWtpKAx; AKA_A2=A; ak_bmsc=CB29F13A87A2C343ECB1CDBF50E4AEA8170346370A780000FE74A160284B7E50~plAQmEUpctgLhxrlOguMnb2bnL5JoMxPli81qqa/03JPJ+U0+vroRmBH7LAVIBXEAxA9LlT4PVWSlYjEToD8yRgCa6tllBbd7gtaWPo7FIvnoPfDcBXGv+e/SNcq73SptmnldQPNKiIjvETZr0niIBI8BbjuFkrwVc7OG26QJmKL+DDZV1zCUMt5/ru12+BDtrCjzmiIkdEZXnqPvQK5UCtlaj/G6NtrWiWxaCZDIZhxBnQOBJs/qciZrqGKdDNT7m; _gid=GA1.2.1955822214.1621193984; bm_sv=F957E7C3D54BFCEFD261107AAA57A4E6~rdiEXo34lxbk46cABSTC7FbzgEvdRPXw1yYR8TQd4GnEmQplYfXQK3ryDxihY2ZQU80loJhXSTvnb3ucfbRcwILlqYKd7Wt68W7yFk1XrxPmrd2vK3yJWZL2t7qmmx1y3tOtCbS54R+3dK99KUiLiz2kpah9HS1whjeamQYcK6s=; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYyMTE5NDEyMCwiZXhwIjoxNjIxMTk3NzIwfQ.VOUUKyB0a67lzBQ65mbarWSQ3NkG93f9RquGAATEWU8'
refval = "https://www.nseindia.com/option-chain"
useragentval = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
accept_encval = "gzip, deflate, br"
cookie_dict = {
    "_ga": "GA1.2.1735051097.1517463640",
    "_gat_UA-143761337-1": "1",
    "_gid": "GA1.2.1955822214.1621193984",
    "ak_bmsc": "6FD08BAAA19FF1B5857994C648277AAD170346370A780000D60EA2605667743C~plw8wc9y/uuZZlwVPJYRXK12zBHg3Uwy4Qo9K6re9XjxDz5pFpBNFyVCD3/1415TpItqnGOIv7rEyjOOIJyGOpoDdDWcvz3vZ/7Y0SIXkq+qTbeAVIsjKUyW137akodlknrU/C/JCMbgPPl3zPBE9bcmS6zA35EvidPkPUXKqj8XoK0bTqXW3CrmgnhMSMNdFUtPJ7PRcg7cKf/Xw4VuhgK9TJCryb2S6yUyUfPXvNJp2arahZQHM0TjGo/gJp/mI6",
    "AKA_A2": "A",
    "bm_sv": "FDE716D2093676C1F80411EB7E0FC533~rdiEXo34lxbk46cABSTC7Cmktufnj1gIWcP5LlcMrujqVlWpbvFkLJ+8TPctGthblraxmNo9xudlGthUz2/QmckPB/nInu2nXxmZ7l53cKY73xTtbZ2FvBK7yGcD9EMt1HA6LRbFqmZqXSn0XWhvi9Rk9aSpmOzsUU8Fv/VAz1w=",
    "JSESSIONID": "612DC35ACBB14EF169B200B757085DF9.tomcat2",
    "NSE-TEST-1": "1927290890.20480.0000",
    "nseappid": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYyMTIzMzM3NSwiZXhwIjoxNjIxMjM2OTc1fQ.i_ZtiUEzL0iLd9zFORF5T3YWzsCCsWaQCOxxbldiS5Y",
    "nsit": "a6d_stpt9kCd5B8GGAnnAW60",
    "RT": "\"z=1&dm=nseindia.com&si=bd861a45-798a-413b-a8af-b1cc5598bf1b&ss=kos8hjnu&sl=2&tt=2tk&bcn=//684fc53e.akstat.io/&ld=8jb\""
}
response = requests.get(urlval, cookies=cookie_dict, headers={
    'Accept-Encoding': accept_encval, 'Referer': refval, 'User-Agent': useragentval})

json_response = response.json()
print(json_response)
