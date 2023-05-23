import random
import json

n = 50
m = 10000

services = []
for i in range(n):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    properties = [random.choice(["price", "stock_count", "partner_content"]) for j in range(a+b)]
    services.append((a, b, properties))

requests = []
for i in range(m):
    trace_id = str(i+1)
    offer_id = str(random.randint(1, n))
    property_name = random.choice(["price", "stock_count", "partner_content"])
    if property_name == "partner_content":
        sub_property_name = random.choice(["title", "description"])
        offer = {"id": offer_id, "partner_content": {sub_property_name: "Some value"}}
    else:
        offer = {"id": offer_id, property_name: random.randint(1, 100)}
    request = {"trace_id": trace_id, "offer": offer}
    requests.append(request)

# записываем данные в файл
with open("input2.txt", "w") as f:
    f.write(f"{n} {m}\n")
    for service in services:
        f.write(f"{service[0]} {service[1]} {' '.join(service[2])}\n")
    for request in requests:
        f.write(json.dumps(request) + "\n")



