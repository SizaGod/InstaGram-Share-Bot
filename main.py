import os
try:
    import aiohttp
    import asyncio
    import uuid
    import json
    import sys
    import requests
    import uuid
    import time 
    import random
    from base64 import b64encode
    from hashlib import md5
    import time
    import secrets
except:
  os.system("pip install aiohttp uuid requests")

import os
import aiohttp
import asyncio
import uuid
import json
import sys
import requests
import uuid
import time 
import random
from base64 import b64encode
import uuid
from hashlib import md5
import time
import secrets


user=input("ENTER YOUR USERNAME Or EMAIL Or PHONE : ")
psw=input("ENTET YOUR PASSWORD : ")

data = {
'username': user,
'password': psw,
'device_id': f"android-{secrets.token_hex(8)}",
'_csrftoken' : md5(str(time.time()).encode()).hexdigest(),
'phone_id': str(uuid.uuid4()),
'guid': str(uuid.uuid4()),

        }
Siza = requests.post('https://b.i.instagram.com/api/v1/accounts/login/', headers = {
'User-Agent': "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
"Content-Type": "application/x-www-form-urlencoded",
"X-CSRFToken": str(secrets.token_hex(8)),
        }, data=data)
        
        
if "logged_in_user" in Siza.text:
    print("Login Successfully")
    ses = Siza.cookies["sessionid"]
    id = Siza.cookies["ds_user_id"]
else:
    print("BAD LOGIN TRY ANOTHER ACCOUNT ..!")
    exit(0)
    
    
link = input ("ENTER The Reel Instagram (Video) Link : ")
code = link.split("/reel/")[1].split("/")[0]
zzz = int(input("ENTER THE Time Sleep (1, 20): "))


Greenlight = {
    'A': '0',
    'B': '1',
    'C': '2',
    'D': '3',
    'E': '4',
    'F': '5',
    'G': '6',
    'H': '7',
    'I': '8',
    'J': '9',
    'K': 'a',
    'L': 'b',
    'M': 'c',
    'N': 'd',
    'O': 'e',
    'P': 'f',
    'Q': 'g',
    'R': 'h',
    'S': 'i',
    'T': 'j',
    'U': 'k',
    'V': 'l',
    'W': 'm',
    'X': 'n',
    'Y': 'o',
    'Z': 'p',
    'a': 'q',
    'b': 'r',
    'c': 's',
    'd': 't',
    'e': 'u',
    'f': 'v',
    'g': 'w',
    'h': 'x',
    'i': 'y',
    'j': 'z',
    'k': 'A',
    'l': 'B',
    'm': 'C',
    'n': 'D',
    'o': 'E',
    'p': 'F',
    'q': 'G',
    'r': 'H',
    's': 'I',
    't': 'J',
    'u': 'K',
    'v': 'L',
    'w': 'M',
    'x': 'N',
    'y': 'O',
    'z': 'P',
    '0': 'Q',
    '1': 'R',
    '2': 'S',
    '3': 'T',
    '4': 'U',
    '5': 'V',
    '6': 'W',
    '7': 'X',
    '8': 'Y',
    '9': 'Z',
    '-': '$',
    '_': '_'
}

def MyMedia(code):
    kk = ""
    for letter in code:
        kk += Greenlight[letter]
  
    Qat = list(Greenlight.values())
    number = 0
    for char in kk:
        number = number * 64 + Qat.index(char)

    return number
  
media_id = MyMedia(code)
print(media_id)



token = b64encode(f'{{"ds_user_id":"{id}","sessionid":"{ses}"}}'.encode('utf-8'))
headers = {
    'User-Agent': "Instagram 351.0.0.41.106 Android (30/11; 440dpi; 1080x2220; Xiaomi/Redmi; Redmi Note 8 Pro; begonia; mt6785; ar_EG; 647663441)",
    'x-bloks-version-id': "145bdb95c874a8d81dfe9d44aeff8286378f930f5898c808f8d2f0bb1d931181",
    'accept-language': "ar-EG, en-US",
    'authorization': f"Bearer IGT:2:{token.decode('utf-8')}",
}

async def explore(session, vidID):
    while True:
        try:
            params = {
                'exposed_to_experiment': "true",
                'inventory_source': "media_or_ad",
                'share_to_app': "copy_link",
                'm_t': "2",
                'm_ix': "0",
                'qe_universe_name': "ig_external_sharing_v2",
                'is_threads': "false",
                'containermodule': "direct_reshare_sheet"
            }

            async with session.get(f"https://i.instagram.com/api/v1/media/{vidID}/permalink/", params=params, headers=headers) as response:
                print(await response.text())
                await asyncio.sleep(zzz)
        except Exception as e:
            print(f"Error in Explore: {e}")
            await asyncio.sleep(zzz)

async def SizaGod(session):
    try:
        params = {
            'clips_media_id': media_id
        }

        async with session.get("https://i.instagram.com/api/v1/clips/item/", params=params, headers=headers) as response:
            data = await response.json()
            vidID = data.get('media', {}).get("id")
            if vidID:
                await explore(session, vidID)
            else:
                print("Try Again Letter")
    except Exception as e:
        print(f"Error: {e}")

async def seen(session):
    try:
        url = "https://i.instagram.com/api/v1/clips/write_seen_state/"
        payload = f"signed_body=SIGNATURE.%7B%22impressions%22%3A%22%5B%5C%22{media_id}%5C%22%5D%22%2C%22_uid%22%3A%22{id}%22%2C%22_uuid%22%3A%22{str(uuid.uuid4())}%22%2C%22blend_impressions%22%3A%22%5B%5D%22%7D"
        
        async with session.post(url, data=payload, headers=headers) as response:
            data = await response.json()
            if data["status"] == "ok":
                await SizaGod(session)
            else:
                print("Try Again Letter")
    except Exception as e:
        print(f"Error in Seen: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        await seen(session)


if __name__ == "__main__":
    asyncio.run(main())

