import requests
import json
import sys
import socket


def callback(data):
    local_ip = socket.gethostbyname(socket.gethostname())
    items = [
        {
            "title": local_ip,
            "subtitle": "本地的ip",
            "arg": local_ip,
            'icon': {'path': 'IP.png'},
            "valid": "True"
        },
        {
            "title": data.get('ip'),
            "subtitle": "查询的ip",
            "arg": data.get('ip'),
            'icon': {'path': 'IP.png'},
            "valid": "True"
        },
        {
            "title": data.get('country'),
            "subtitle": "所在国家",
            "arg": data.get('country'),
            'icon': {'path': 'guojia.png'},
            "valid": "True"
        },
        {
            "title": data.get('province'),
            "subtitle": "所在省份",
            "arg": data.get('province'),
            'icon': {'path': 'shengfen.png'},
            "valid": "True"
        },
        {
            "title": data.get('city'),
            "subtitle": "所在城市",
            "arg": data.get('city'),
            'icon': {'path': 'chengshi.png'},
            "valid": "True"
        },
        {
            "title": data.get('area') or '无记录',
            "subtitle": "所在县区",
            "arg": data.get('area'),
            'icon': {'path': 'shequ.png'},
            "valid": "True"
        },
        {
            "title": data.get('isp'),
            "subtitle": "IP运营商",
            "arg": data.get('isp'),
            'icon': {'path': 'yunyingshang.png'},
            "valid": "True"
        },
        {
            "title": data.get('net') or '互联网',
            "subtitle": "IP网络类型（局域网、广域网、城域网、互联网）",
            "arg": data.get('net'),
            'icon': {'path': 'type.png'},
            "valid": "True"
        },
    ]

    print(json.dumps({'items': items}))


def main(ip):
    url = 'https://ip.useragentinfo.com/jsonp'
    params = {'ip': ip, 'callback': 'callback'}
    response = requests.get(url, params=params).text
    return exec(response)


def exit_error(ip):
    items = [{
        "title": "ip类型错误",
        "subtitle": ip,
        "arg": '',
        'icon': {'path': 'error.png'},
        "valid": "True"
    }]

    return json.dumps({'items': items})


if __name__ == '__main__':
    query = ''
    if len(sys.argv) > 1:
        query = sys.argv[1]
    try:
        main(query)
    except:
        res = exit_error(query)
        print(res)
