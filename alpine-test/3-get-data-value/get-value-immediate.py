def test_LIFELOG_immediate(int_client):

  urls = []
  with open(f'{DATADIR}/immediate-url.txt', 'r') as f:
    while True:
      line = f.readline()
      if not line:
        break
      urls.append(line)

  print(urls)

  with open(f'{DATADIR}/res-immediate.json', 'w', encoding='UTF-8-sig') as f:
    for url in urls:
      response = requests.get(url)
      f.write(json.dumps(response.json(), ensure_ascii=False))
      f.write("\n")
      print(response.json())
