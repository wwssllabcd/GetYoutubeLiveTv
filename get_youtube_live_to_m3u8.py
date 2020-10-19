
import sys
sys.path.append(r'D:\GitHub\Python')
from EricCorePy.Utility.EricUtility import EricUtility
from EricCorePy.Utility.UrlUtility import UrlUtility
from EricCorePy.Utility.ReUtility import ReUtility
from EricCorePy.Utility.M3u8 import M3u8


crlf = "\n"

urlList = [
    ("12-華視新聞", "https://www.youtube.com/watch?v=HvqBnBVNRuw")
    ,("13-公共電視", "https://www.youtube.com/watch?v=ED4QXd5xAco")
    ,("51-東森新聞台", "https://www.youtube.com/watch?v=63RmMXCd_bQ")
    ,("52-中天新聞台", "https://www.youtube.com/watch?v=wUPPkSANpyo")
    ,("53-民視新聞台", "https://www.youtube.com/watch?v=XxJKnDLYZz4")
    ,("54-三立新聞台", "https://www.youtube.com/watch?v=4ZVUmEUFwaY")
    ,("55-TVBS新聞台", "https://www.youtube.com/watch?v=A4FbB8UhNRs")
    ,("57-東森財經新聞", "https://www.youtube.com/watch?v=68lLQ7hkdzU")
    ,("154-中視新聞台", "https://www.youtube.com/watch?v=ptqD4qo9D3I")
    ,("155-台視新聞", "https://www.youtube.com/watch?v=xL0ch83RAK8")

    ,("公視台語台", "https://www.youtube.com/watch?v=iTz7AfRrxH4")
    ,("新唐人LIVE", "https://www.youtube.com/watch?v=wSKE3A40SIk")

    #Japan
    ,("JapaNews24", "https://www.youtube.com/watch?v=coYw-eVU0Ks")

    #korea
    ,("KBS", "https://www.youtube.com/watch?v=xgGpYcnPKH8")
    ,("YTN", "https://www.youtube.com/watch?v=U_sYIKWhJvk")

    #American
    ,("CNN News18 ", "https://www.youtube.com/watch?v=YYYE1FHh5sM")
    ,("NBC News", "https://www.youtube.com/watch?v=H6-1NnJZHAw")
    ,("NBC2 live", "https://www.youtube.com/watch?v=tPeUHECNLKs")
    ,("Bloomberg Financial News", "https://www.youtube.com/watch?v=dp8PhLsUcFE")

    #Australia
    ,("ABC News", "https://www.youtube.com/watch?v=W1ilCy6XrmI")

    #UK
    ,("Sky News", "https://www.youtube.com/watch?v=9Auq9mYxFEE")

    #Singapore
    ,("CNA", "https://www.youtube.com/watch?v=XWq5kBlakcQ")

    #Euronews
    ,("Euronews English", "https://www.youtube.com/watch?v=s8KklUefbWA")
    ,("FRANCE 24 English ", "https://www.youtube.com/watch?v=oaugY_Yn6Yw")

    #German 
    ,("DW News", "https://www.youtube.com/watch?v=gOoTbPssAo4")

    #Turkey
    ,("TRTWORLD", "https://www.youtube.com/watch?v=CV5Fooi8YJA")

    #Russian
    ,("RT News", "https://www.youtube.com/watch?v=NvCSr7qzAAM")
    
    #India
    ,("India Today", "https://www.youtube.com/watch?v=8UJMH_VIRhU")
]

urlU = UrlUtility()
reu = ReUtility()
m3u8U = M3u8()

resList = []
for urlObj in urlList:
    htmldata = urlU.get_url_data(urlObj[1])
    res = reu.get_between_string(htmldata, "m3u8", "http", "m3u8")
    res = res.replace('\/', '/')
    resList.append((urlObj[0], res))

m3u8 = m3u8U.get_m3u8_head_string()
for obj in resList:
    m3u8 += m3u8U.get_m3u8_item_string(obj[0], obj[1])

print(m3u8)

