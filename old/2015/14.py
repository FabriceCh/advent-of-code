from aocd import get_data
ar = get_data(day=14, year=2015)
ar = ar.splitlines()
print(ar)

ar2 = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]

def extract_deer_from_line(line):
    words = line.split(" ")
    name = words[0]
    speed = int(words[3])
    move_time = int(words[6])
    rest_time = int(words[13])
    return {
        "name": name,
        "speed": speed,
        "move_time": move_time,
        "rest_time": rest_time,
        "position": 0,
        "cur_mode": "move",
        "cur_rest_time": 0,
        "cur_move_time": 0,
        "points": 0
    }

def find_lead(deers):
    maxx, lead = 0, []
    for d in deers:
        if d["position"] > maxx:
            maxx = d["position"]
            lead = [d]
        elif d["position"] == maxx:
            lead.append(d)
    return lead

def part1(seconds):

    deers = []
    for l in ar:
        deers.append(extract_deer_from_line(l))

    for s in range(seconds):
        for deer in deers:
            if deer["cur_mode"] == "move":
                deer["cur_move_time"] += 1
                deer["position"] += deer["speed"]
                if deer["cur_move_time"] == deer["move_time"]:
                    deer["cur_move_time"] = 0
                    deer["cur_mode"] = "rest"
            elif deer["cur_mode"] == "rest":
                deer["cur_rest_time"] += 1
                if deer["cur_rest_time"] == deer["rest_time"]:
                    deer["cur_rest_time"] = 0
                    deer["cur_mode"] = "move"
        ds = find_lead(deers)
        print([d["name"] for d in ds])
        for d in ds:
            d["points"] += 1
    print(deers)
    print(max([d["points"] for d in deers]))

part1(2503)
