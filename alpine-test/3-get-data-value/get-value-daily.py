from pathlib import Path

DATADIR = Path(__file__).parent / 'data'


def test_LIFELOG_daily(int_client):

  urls = []
  with open(f'{DATADIR}/daily-url.txt', 'r') as f:
    while True:
      line = f.readline()
      if not line:
        break
      urls.append(line)

  with open(f'{DATADIR}/res-daily.json', 'w', encoding='UTF-8-sig') as f:
    for url in urls:
      response = requests.get(url)
      f.write(json.dumps(response.json(), ensure_ascii=False))
      f.write("\n")
