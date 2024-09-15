
import sys

sys.path.append(r'D:\GitHub\Python')

from EricCorePy.Utility.EricUtility import EricUtility
from EricCorePy.Utility.UrlUtility import UrlUtility
from EricCorePy.Utility.ReUtility import ReUtility
from EricCorePy.Utility.M3u8 import M3u8
from EricCorePy.Utility.MyThread import MyThread

crlf = "\n"

urlList = [
    
    ("13-公視新聞", "https://www.youtube.com/watch?v=C6gYqSHLRw4")
    ,("51-東森新聞台", "https://www.youtube.com/watch?v=V1p33hqPrUk")
    ,("52-中天新聞台", "https://www.youtube.com/watch?v=oIgbl7t0S_w")
    ,("53-民視新聞台", "https://www.youtube.com/watch?v=ylYJSBUgaMA")
    ,("54-三立新聞台", "https://www.youtube.com/watch?v=oZdzzvxTfUY")
    ,("55-TVBS NEWS 24hr", "https://www.youtube.com/watch?v=m_dhMSvUCIc")
    ,("57-東森財經新聞", "https://www.youtube.com/watch?v=WHEPzbFA3hw")
    ,("154-中視新聞台", "https://www.youtube.com/watch?v=TCnaIE_SAtM")
    ,("155-台視新聞-HD", "https://www.youtube.com/watch?v=xL0ch83RAK8")

    ,("寰宇新聞台 24小時", "https://www.youtube.com/watch?v=6IquAgfvYmc")
    ,("寰宇新聞 台灣台", "https://www.youtube.com/watch?v=w87VGpgd90U")
    ,("台灣地震監視", "https://www.youtube.com/watch?v=Owke6Quk7T0")

    ,("華視新聞直播 CH52", "https://www.youtube.com/watch?v=wM0g8EoUZ_E")
    ,("公視新聞 PTS News", "https://www.youtube.com/watch?v=quwqlazU-c8")
    ,("公視台語台", "https://www.youtube.com/watch?v=6KlRR_DGhmI")
    ,("新唐人LIVE", "https://www.youtube.com/watch?v=WIhgU_mc05A")

    #Japan
    ,("JapaNews24", "https://www.youtube.com/watch?v=coYw-eVU0Ks")

    #korea
    ,("KBS World TV", "https://www.youtube.com/watch?v=OxQQsIvJTTU")
    ,("YTN", "https://www.youtube.com/watch?v=FJfwehhzIhw")

    #American
    ,("CNN News18 ", "https://www.youtube.com/watch?v=rfDx1HMvXbQ")
    
    ,("NBC News", "https://www.youtube.com/watch?v=yZJz31TwTTg")
    ,("NBC2 live", "https://www.youtube.com/watch?v=01tsVNieY8E")
    ,("Bloomberg Business News Live", "https://www.youtube.com/watch?v=iyOq8DhaMYw")
    ,("Live Business, Finance & Investment News from Bloomberg", "https://www.youtube.com/watch?v=f39oHo6vFLg")
    ,("USA TODAY 24/7 Live Stream", "https://www.youtube.com/watch?v=vZYMwAm8sso")
    ,("Bloomberg Originals Live News", "https://www.youtube.com/watch?v=DxmDPrfinXY")
    ,("FOX Weather Live Stream", "https://www.youtube.com/watch?v=wt6SIE7BXS8")
    ,("FOX 24/7 LIVE STREAM", "https://www.youtube.com/watch?v=YDfiTGGPYCk")

    #Australia
    ,("ABC News Australia live", "https://www.youtube.com/watch?v=vOTiJkg1voo")
    ,("ABC13 Houston", "https://www.youtube.com/watch?v=6EdywNFYhu8")

    #UK
    ,("Sky News", "https://www.youtube.com/watch?v=oJUvTVdTMyY")

    #Singapore
    ,("CNA Breaking news", "https://www.youtube.com/watch?v=XWq5kBlakcQ")
    ,("CNA Insider LIVE", "https://www.youtube.com/watch?v=fSUMKrxPEd8")

    #Euronews
    ,("Euronews English Live", "https://www.youtube.com/watch?v=pykpO5kQJ98")
    ,("FRANCE 24 English ", "https://www.youtube.com/watch?v=Ap-UM1O9RBU")

    #German 
    ,("DW News(德國之聲)", "https://www.youtube.com/watch?v=tZT2MCYu6Zw")

    #Turkey
    ,("TRT World", "https://www.youtube.com/watch?v=66LVIaUxaFk")

    #Russian
    ,("RT News", "https://www.youtube.com/watch?v=NvCSr7qzAAM")
    
    #India
    ,("India Today", "https://www.youtube.com/watch?v=8UJMH_VIRhU")
    ,("WION LIVE News(世界一體)", "https://www.youtube.com/watch?v=gadjsB5BkK4")

    #middle-asian
    #Israel
    ,("Israel News LIVE -- from CNN News18 ", "https://www.youtube.com/watch?v=dMEZf8Pmz-0")

    ,("Al Jazeera English(半島電視台)", "https://www.youtube.com/watch?v=gCNeDWCI0vo")

    # 聯合國
    ,("United Nations - LIVE", "https://www.youtube.com/watch?v=wfAa1GiNdgM")


]

def get_html_data(url):
    urlU = UrlUtility()
    htmldata = urlU.get_url_data(url)
    return htmldata

def gen_m3u8():
    
    reu = ReUtility()
    threads = []
    resList = []
    for urlObj in urlList:
        t = MyThread(get_html_data, args = (urlObj[1], ) )
        t.start()
        threads.append((urlObj[0], t))

    for item in threads:
        name = item[0]
        t = item[1]
        t.join()
        htmldata = t.get_result()
        res = reu.get_between_string(htmldata, "m3u8", "http", "m3u8")
        res = res.replace('\/', '/')
        resList.append((name, res))

    m3u8U = M3u8()
    m3u8 = m3u8U.get_m3u8_head_string()
    for obj in resList:
        m3u8 += m3u8U.get_m3u8_item_string(obj[0], obj[1])

    print(m3u8)
    return m3u8

aaa = gen_m3u8()
print(aaa)
