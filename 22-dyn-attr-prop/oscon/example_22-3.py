import json
from explore0 import FrozenJSON

raw_feed = json.load(open('data/osconfeed.json'))
feed = FrozenJSON(raw_feed)

print(len(feed.Schedule.speakers))
print(feed.keys())
print(sorted(feed.Schedule.keys()))

for key, value in sorted(feed.Schedule.items()): # <4>
    print(f'{len(value):3} {key}')

print(feed.Schedule.speakers[-1].name)

talk = feed.Schedule.events[40]
print(talk.name)
print(talk.speakers)
# print(talk.flavor)
