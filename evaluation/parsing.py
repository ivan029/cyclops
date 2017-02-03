import sys
import os
import time as timing
import datetime


def find_slize(in_array, actual_start, actual_end, fist_time):
    day = 0
    def normalize(date):
        day_delta = datetime.datetime.strptime(date.split('T')[0], "%Y-%m-%d") - datetime.datetime.strptime(fist_time.split('T')[0], "%Y-%m-%d")
        my_date = datetime.datetime.strptime(date.split('T')[1].split('.')[0], "%H:%M:%S") + datetime.timedelta(hours=1) + day_delta
        return my_date
    actual_start = normalize(actual_start)
    actual_end = normalize(actual_end)
    array = []
    for i in range(len(in_array)):
        if datetime.datetime.strptime(in_array[i], "%H:%M:%S").time() == datetime.time():
            day +=1
        time = datetime.datetime.strptime(in_array[i], "%H:%M:%S") + datetime.timedelta(days=day)
        if time >= actual_start:
            array.append(in_array[i])
            if actual_end < time:
                if len(array) < 2:
                    array.append(in_array[i-1])
                return array


def get_data_from_time(data_dict, times, source):
        for time in times:
            for data in data_dict:
                if data["time"] == time:
                    for point in source:
                        print data['time'], data[point]


def parse_output(path, data_map):
    timing.sleep(3)
    count = 1
    first_date = ""
    target = open(path + '/full_output.txt', 'r')
    sys.stdout = open(path + '/parsed_output.txt', 'w+')
    data_file = open(path + '/data.txt', 'r')
    data_dict = []
    list_of_all_times = []
    for data in data_file.read().split("alpha - "):
        point = {"time": data.split(",")[0]}
        for line in data.split("\n"):
            if " udr.jar" in line:
                point['udr'] = line
            if " cdr.jar" in line:
                point['cdr'] = line
            if " billing.jar" in line:
                point['billing'] = line
            if " coin_cdr.jar" in line:
                point['coin_cdr'] = line
            if " coin_bill.jar" in line:
                point['coin_bill'] = line
        if len(point) == 6:
            data_dict.append(point)
    for time_unit in data_dict:
        list_of_all_times.append(time_unit['time'])

    for block in target.read().split('with parameters: '):
        started = []
        ended = []
        range_time = []
        has_started = False
        has_ended = False
        for line in block.split("\n"):
            if has_started or has_ended:
                range_time.append(line)
                has_started = False
                has_ended = False
            if 'number' in line:
                print line
            if "started" in line:
                started.append(float(line.split(" ")[1]))
                has_started = True
            if "ended" in line:
                ended.append(float(line.split(" ")[1]))
                has_ended = True
        if started and ended:
            if count == 1:
                first_date = range_time[0]
                count -= 1
            for point in data_map:
                position = point['position']
                print str(ended[position] - started[position])
                get_data_from_time(data_dict, find_slize(list_of_all_times,
                                                         range_time[position*2],
                                                         range_time[position*2 + 1], first_date),
                                   point['source'])

data_map = [{'position': -1, 'source': ['cdr', 'coin_bill', 'billing']}]
parse_output('output/billing/2016-11-24T16:55:18.180465', data_map)

#my_array = [ '23:59:52', '23:59:53', '23:59:54', '23:59:55', '23:59:56', '23:59:57', '23:59:58', '23:59:59', '00:00:00', '00:00:01', '00:00:03', '00:00:04', '00:00:05', '00:00:06', '00:00:07', '00:00:08', '00:00:09', '00:00:10', '00:00:11', '00:00:12', '00:00:13', '00:00:14', '00:00:15', '00:00:16', '00:00:17', '00:00:18', '00:00:19', '00:00:20', '00:00:21', '00:00:22', '00:00:23', '00:00:24', '00:00:25', '00:00:26', '00:00:27', '00:00:28', '00:00:29', '00:00:30', '00:00:31', '00:00:32', '00:00:33', '00:00:34', '00:00:35', '00:00:36', '00:00:37', '00:00:38', '00:00:39', '00:00:40', '00:00:42', '00:00:43', '00:00:44', '00:00:45', '00:00:46', '00:00:47', '00:00:48', '00:00:49', '00:00:50', '00:00:51', '00:00:52', '00:00:53', '00:00:54', '00:00:55', '00:00:56', '00:00:57', '00:00:58', '00:00:59', '00:01:00', '00:01:01', '00:01:02', '00:01:03', '00:01:04', '00:01:05', '00:01:06', '00:01:07', '00:01:08', '00:01:09', '00:01:10', '00:01:11', '00:01:12', '00:01:13', '00:01:14', '00:01:15', '00:01:16', '00:01:17', '00:01:18', '00:01:19', '00:01:21', '00:01:22', '00:01:23', '00:01:24', '00:01:25', '00:01:26', '00:01:27', '00:01:28', '00:01:29', '00:01:30', '00:01:31', '00:01:32', '00:01:33', '00:01:34', '00:01:35', '00:01:36', '00:01:37', '00:01:38', '00:01:39', '00:01:40', '00:01:41', '00:01:42', '00:01:43', '00:01:44', '00:01:45', '00:01:46', '00:01:47', '00:01:48', '00:01:49', '00:01:50', '00:01:51', '00:01:52', '00:01:53', '00:01:54', '00:01:55', '00:01:56', '00:01:57', '00:01:58', '00:02:00', '00:02:01', '00:02:02', '00:02:03', '00:02:04', '00:02:05', '00:02:06', '00:02:07', '00:02:08', '00:02:09', '00:02:10', '00:02:11', '00:02:12', '00:02:13', '00:02:14', '00:02:15', '00:02:16', '00:02:17', '00:02:18', '00:02:19', '00:02:20', '00:02:21', '00:02:22', '00:02:23', '00:02:24', '00:02:25', '00:02:26', '00:02:27', '00:02:28', '00:02:29', '00:02:30', '00:02:31', '00:02:32', '00:02:33', '00:02:34', '00:02:35', '00:02:37', '00:02:38', '00:02:39', '00:02:40', '00:02:41', '00:02:42', '00:02:43', '00:02:44', '00:02:45', '00:02:46', '00:02:47', '00:02:48', '00:02:49', '00:02:50', '00:02:51', '00:02:52', '00:02:53', '00:02:54', '00:02:55', '00:02:56', '00:02:57', '00:02:58', '00:02:59', '00:03:00', '00:03:01', '00:03:02', '00:03:03', '00:03:04', '00:03:05', '00:03:06', '00:03:07', '00:03:08', '00:03:09', '00:03:10', '00:03:11', '00:03:12', '00:03:13', '00:03:14', '00:03:15', '00:03:16', '00:03:17', '00:03:19', '00:03:20', '00:03:21', '00:03:22', '00:03:23', '00:03:24', '00:03:25', '00:03:26', '00:03:27', '00:03:28', '00:03:29', '00:03:30', '00:03:31', '00:03:32', '00:03:33', '00:03:34', '00:03:35', '00:03:36', '00:03:37', '00:03:38', '00:03:39', '00:03:40', '00:03:41', '00:03:42', '00:03:43', '00:03:44', '00:03:45', '00:03:46', '00:03:47', '00:03:48', '00:03:49', '00:03:50', '00:03:51', '00:03:52', '00:03:53', '00:03:54', '00:03:55', '00:03:56', '00:03:57', '00:03:59', '00:04:00', '00:04:01', '00:04:02', '00:04:03', '00:04:04', '00:04:05', '00:04:06', '00:04:07', '00:04:08', '00:04:09', '00:04:10', '00:04:11', '00:04:12', '00:04:13', '00:04:14', '00:04:15', '00:04:16', '00:04:17', '00:04:18', '00:04:19', '00:04:20', '00:04:21', '00:04:22', '00:04:23', '00:04:24', '00:04:25', '00:04:26', '00:04:27', '00:04:28', '00:04:29', '00:04:30', '00:04:31', '00:04:32', '00:04:33', '00:04:34', '00:04:35', '00:04:36', '00:04:37', '00:04:38', '00:04:40', '00:04:41', '00:04:42', '00:04:43', '00:04:44', '00:04:45', '00:04:46', '00:04:47', '00:04:48', '00:04:49', '00:04:50', '00:04:51', '00:04:52', '00:04:53', '00:04:54', '00:04:55', '00:04:56', '00:04:57', '00:04:58', '00:04:59', '00:05:00', '00:05:01', '00:05:02', '00:05:03', '00:05:04', '00:05:05', '00:05:06', '00:05:07', '00:05:08', '00:05:09', '00:05:10', '00:05:11', '00:05:12', '00:05:13', '00:05:14', '00:05:15', '00:05:16', '00:05:17', '00:05:19', '00:05:20', '00:05:21', '00:05:22', '00:05:23', '00:05:24', '00:05:25', '00:05:26', '00:05:27', '00:05:28', '00:05:29', '00:05:30', '00:05:31', '00:05:32', '00:05:33', '00:05:34', '00:05:35', '00:05:36', '00:05:37', '00:05:38', '00:05:39', '00:05:40', '00:05:41', '00:05:42', '00:05:43', '00:05:44', '00:05:45', '00:05:46', '00:05:47', '00:05:48', '00:05:49', '00:05:50', '00:05:51', '00:05:52', '00:05:53', '00:05:54', '00:05:55', '00:05:56', '00:05:57', '00:05:58', '00:06:00', '00:06:01', '00:06:02', '00:06:03', '00:06:04', '00:06:05', '00:06:06', '00:06:07', '00:06:08', '00:06:09', '00:06:10', '00:06:11', '00:06:12', '00:06:13', '00:06:14', '00:06:15', '00:06:16', '00:06:17', '00:06:18', '00:06:19', '00:06:20', '00:06:21', '00:06:22', '00:06:23', '00:06:24', '00:06:25', '00:06:26', '00:06:27', '00:06:28', '00:06:29', '00:06:30', '00:06:31', '00:06:32', '00:06:33', '00:06:34', '00:06:35', '00:06:37', '00:06:38', '00:06:39', '00:06:40', '00:06:41', '00:06:42', '00:06:43', '00:06:44', '00:06:45', '00:06:46', '00:06:47', '00:06:48', '00:06:49', '00:06:50', '00:06:51', '00:06:52', '00:06:53', '00:06:54', '00:06:55', '00:06:56', '00:06:57', '00:06:58', '00:06:59', '00:07:00', '00:07:01', '00:07:02', '00:07:03', '00:07:04', '00:07:05', '00:07:06', '00:07:07', '00:07:08', '00:07:09', '00:07:10', '00:07:11', '00:07:13', '00:07:14', '00:07:15', '00:07:16', '00:07:17', '00:07:18', '00:07:19', '00:07:20', '00:07:21', '00:07:22', '00:07:23', '00:07:24', '00:07:25', '00:07:26', '00:07:27', '00:07:28', '00:07:29', '00:07:30', '00:07:31', '00:07:32', '00:07:33', '00:07:34', '00:07:35', '00:07:36', '00:07:37', '00:07:38', '00:07:39', '00:07:40', '00:07:41', '00:07:42', '00:07:43', '00:07:44', '00:07:45', '00:07:46', '00:07:47', '00:07:48', '00:07:50', '00:07:51', '00:07:52', '00:07:53', '00:07:54', '00:07:55', '00:07:56', '00:07:57', '00:07:58', '00:07:59', '00:08:00', '00:08:01', '00:08:02', '00:08:03', '00:08:04', '00:08:05', '00:08:06', '00:08:07', '00:08:08', '00:08:09', '00:08:10', '00:08:11', '00:08:12', '00:08:13', '00:08:14', '00:08:15', '00:08:16', '00:08:17', '00:08:18', '00:08:19', '00:08:20', '00:08:21', '00:08:22', '00:08:23', '00:08:24', '00:08:25', '00:08:26', '00:08:27', '00:08:29', '00:08:30', '00:08:31', '00:08:32', '00:08:33', '00:08:34', '00:08:35', '00:08:36', '00:08:37', '00:08:38', '00:08:39', '00:08:40', '00:08:41', '00:08:42', '00:08:43', '00:08:44', '00:08:45', '00:08:46', '00:08:47', '00:08:48', '00:08:49', '00:08:50', '00:08:51', '00:08:52', '00:08:53', '00:08:54', '00:08:55', '00:08:56', '00:08:57', '00:08:58', '00:08:59', '00:09:00', '00:09:01', '00:09:02', '00:09:03', '00:09:04', '00:09:05', '00:09:07', '00:09:08', '00:09:09', '00:09:10', '00:09:11', '00:09:12', '00:09:13', '00:09:14', '00:09:15', '00:09:16', '00:09:17', '00:09:18', '00:09:19', '00:09:20', '00:09:21', '00:09:22', '00:09:23', '00:09:24', '00:09:25', '00:09:26', '00:09:27', '00:09:28', '00:09:29', '00:09:30', '00:09:31', '00:09:32', '00:09:33', '00:09:34', '00:09:35', '00:09:36', '00:09:37', '00:09:38', '00:09:39', '00:09:40', '00:09:41', '00:09:43', '00:09:44', '00:09:45', '00:09:46', '00:09:47', '00:09:48', '00:09:49', '00:09:50', '00:09:51', '00:09:52', '00:09:53', '00:09:54', '00:09:55', '00:09:56', '00:09:57', '00:09:58', '00:09:59', '00:10:00', '00:10:01', '00:10:02', '00:10:03', '00:10:04', '00:10:05', '00:10:06', '00:10:07', '00:10:08', '00:10:09', '00:10:10', '00:10:11', '00:10:12', '00:10:13', '00:10:14', '00:10:15', '00:10:16', '00:10:17', '00:10:18', '00:10:19', '00:10:20', '00:10:21', '00:10:23', '00:10:24', '00:10:25', '00:10:26', '00:10:27', '00:10:28', '00:10:29', '00:10:30', '00:10:31', '00:10:32', '00:10:33', '00:10:34', '00:10:35', '00:10:36', '00:10:37', '00:10:38', '00:10:39', '00:10:40', '00:10:41', '00:10:42', '00:10:43', '00:10:44', '00:10:45', '00:10:46', '00:10:47', '00:10:48', '00:10:49', '00:10:50', '00:10:51', '00:10:52', '00:10:53', '00:10:54', '00:10:55', '00:10:56', '00:10:57', '00:10:58', '00:10:59', '00:11:00', '00:11:01', '00:11:03', '00:11:04', '00:11:05', '00:11:06', '00:11:07', '00:11:08', '00:11:09', '00:11:10', '00:11:11', '00:11:12', '00:11:13', '00:11:14', '00:11:15', '00:11:16', '00:11:17', '00:11:18', '00:11:19', '00:11:20', '00:11:21', '00:11:22', '00:11:23', '00:11:24', '00:11:25', '00:11:26', '00:11:27', '00:11:28', '00:11:29', '00:11:30', '00:11:31', '00:11:32', '00:11:33', '00:11:34', '00:11:35', '00:11:36', '00:11:37', '00:11:38', '00:11:39', '00:11:40', '00:11:41', '00:11:42', '00:11:43', '00:11:45', '00:11:46', '00:11:47', '00:11:48', '00:11:49', '00:11:50', '00:11:51', '00:11:52', '00:11:53', '00:11:54', '00:11:55', '00:11:56', '00:11:57', '00:11:58', '00:11:59', '00:12:00', '00:12:01', '00:12:02', '00:12:03', '00:12:04', '00:12:05', '00:12:06', '00:12:07', '00:12:08', '00:12:09', '00:12:10', '00:12:11', '00:12:12', '00:12:13', '00:12:14', '00:12:15', '00:12:16', '00:12:17', '00:12:18', '00:12:19', '00:12:20']
#print find_slize(my_array,
#                '2016-11-19T00:11:02.470553',
#                '2016-11-19T00:12:15.425844',
#                 '2016-11-18T16:12:27.720134')