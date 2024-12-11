import datetime
import json
import os

import requests
from AocCommon import get_league_data_from_api


def get_data_from_cache_or_api(league_id, year):
    cache_file = f"cached_leaderboard_{league_id}_{year}.json"
    now = (
        datetime.datetime.now(datetime.timezone.utc)
        .replace(tzinfo=datetime.timezone.utc)
        .timestamp()
    )
    if os.path.isfile(cache_file):
        with open(cache_file, "r") as infile:
            data = json.load(infile)
        cache_time = data.get("cache_time", None)
        if cache_time is not None and (now - cache_time) < 15 * 60:
            print(
                f"Getting from cache as delta is only {round(
                    now - cache_time)} seconds."
            )
            return data

    data = get_league_data_from_api(league_id, year)
    data["cache_time"] = now

    with open(cache_file, "w") as outfile:
        outfile.write(json.dumps(data, indent=4))
    return data


data = get_data_from_cache_or_api(2257599, 2024)

user_map = {}
for _, m in data["members"].items():
    name = m["name"]
    if name is None:
        continue
    for day, dat in m["completion_day_level"].items():
        if name not in user_map:
            user_map[name] = {}
        d = {}
        times = [None, None]
        for v, i in enumerate(["1", "2"]):
            if dat.get(i, None) is not None:
                times[v] = int(dat.get(i)["get_star_ts"])
                d[f"Star {i} Timestamp"] = datetime.datetime.fromtimestamp(
                    times[v], datetime.timezone.utc
                ).strftime("%H:%M %Y-%m-%d")
        if times[0] is not None and times[1] is not None:
            d["Star 2 Time"] = times[1] - times[0]
        user_map[name][day] = d

day = 0
while True:
    day += 1
    times = []
    for u, ud in user_map.items():
        if str(day) in ud:
            if "Star 2 Time" in ud[str(day)]:
                times.append((u, ud[str(day)]["Star 2 Time"]))
    if len(times) == 0:
        break
    print(f"Day {day}")
    for i in sorted(times, key=lambda k: k[1]):
        print(f"{i[0]:>30} | {i[1]:>8}")
# print(json.dumps(user_map, indent=4))
