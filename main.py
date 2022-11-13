import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
heroes_names = ['Hulk', 'Captain America', 'Thanos']
new_list = {}


def main():
    r = requests.get(url)
    resp = r.json()
    for el in resp:
        if el['name'] in heroes_names:
            new_list[el['name']] = el['powerstats']['intelligence']
    print(max(new_list, key=new_list.get))


if __name__ == '__main__':
    main()
