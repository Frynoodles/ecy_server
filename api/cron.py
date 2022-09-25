import json

import requests
import os

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Cookie':
        'buvid3=3CB14678-25EC-40D6-7EF7-873DF92DBD4B15817infoc; b_nut=100; i-wanna-go-back=-1; b_ut=7; _uuid=36594562-10BB9-2ACA-F4910-93EC66CACF10374799infoc; buvid_fp=194f17396eafdd8931ec4a30a3380308; buvid4=E1F61BD2-E082-1EE9-8B9C-74A0F3B161E278386-022092422-BErYQwk6jq3TkhXM80TpAA%3D%3D; innersign=0; b_lsid=81C98316_1837332BF98; CURRENT_FNVAL=16; sid=fh7wtqmm'
}


def update_bilibili_info():
    # 更新数据
    info_data: dict = get_bili_user_info('29325500')
    if info_data == {}:
        pass
    else:
        data: dict = info_data['data']
        mid = data['mid']
        name = data['name']
        face = data['face']
        sign = data['sign']
        top_photo = data['top_photo']
        if os.path.exists(f'../resource/{face.split("/")[-1]}'):
            pass
        else:
            with open(f'../resource/{face.split("/")[-1]}', 'wb') as f:
                f.write(requests.get(face, headers=HEADERS).content)
        if os.path.exists(f'../resource/{top_photo.split("/")[-1]}'):
            pass
        else:
            with open(f'../resource/{top_photo.split("/")[-1]}', 'wb') as f:
                f.write(requests.get(top_photo, headers=HEADERS).content)
        with open('../resource/info.json', 'w', encoding='utf-8') as f:
            data: str = json.dumps(
                {'mid': mid, 'name': name, 'face': face.split('/')[-1], 'sign': sign,
                 'top_photo': top_photo.split('/')[-1]})
            f.write(data)


def get_bili_user_info(mid: str) -> dict:
    # 由mid获取用户数据
    URL = f"https://api.bilibili.com/x/space/acc/info?mid={mid}&token=&platform=web&jsonp=jsonp"
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.text)
        return {}


if __name__ == '__main__':
    update_bilibili_info()
