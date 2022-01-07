import requests

cookie = input('Cokkies: ')
authority = "https://fap.fpt.edu.vn"

term = 15
group = 'IA1501'

payload = {
    'authority':authority,
    'accept':'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9',
    'cookie':cookie,
    'sec-ch-ua':'"Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'image',
    'sec-fetch-mode':'no-cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53'
}

link = f'https://fap.fpt.edu.vn/Schedule/TimeTable.aspx?campus=6&term={term}&group={group.upper()}'
link =  'https://fap.fpt.edu.vn/Student.aspx?view=user'

class Subject:
    subject_code = None
    start = None
    end = None

    def __init__(self, _c, _s, _e) -> None:
        self.subject_code = _c
        self.start = _s
        self.end = _e


def main():
    res = requests.get(url=link, headers=payload)
    with open('output.html', 'w+', encoding='utf8') as f:
        print(res.text, file=f)


main()

index2time = {
    1: "07:00 08:30",
    2: "",
    3: "",
    4: "12:45 14:15",
    5: "14:30 16:00",
    6: "16:15 17:45"
}

name2url = {
    'HuongLH3': 'https://meet.google.com/xgd-rbhr-khn',
    'TrietNM3': 'https://meet.google.com/zgh-uejr-esb',
    'VinhND18': 'https://meet.google.com/hdw-tgud-new'
}
