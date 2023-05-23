import json

f = open("inputs/input1.txt")

data_collection = f.readline()
count_sub_servers, count_upd_req = map(int, data_collection.split())

db = {}
change_fields = []


def merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            fields_before = change_fields.copy()
            merge(value, node)
            if fields_before != change_fields:
                change_fields.append(key)

        elif destination.get(key) != value:
            destination[key] = value
            change_fields.append(key)
    return destination


def deepcopy(source):
    destination = {}
    for key, value in source.items():
        if isinstance(value, dict):
            destination[key] = deepcopy(value)
        else:
            destination[key] = value
    return destination


def processing_description_sub_servers(count_sub_servers, count_upd_req):
    all_sub = []
    for _ in range(count_sub_servers):
        sub_description = f.readline().split()
        count_trigger_fields = int(sub_description[0])
        count_shipment_fields = int(sub_description[1])
        triggers = sub_description[2:2+count_trigger_fields]

        if count_shipment_fields:
            shipments = sub_description[-count_shipment_fields:]
        else:
            shipments = []
        all_sub.append((triggers, shipments))

    for _ in range(count_upd_req):
        change_fields.clear()
        update = json.loads(f.readline())
        trace_id = update['trace_id']
        offer = update['offer']
        actual_offer = db.get(offer['id'], None)

        if actual_offer is not None:
            db[offer['id']] = merge(offer, actual_offer)

        else:
            db[offer['id']] = offer
            change_fields.extend(db[offer['id']])

        for trig, ship in all_sub:
            if len(set(change_fields).intersection(set(trig))) > 0:
                duplicate_db = deepcopy(db[offer['id']])
                result = {
                    'trace_id': trace_id, 'offer': duplicate_db
                }
                trig_ship = trig + ship
                del_item = []
                for key in result['offer'].keys():
                    if key not in trig_ship and key != 'id':
                        del_item.append(key)
                if del_item:
                    del result['offer'][del_item[0]]

                if len(result['offer']) != 1:
                    print(result)


processing_description_sub_servers(count_sub_servers, count_upd_req)
