import requests

## openwebif 
ip = "192.168.1.2"
p = "80"

#l = "2"
#p = "1234567"
#u = "http://"+l+":"+pw+"@"+ip+":"+p

u = "http://"+ip+":"+port
r = u+"/web/remotecontrol?command="
z = u+"/web/zap?sRef="

b = {"ard": z+"1:0:19:283D:3FB:1:C00000:0:0:0:",
    "zdf": z+"1:0:19:2B66:3F3:1:C00000:0:0:0:",
    "wdr": z+"1:0:19:6F83:457:1:C00000:0:0:0::WDR HD",
    "rtl": z+"1:0:19:EF10:421:1:C00000:0:0:0:",
    "sat1": z+"1:0:19:EF74:3F9:1:C00000:0:0:0:",
    "rtl2": z+"1:0:19:EF15:421:1:C00000:0:0:0:",
    "pro7": z+"1:0:19:EF75:3F9:1:C00000:0:0:0:",
    "vox": z+"1:0:19:EF11:421:1:C00000:0:0:0:",
    "kabel1": z+"1:0:19:EF76:3F9:1:C00000:0:0:0:",
    "superrtl": z+"1:0:19:2E9B:411:1:C00000:0:0:0:",
    "sixx": z+"1:0:19:EF77:3F9:1:C00000:0:0:0:",
    "rtlplus": z+"1:0:1:2F30:441:1:C00000:0:0:0:",
    "pro7maxx": z+"1:0:19:EF78:3F9:1:C00000:0:0:0::Pro7 MAXX HD",
    "rtlnitro": z+"1:0:19:2EAF:411:1:C00000:0:0:0:",
    "viva": z+"1:0:1:7004:436:1:C00000:0:0:0::Comedy Central VIVA",
    "comedycentral": z+"1:0:1:7004:436:1:C00000:0:0:0::Comedy Central VIVA",
    "tlc": z+"1:0:19:2774:409:1:C00000:0:0:0:",
    "insighttv": z+"1:0:19:1392:3EA:1:C00000:0:0:0:",
    "passion": z+"1:0:16:1D:4:85:C00000:0:0:0:",
    "sat1gold": z+"1:0:19:30D4:413:1:C00000:0:0:0:",
    "sat1emo": z+"1:0:16:14C1:407:1:C00000:0:0:0:",
    "toggoplus": z+"1:0:1:2EFE:441:1:C00000:0:0:0:",
    "nickaustria": z+"1:0:1:3D:7:85:C00000:0:0:0:",
    "nick": z+"1:0:19:5273:41D:1:C00000:0:0:0:",
    "kika": z+"1:0:19:2B98:3F2:1:C00000:0:0:0:",
    "disneychannel": z+"1:0:19:157C:41F:1:C00000:0:0:0:",
    "kabeleinsdoku": z+"1:0:1:4465:453:1:C00000:0:0:0:",
    "dmax": z+"1:0:19:151A:455:1:C00000:0:0:0:",
    "n24": z+"1:0:19:5274:41D:1:C00000:0:0:0:",
    "ntv": z+"1:0:19:EF14:421:1:C00000:0:0:0:",
    "n24doku": z+"1:0:1:30:5:85:C00000:0:0:0:",
    "phoenix": z+"1:0:19:285B:401:1:C00000:0:0:0:",
    "sport1": z+"1:0:19:1581:41F:1:C00000:0:0:0:",
    "sport1+": z+"1:0:19:7A:B:85:C00000:0:0:0:",
    "eurosport": z+"1:0:19:30D6:413:1:C00000:0:0:0:",
    "eurosport2": z+"1:0:19:6D:9:85:C00000:0:0:0:",
    "eurosport2x": z+"1:0:19:30D7:413:1:C00000:0:0:0:",
    "motorvision": z+"1:0:16:A8:E:85:C00000:0:0:0:",
    "anixe": z+"1:0:19:526C:41D:1:C00000:0:0:0:",
    "rtlcrime": z+"1:0:19:8C:9:85:C00000:0:0:0:",
    "axn": z+"1:0:16:101D:451:35:C00000:0:0:0::AXN",
    "13street": z+"1:0:19:7F:D:85:C00000:0:0:0:",
    "fox": z+"1:0:19:7C:A:85:C00000:0:0:0:",
    "syfy": z+"1:0:19:7E:C:85:C00000:0:0:0:",
    "tnts": z+"1:0:19:7B:B:85:C00000:0:0:0:",
    "tntc": z+"1:0:19:88:E:85:C00000:0:0:0::TNT Comedy HD",
    "universal": z+"1:0:19:65:E:85:C00000:0:0:0:",
    "skyatlantic": z+"1:0:19:6E:D:85:C00000:0:0:0:",
    "discovery": z+"1:0:19:82:6:85:C00000:0:0:0:",
    "natgeo": z+"1:0:19:70:D:85:C00000:0:0:0:",
    "natgetowild": z+"1:0:19:76:6:85:C00000:0:0:0:",
    "history": z+"1:0:19:71:B:85:C00000:0:0:0:",
    "spiegelgeschichte": z+"1:0:19:89:A:85:C00000:0:0:0:",
    "a&e": z+"1:0:16:192:E:85:C00000:0:0:0:",
    "planet": z+"1:0:16:1013:451:35:C00000:0:0:0:",
    "entertainment": z+"1:0:19:80:E:85:C00000:0:0:0:",
    "weltderwunder": z+"1:0:1:332F:45B:1:C00000:0:0:0:",
    "servustv": z+"1:0:19:1331:3EF:1:C00000:0:0:0:",
    "servustvat": z+"1:0:19:1332:3EF:1:C00000:0:0:0:",
    "skyarts": z+"1:0:19:91:9:85:C00000:0:0:0:",
    "skyaction": z+"1:0:19:74:B:85:C00000:0:0:0:",
    "skycinema": z+"1:0:19:83:6:85:C00000:0:0:0:",
    "skycinema1": z+"1:0:19:86:8:85:C00000:0:0:0:",
    "skycinema24": z+"1:0:19:87:8:85:C00000:0:0:0:",
    "skyhits": z+"1:0:19:6B:C:85:C00000:0:0:0:",
    "skyfamily": z+"1:0:19:8B:8:85:C00000:0:0:0:",
    "skycomedy": z+"1:0:16:8:3:85:C00000:0:0:0:",
    "skyemotions": z+"1:0:16:14:4:85:C00000:0:0:0:",
    "skynostalgie": z+"1:0:16:204:4:85:C00000:0:0:0:",
    "disneycinemagic": z+"1:0:19:6F:D:85:C00000:0:0:0:",
    "skykrimi": z+"1:0:16:17:4:85:C00000:0:0:0:",
    "tntf": z+"1:0:16:195:6:85:C00000:0:0:0::TNT Film",
    "kabeleinsclassic": z+"1:0:16:14C2:407:1:C00000:0:0:0:",
    "kinowelt": z+"1:0:16:196:4:85:C00000:0:0:0:",
    "heimatkanal": z+"1:0:16:16:2:85:C00000:0:0:0:",
    "junior": z+"1:0:16:13:3:85:C00000:0:0:0:",
    "cartoonnetwork": z+"1:0:16:194:E:85:C00000:0:0:0:",
    "disneyxd": z+"1:0:16:1C:3:85:C00000:0:0:0:",
    "disneyjunior": z+"1:0:19:8A:8:85:C00000:0:0:0:",
    "boomerang": z+"1:0:16:193:E:85:C00000:0:0:0:",
    "skysportnews": z+"1:0:19:6C:C:85:C00000:0:0:0:",
    "skysport1": z+"1:0:19:81:6:85:C00000:0:0:0:",
    "skysport2": z+"1:0:19:72:D:85:C00000:0:0:0:",
    "skysport3": z+"1:0:19:10C:6:85:C00000:0:0:0:",
    "skysport4": z+"1:0:19:116:D:85:C00000:0:0:0:",
    "skysport5": z+"1:0:19:120:C:85:C00000:0:0:0:",
    "skysport6": z+"1:0:19:12A:B:85:C00000:0:0:0:",
    "skysport7": z+"1:0:19:134:8:85:C00000:0:0:0:",
    "skysport8": z+"1:0:19:13E:9:85:C00000:0:0:0:",
    "skysport9": z+"1:0:19:148:10:85:C00000:0:0:0:",
    "bl1": z+"1:0:19:69:C:85:C00000:0:0:0:",
    "bl2": z+"1:0:19:10B:6:85:C00000:0:0:0:",
    "bl3": z+"1:0:19:115:D:85:C00000:0:0:0:",
    "bl4": z+"1:0:19:11F:C:85:C00000:0:0:0:",
    "bl5": z+"1:0:19:129:B:85:C00000:0:0:0:",
    "bl6": z+"1:0:19:133:8:85:C00000:0:0:0:",
    "bl7": z+"1:0:19:13D:9:85:C00000:0:0:0:",
    "bl8": z+"1:0:19:147:10:85:C00000:0:0:0:",
    "bl9": z+"1:0:19:151:A:85:C00000:0:0:0:",
    "bl10": z+"1:0:19:151:A:85:C00000:0:0:0:",
    "deluxemusic": z+"1:0:19:2777:409:1:C00000:0:0:0:",
    "mtv": z+"1:0:19:2777:409:1:C00000:0:0:0:",
    "mtvhits": z+"1:0:1:6FEE:42A:1:C00000:0:0:0:",
    "mtvdance": z+"1:0:1:6FEF:42A:1:C00000:0:0:0:",
    "mtvmusic24": z+"1:0:1:6FFF:436:1:C00000:0:0:0:",
    "mtvrocks": z+"1:0:1:6FF3:42A:1:C00000:0:0:0:",
    "vh1": z+"1:0:1:6FF0:42A:1:C00000:0:0:0:",
    "vh1classic": z+"1:0:1:6FF1:42A:1:C00000:0:0:0:",
    "jukebox": z+"1:0:16:191:9:85:C00000:0:0:0:",
    "gotv": z+"1:0:16:3404:3ED:1:C00000:0:0:0:",
    "zeeone": z+"1:0:19:2775:409:1:C00000:0:0:0:",
    "arte": z+"1:0:19:283E:3FB:1:C00000:0:0:0:",
    "ardalpha": z+"1:0:1:6F47:445:1:C00000:0:0:0:",
    "one": z+"1:0:19:2888:40F:1:C00000:0:0:0:",
    "tagesschau24": z+"1:0:19:2887:40F:1:C00000:0:0:0:",
    "zdfinfo": z+"1:0:19:2BA2:3F2:1:C00000:0:0:0:",
    "zdfneo": z+"1:0:19:2B7A:3F3:1:C00000:0:0:0:",
    "3sat": z+"1:0:19:2B8E:3F2:1:C00000:0:0:0:",
    "ndr": z+"1:0:19:2857:401:1:C00000:0:0:0:",
    "rbb": z+"1:0:19:286F:425:1:C00000:0:0:0:",
    "hr": z+"1:0:19:2873:425:1:C00000:0:0:0:",
    "swr": z+"1:0:19:283F:3FB:1:C00000:0:0:0:",
    "mdr": z+"1:0:19:2870:425:1:C00000:0:0:0:",
    "br": z+"1:0:19:2855:401:1:C00000:0:0:0:",
    "orf1": z+"1:0:19:132F:3EF:1:C00000:0:0:0:",
    "orf2": z+"1:0:19:1330:3EF:1:C00000:0:0:0:",
    "orf3": z+"1:0:1:332D:45B:1:C00000:0:0:0:",
    "atv": z+"1:0:19:33AC:3EB:1:C00000:0:0:0:",
    "atv2": z+"1:0:1:33A7:3EB:1:C00000:0:0:0:",
    "puls4": z+"1:0:1:4E27:43A:1:C00000:0:0:0:",
    "orfsport": z+"1:0:19:33FD:3ED:1:C00000:0:0:0:",
    "skysportautria": z+"1:0:19:8F:9:85:C00000:0:0:0:",
    "sportdigital": z+"1:0:19:1018:451:35:C00000:0:0:0:",
    "brazzerstv": z+"1:0:16:1009:451:35:C00000:0:0:0:",
    "hustlertv": z+"1:0:16:100B:451:35:C00000:0:0:0:",
    "vividtv": z+"1:0:16:FE0:451:35:C00000:0:0:0:",
    "standby": r+"116",
    "volup": r+"115",
    "voldown": r+"114",
    "mute": r+"113",
    "chanup": r+"106",
    "chandown": r+"105",
    "up": r+"103",
    "down": r+"108",
    "left": r+"105",
    "right": r+"106",
    "ok": r+"352",
    "info": r+"358",
    "epg": r+"365",
    "back": r+"174",
    "red": r+"398",
    "green": r+"399",
    "yellow": r+"400",
    "blue": r+"401",
    "help": r+"138",
    "text": r+"388",
    "radio": r+"385",
    "tv": r+"377",
    "video": r+"393",
    "audio": r+"392",
    "menu": r+"139",
    "play": r+"164",
    "timeshift": r+"164",
    "record": r+"167"}

while True:
    
    to_print = raw_input("Channel? ")
    
    for v in b:
        if v == to_print:
            requests.post( b[v])
        
