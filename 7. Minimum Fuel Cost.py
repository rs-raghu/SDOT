raw_input = input().replace(',', ' ').split()
seats = int(input())
adj = {}
cities = set()
edges = []

for i in range(0, len(raw_input), 2):
    u, v = int(raw_input[i]), int(raw_input[i+1])
    edges.append((u, v))
    cities.add(u)
    cities.add(v)
for city in cities:
    adj[city] = []
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

total_fuel = 0

def get_people_count(curr, parent):
    global total_fuel
    people = 1
    for neighbor in adj[curr]:
        if neighbor != parent:
            count = get_people_count(neighbor, curr)
            cars = (count + seats - 1) // seats
            total_fuel += cars
            people += count   
    return people

if 0 in adj:
    get_people_count(0, -1)
print(total_fuel)