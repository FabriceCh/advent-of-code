import json
from aocd import get_data
ar = get_data(day=12, year=2015)
ar = json.loads(ar)

def add_json_nums(json_val, buf):
    if isinstance(json_val, int):
        return json_val
    elif isinstance(json_val, dict):
        ans = 0
        if "red" in json_val.keys() or "red" in json_val.values():
            return 0
        for k, v in json_val.items():
            ans += add_json_nums(k, buf)
            ans += add_json_nums(v, buf)
        return ans
    elif isinstance(json_val, list):
        ans = 0
        for v in json_val:
            ans += add_json_nums(v, buf)
        return ans
    else:
        return 0

def part1(ar):
    ans = 0
    ans = add_json_nums(ar, ans)
    print(ans)

part1(ar)

