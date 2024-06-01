# -*- coding: utf-8 -*-
import datetime
import pytz

def boj_rating_to_lv(rating):
    if rating < 30: return 0
    if rating < 150: return rating // 30
    if rating < 200: return 5
    if rating < 500: return (rating-200) // 100 + 6
    if rating < 1400: return (rating-500) // 150 + 9
    if rating < 1600: return 15
    if rating < 1750: return 16
    if rating < 1900: return 17
    if rating < 2800: return (rating-1900) // 100 + 18
    if rating < 3000: return (rating-2800) // 50 + 27
    return 31


def create_grass(tier, solved):
    solved_dict = {}
    # 18주 내 가장 많이 문제를 풀은 날의 solved count가 4 미만일 경우 4으로 설정
    solved_dict['solved_max'] = 4

    for i,value in enumerate(tier["grass"]):
        solved_dict[value['date']] = {'tier': value['value']}
        
    for i,value in enumerate(solved["grass"]):
        solved_dict[value['date']]['solved'] = value['value']
        if (value['value'] is not int):
            solved_dict[value['date']]['solved'] = 0
        print(((solved_dict['solved_max'], solved_dict[value['date']]['solved'])))
        solved_dict['solved_max'] = max(solved_dict['solved_max'], solved_dict[value['date']]['solved'])
        
    solved_dict['solved_max'] = min(solved_dict['solved_max'], 50)
    return solved_dict


def get_starting_day():
    # 오늘 날짜와 오늘로부터 17주 전 일요일의 날짜를 반환
    # solved.ac는 하루의 시작이 오전 6시이므로 UTC+3으로 변경
    today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    # Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6
    weekday = today.isoweekday() % 7
    
    return today.strftime('%Y-%m-%d'), (today - datetime.timedelta(days=weekday + 119)).strftime('%Y-%m-%d')


def get_tomorrow(timestamp):
    # timestamp로부터 하루 뒤의 날짜를 반환
    timedata = datetime.datetime.strptime(timestamp, '%Y-%m-%d')
    tomorrow = timedata + datetime.timedelta(days=1)

    return tomorrow.strftime('%Y-%m-%d')


# solved.ac에서 사용하는 티어 id (0:Unrated, 1~5:Bronze, ..., 31:Master)
def get_tier_name(id: int):
  if id == 0: return 'Unrated'
  lut = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby', 'Master']
  tier = lut[(id - 1) // 5]
  lv = ((id - 1) % 5) + 1
  if tier == 'Master': return 'Master'
  return '{tier} {lv}'.format(tier=tier, lv=lv)


# 티어명을 solved.ac에서 사용하는 티어 id로 변환 ('Bronze 4' => 2)
def get_tier_id(name: str):
  name = name.lower()
  arr = name.split(' ') + [None] # padding when level is empty
  tier = arr[0]
  lv = int(arr[1]) if arr[1] else 0
  lut = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'ruby', 'master']
  if tier in lut:
    if tier == 'master': return 31
    return lut.index(tier) * 5 + lv
  return 0 # unrated
