from django.shortcuts import render, HttpResponse
import requests


def average_salary(request):
    url = "http://127.0.0.1:8000/u/jsonPlayer/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    human = response.text

    sum_salary = 0
    sum_players = 0

    players = human.split('number')
    for player in players[1:]:
        num = ''
        start = 0
        start += player.index('salary')
        start += 8
        for n in player[start:]:
            if n.isnumeric() is True:
                num += n
            else:
                break
        integer = int(num)
        sum_salary += integer
        sum_players += 1

    average = int(sum_salary / sum_players)

    poor = []
    for player in players[1:]:
        num = ''
        start = 0
        start += player.index('salary')
        start += 8
        for n in player[start:]:
            if n.isnumeric() is True:
                num += n
            else:
                break
        integer = int(num)
        if integer < average:
            poor.append(player)

    poor2 = []
    for po in poor:
        name = ''
        start = 0
        start += po.index('last_name')
        start += 12
        for n in po[start:]:
            if n.isalpha() is True:
                name += n
            else:
                break
        poor2.append(name)

    return render(request, 'external/average.html', {'poor2': poor2})
