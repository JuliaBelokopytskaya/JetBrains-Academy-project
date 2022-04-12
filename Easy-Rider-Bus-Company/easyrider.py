# Write your awesome code here
import json
import re
from datetime import datetime

def format_validation(bus_bd):
    count_err = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    pattern_a_time = re.compile(r'^[012]\d:[0-5]\d$')
    pattern_stop_name = re.compile(r'^(([A-Z]\w+) )+(Road|Avenue|Boulevard|Street)$')
    for i in range(len(bus_bd)):
        if (not isinstance(bus_bd[i]["bus_id"], int)) or (bus_bd[i]["bus_id"] is None):
            count_err["bus_id"] += 1
        if (not isinstance(bus_bd[i]["stop_id"], int)) or (bus_bd[i]["stop_id"] is None):
            count_err["stop_id"] += 1
        if not (isinstance(bus_bd[i]["stop_name"], str)) or not(re.findall(pattern_stop_name, bus_bd[i]["stop_name"])):
            count_err["stop_name"] += 1
        if (not isinstance(bus_bd[i]["next_stop"], int)) or (bus_bd[i]["next_stop"] is None):
            count_err["next_stop"] += 1
        if not (isinstance(bus_bd[i]["stop_type"], str)) or (bus_bd[i]["stop_type"] not in ["", "S", "O", "F"]):
            count_err["stop_type"] += 1
        if not(isinstance(bus_bd[i]["a_time"], str)) or not(re.findall(pattern_a_time, bus_bd[i]["a_time"])):
            count_err["a_time"] += 1
    return count_err

def out_err_format_val(count_err):
    print(f"Format validation: {sum(list(count_err.values()))} errors")
    for key in count_err.keys():
        print(f"{key}: {count_err[key]}")

def num_stops(bus_num, bus_bd):
    stops = [[x, 0] for x in bus_num]
    for i in range(len(bus_bd)):
        for j in range(len(bus_num)):
            if bus_bd[i]["bus_id"] == bus_num[j]:
                a = [bus_bd[i]["bus_id"], bus_bd[i]["stop_id"]]
                if a not in stops:
                    stops.append(a)
                    stops[j][1] += 1
    return stops

def out_num_stops(stops):
    print("Line names and number of stops:")
    for key in stops.keys():
        print(f"{key}:, stops: {stops[key]}")

def name_stop_type(bus_num, bus_bd):
    start_st = dict.fromkeys(bus_num, 0)
    end_st = dict.fromkeys(bus_num, 0)
    transfer_st, transfer_stops = [], []
    for i in bus_num:
        for j in range(len(bus_bd)):
            if bus_bd[j]["bus_id"] == i:
                if bus_bd[j]["stop_type"] == "S":
                    if start_st[i] == 0:
                        start_st[i] = bus_bd[j]["stop_name"]
                    else:
                        print(f"There is no start or end stop for the line: {i}")
                        return
                elif bus_bd[j]["stop_type"] == "F":
                    if end_st[i] == 0:
                        end_st[i] = bus_bd[j]["stop_name"]
                    else:
                        print(f"There is no start or end stop for the line: {i}")
                        return
        if start_st[i] == 0 or end_st[i] == 0:
            print(f"There is no start or end stop for the line: {i}")
            return
    start_stops = sorted(list(set(start_st.values())))
    end_stops = sorted(list(set(end_st.values())))
    for i in range(len(bus_bd)):
        transfer_st.append(bus_bd[i]["stop_name"])
    for i in range(len(transfer_st)):
        if transfer_st.count(transfer_st[i]) > 1:
            transfer_stops.append(transfer_st[i])
    transfer_stops = sorted(list(set(transfer_stops)))
    return[start_stops, transfer_stops, end_stops]

def out_name_stop_type(stop_type):
        print(f"Start stops: {len(stop_type[0])} {stop_type[0]}")
        print(f"Transfer stops: {len(stop_type[1])} {stop_type[1]}")
        print(f"Finish stops: {len(stop_type[2])} {stop_type[2]}")

def time_error(bus_num, bus_bd):
    time_err = {}
    for i in bus_num:
        a, index = [], []
        for j in range(len(bus_bd)):
            if bus_bd[j]["bus_id"] == i:
                a.append(datetime.strptime(bus_bd[j]["a_time"], "%H:%M"))
                index.append(j)
        for t in range(1, len(a)):
            if (a[t]-a[t-1]).total_seconds() <= 0:
                time_err[i] = bus_bd[index[t]]["stop_name"]
                break
    return time_err

def out_time_error(time_err):
    if len(time_err) > 0:
        print("Arrival time test:")
        for key in time_err.keys():
            print(f'bus_id line {key}: wrong time on station {time_err[key]}')
    else:
        print("Arrival time test:")
        print("OK")

def stop_type_error(bus_num, bus_bd, stop_type):
    stop_type_err=[]
    for i in bus_num:
        for j in range(len(bus_bd)):
            if bus_bd[j]["bus_id"] == i:
                if bus_bd[j]["stop_type"] == "O":
                    if bus_bd[j]["stop_name"] in stop_type[0] or bus_bd[j]["stop_name"] in stop_type[2] or bus_bd[j]["stop_name"] in stop_type[1]:
                        stop_type_err.append(bus_bd[j]["stop_name"])
    return stop_type_err

def out_stop_type_error(stop_type_err):
    if len(stop_type_err) > 0:
        print("On demand stops test:")
        print(f'Wrong stop type: {sorted(stop_type_err)}')
    else:
        print("On demand stops test:")
        print("OK")

json_str = input()
bus_bd = json.loads(json_str)
bus_num = []
count_err = format_validation(bus_bd)
out_err_format_val(count_err)
for i in range(len(bus_bd)):
    if bus_bd[i]["bus_id"] not in bus_num:
        bus_num.append(bus_bd[i]["bus_id"])
stops = num_stops(bus_num, bus_bd)
out_num_stops(stops)
stop_type = name_stop_type(bus_num, bus_bd)
out_name_stop_type(stop_type)
time_err = time_error(bus_num, bus_bd)
out_time_error(time_err)
stop_type_err = stop_type_error(bus_num, bus_bd, stop_type)
out_stop_type_error(stop_type_err)








