import requests


def get_ip_data(ip):
    link = f'http://ip-api.com/json/{ip}'
    result = requests.get(link)
    return result.json()


def find_ips_from_json(ips):
    data = []
    for x in ips:
        data.append(get_ip_data(x['ip']))
    return data


def find_ips_from_txt(file):
    data = []
    for line in file:
        x = line.strip().decode("utf-8")
        ip = get_ip_data(x)
        data.append(ip)
    return data
