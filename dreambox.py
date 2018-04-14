import requests

## openwebif 
ip = "192.168.1.2"
port = "80"
url = "http://"+ip+":"+port

#u = "2"
#pw = "1234567"
#url = "http://"+u+":"+pw+"@"+ip+":"+port

## Remote Controll Commands
rc = url+"/web/remotecontrol?command="

## Zap to ServiceRef
zap = url+"/web/zap?sRef="

b = {"ard": zap+"1:0:19:283D:3FB:1:C00000:0:0:0:",
    "zdf": zap+"1:0:19:2B66:3F3:1:C00000:0:0:0:",
    "wdr": zap+"1:0:19:6F83:457:1:C00000:0:0:0::WDR HD",
    "rtl": zap+"1:0:19:EF10:421:1:C00000:0:0:0:",
    "sat1": zap+"1:0:19:EF74:3F9:1:C00000:0:0:0:",
    "rtl2": zap+"1:0:19:EF15:421:1:C00000:0:0:0:",
    "pro7": zap+"1:0:19:EF75:3F9:1:C00000:0:0:0:",
    "vox": zap+"1:0:19:EF11:421:1:C00000:0:0:0:",
    "kabel1": zap+"1:0:19:EF76:3F9:1:C00000:0:0:0:",
    "superrtl": zap+"1:0:19:2E9B:411:1:C00000:0:0:0:",
    "sixx": zap+"1:0:19:EF77:3F9:1:C00000:0:0:0:",
    "rtlplus": zap+"1:0:1:2F30:441:1:C00000:0:0:0:",
    "pro7maxx": zap+"1:0:19:EF78:3F9:1:C00000:0:0:0::Pro7 MAXX HD",
    "rtlnitro": zap+"1:0:19:2EAF:411:1:C00000:0:0:0:",
    "viva": zap+"1:0:1:7004:436:1:C00000:0:0:0::Comedy Central VIVA",
    "comedycentral": zap+"1:0:1:7004:436:1:C00000:0:0:0::Comedy Central VIVA",
    "tlc": zap+"1:0:19:2774:409:1:C00000:0:0:0:",
    "insighttv": zap+"1:0:19:1392:3EA:1:C00000:0:0:0:",
    "passion": zap+"1:0:16:1D:4:85:C00000:0:0:0:",
    "sat1gold": zap+"1:0:19:30D4:413:1:C00000:0:0:0:",
    "sat1emo": zap+"1:0:16:14C1:407:1:C00000:0:0:0:",
    "toggoplus": zap+"1:0:1:2EFE:441:1:C00000:0:0:0:",
    "nickaustria": zap+"1:0:1:3D:7:85:C00000:0:0:0:",
    "nick": zap+"1:0:19:5273:41D:1:C00000:0:0:0:",
    "kika": zap+"1:0:19:2B98:3F2:1:C00000:0:0:0:",
    "disneychannel": zap+"1:0:19:157C:41F:1:C00000:0:0:0:",
    "kabeleinsdoku": zap+"1:0:1:4465:453:1:C00000:0:0:0:",
    "dmax": zap+"1:0:19:151A:455:1:C00000:0:0:0:",
    "n24": zap+"1:0:19:5274:41D:1:C00000:0:0:0:",
    "ntv": zap+"1:0:19:EF14:421:1:C00000:0:0:0:",
    "n24doku": zap+"1:0:1:30:5:85:C00000:0:0:0:",
    "phoenix": zap+"1:0:19:285B:401:1:C00000:0:0:0:",
    "sport1": zap+"1:0:19:1581:41F:1:C00000:0:0:0:",
    "sport1+": zap+"1:0:19:7A:B:85:C00000:0:0:0:",
    "eurosport": zap+"1:0:19:30D6:413:1:C00000:0:0:0:",
    "eurosport2": zap+"1:0:19:6D:9:85:C00000:0:0:0:",
    "eurosport2x": zap+"1:0:19:30D7:413:1:C00000:0:0:0:",
    "motorvision": zap+"1:0:16:A8:E:85:C00000:0:0:0:",
    "anixe": zap+"1:0:19:526C:41D:1:C00000:0:0:0:",
    "rtlcrime": zap+"1:0:19:8C:9:85:C00000:0:0:0:",
    "axn": zap+"1:0:16:101D:451:35:C00000:0:0:0::AXN",
    "13street": zap+"1:0:19:7F:D:85:C00000:0:0:0:",
    "fox": zap+"1:0:19:7C:A:85:C00000:0:0:0:",
    "syfy": zap+"1:0:19:7E:C:85:C00000:0:0:0:",
    "tnts": zap+"1:0:19:7B:B:85:C00000:0:0:0:",
    "tntc": zap+"1:0:19:88:E:85:C00000:0:0:0::TNT Comedy HD",
    "universal": zap+"1:0:19:65:E:85:C00000:0:0:0:",
    "skyatlantic": zap+"1:0:19:6E:D:85:C00000:0:0:0:",
    "discovery": zap+"1:0:19:82:6:85:C00000:0:0:0:",
    "natgeo": zap+"1:0:19:70:D:85:C00000:0:0:0:",
    "natgetowild": zap+"1:0:19:76:6:85:C00000:0:0:0:",
    "history": zap+"1:0:19:71:B:85:C00000:0:0:0:",
    "spiegelgeschichte": zap+"1:0:19:89:A:85:C00000:0:0:0:",
    "a&e": zap+"1:0:16:192:E:85:C00000:0:0:0:",
    "planet": zap+"1:0:16:1013:451:35:C00000:0:0:0:",
    "entertainment": zap+"1:0:19:80:E:85:C00000:0:0:0:",
    "weltderwunder": zap+"1:0:1:332F:45B:1:C00000:0:0:0:",
    "servustv": zap+"1:0:19:1331:3EF:1:C00000:0:0:0:",
    "servustvat": zap+"1:0:19:1332:3EF:1:C00000:0:0:0:",
    "skyarts": zap+"1:0:19:91:9:85:C00000:0:0:0:",
    "skyaction": zap+"1:0:19:74:B:85:C00000:0:0:0:",
    "skycinema": zap+"1:0:19:83:6:85:C00000:0:0:0:",
    "skycinema1": zap+"1:0:19:86:8:85:C00000:0:0:0:",
    "skycinema24": zap+"1:0:19:87:8:85:C00000:0:0:0:",
    "skyhits": zap+"1:0:19:6B:C:85:C00000:0:0:0:",
    "skyfamily": zap+"1:0:19:8B:8:85:C00000:0:0:0:",
    "skycomedy": zap+"1:0:16:8:3:85:C00000:0:0:0:",
    "skyemotions": zap+"1:0:16:14:4:85:C00000:0:0:0:",
    "skynostalgie": zap+"1:0:16:204:4:85:C00000:0:0:0:",
    "disneycinemagic": zap+"1:0:19:6F:D:85:C00000:0:0:0:",
    "skykrimi": zap+"1:0:16:17:4:85:C00000:0:0:0:",
    "tntf": zap+"1:0:16:195:6:85:C00000:0:0:0::TNT Film",
    "kabeleinsclassic": zap+"1:0:16:14C2:407:1:C00000:0:0:0:",
    "kinowelt": zap+"1:0:16:196:4:85:C00000:0:0:0:",
    "heimatkanal": zap+"1:0:16:16:2:85:C00000:0:0:0:",
    "junior": zap+"1:0:16:13:3:85:C00000:0:0:0:",
    "cartoonnetwork": zap+"1:0:16:194:E:85:C00000:0:0:0:",
    "disneyxd": zap+"1:0:16:1C:3:85:C00000:0:0:0:",
    "disneyjunior": zap+"1:0:19:8A:8:85:C00000:0:0:0:",
    "boomerang": zap+"1:0:16:193:E:85:C00000:0:0:0:",
    "skysportnews": zap+"1:0:19:6C:C:85:C00000:0:0:0:",
    "skysport1": zap+"1:0:19:81:6:85:C00000:0:0:0:",
    "skysport2": zap+"1:0:19:72:D:85:C00000:0:0:0:",
    "skysport3": zap+"1:0:19:10C:6:85:C00000:0:0:0:",
    "skysport4": zap+"1:0:19:116:D:85:C00000:0:0:0:",
    "skysport5": zap+"1:0:19:120:C:85:C00000:0:0:0:",
    "skysport6": zap+"1:0:19:12A:B:85:C00000:0:0:0:",
    "skysport7": zap+"1:0:19:134:8:85:C00000:0:0:0:",
    "skysport8": zap+"1:0:19:13E:9:85:C00000:0:0:0:",
    "skysport9": zap+"1:0:19:148:10:85:C00000:0:0:0:",
    "skybundesliga1": zap+"1:0:19:69:C:85:C00000:0:0:0:",
    "skybundesliga2": zap+"1:0:19:10B:6:85:C00000:0:0:0:",
    "skybundesliga3": zap+"1:0:19:115:D:85:C00000:0:0:0:",
    "skybundesliga4": zap+"1:0:19:11F:C:85:C00000:0:0:0:",
    "skybundesliga5": zap+"1:0:19:129:B:85:C00000:0:0:0:",
    "skybundesliga6": zap+"1:0:19:133:8:85:C00000:0:0:0:",
    "skybundesliga7": zap+"1:0:19:13D:9:85:C00000:0:0:0:",
    "skybundesliga8": zap+"1:0:19:147:10:85:C00000:0:0:0:",
    "skybundesliga9": zap+"1:0:19:151:A:85:C00000:0:0:0:",
    "skybundesliga10": zap+"1:0:19:151:A:85:C00000:0:0:0:",
    "deluxemusic": zap+"1:0:19:2777:409:1:C00000:0:0:0:",
    "mtv": zap+"1:0:19:2777:409:1:C00000:0:0:0:",
    "mtvhits": zap+"1:0:1:6FEE:42A:1:C00000:0:0:0:",
    "mtvdance": zap+"1:0:1:6FEF:42A:1:C00000:0:0:0:",
    "mtvmusic24": zap+"1:0:1:6FFF:436:1:C00000:0:0:0:",
    "mtvrocks": zap+"1:0:1:6FF3:42A:1:C00000:0:0:0:",
    "vh1": zap+"1:0:1:6FF0:42A:1:C00000:0:0:0:",
    "vh1classic": zap+"1:0:1:6FF1:42A:1:C00000:0:0:0:",
    "jukebox": zap+"1:0:16:191:9:85:C00000:0:0:0:",
    "gotv": zap+"1:0:16:3404:3ED:1:C00000:0:0:0:",
    "zeeone": zap+"1:0:19:2775:409:1:C00000:0:0:0:",
    "arte": zap+"1:0:19:283E:3FB:1:C00000:0:0:0:",
    "ardalpha": zap+"1:0:1:6F47:445:1:C00000:0:0:0:",
    "one": zap+"1:0:19:2888:40F:1:C00000:0:0:0:",
    "tagesschau24": zap+"1:0:19:2887:40F:1:C00000:0:0:0:",
    "zdfinfo": zap+"1:0:19:2BA2:3F2:1:C00000:0:0:0:",
    "zdfneo": zap+"1:0:19:2B7A:3F3:1:C00000:0:0:0:",
    "3sat": zap+"1:0:19:2B8E:3F2:1:C00000:0:0:0:",
    "ndr": zap+"1:0:19:2857:401:1:C00000:0:0:0:",
    "rbb": zap+"1:0:19:286F:425:1:C00000:0:0:0:",
    "hr": zap+"1:0:19:2873:425:1:C00000:0:0:0:",
    "swr": zap+"1:0:19:283F:3FB:1:C00000:0:0:0:",
    "mdr": zap+"1:0:19:2870:425:1:C00000:0:0:0:",
    "br": zap+"1:0:19:2855:401:1:C00000:0:0:0:",
    "orf1": zap+"1:0:19:132F:3EF:1:C00000:0:0:0:",
    "orf2": zap+"1:0:19:1330:3EF:1:C00000:0:0:0:",
    "orf3": zap+"1:0:1:332D:45B:1:C00000:0:0:0:",
    "atv": zap+"1:0:19:33AC:3EB:1:C00000:0:0:0:",
    "atv2": zap+"1:0:1:33A7:3EB:1:C00000:0:0:0:",
    "puls4": zap+"1:0:1:4E27:43A:1:C00000:0:0:0:",
    "orfsport": zap+"1:0:19:33FD:3ED:1:C00000:0:0:0:",
    "skysportautria": zap+"1:0:19:8F:9:85:C00000:0:0:0:",
    "sportdigital": zap+"1:0:19:1018:451:35:C00000:0:0:0:",
    "brazzerstv": zap+"1:0:16:1009:451:35:C00000:0:0:0:",
    "hustlertv": zap+"1:0:16:100B:451:35:C00000:0:0:0:",
    "vividtv": zap+"1:0:16:FE0:451:35:C00000:0:0:0:",
    "standby": rc+"116",
    "volup": rc+"115",
    "voldown": rc+"114",
    "mute": rc+"113",
    "chanup": rc+"106",
    "chandown": rc+"105",
    "up": rc+"103",
    "down": rc+"108",
    "left": rc+"105",
    "right": rc+"106",
    "ok": rc+"352",
    "info": rc+"358",
    "epg": rc+"365",
    "back": rc+"174",
    "red": rc+"398",
    "green": rc+"399",
    "yellow": rc+"400",
    "blue": rc+"401",
    "help": rc+"138",
    "text": rc+"388",
    "radio": rc+"385",
    "tv": rc+"377",
    "video": rc+"393",
    "audio": rc+"392",
    "menu": rc+"139",
    "play": rc+"164",
    "timeshift": rc+"164",
    "record": rc+"167"}

while True:
    
    to_print = raw_input("Channel? ")
    
    for v in b:
        if v == to_print:
            requests.post( b[v])
        
