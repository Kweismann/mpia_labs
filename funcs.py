import os


class People:
    pass


def Input(file):
    if os.stat(file).st_size == 0:
        return None
    else:
        s = open(file)
        peoples = []
        i = 0
        for x in s:
            peoples.append(People())
            temp_people = x.split(' ')
            peoples[i].f_name = temp_people[0]
            peoples[i].l_name = temp_people[1]
            peoples[i].day = temp_people[2]
            peoples[i].month = temp_people[3]
            peoples[i].year = temp_people[4]
            i += 1
        return peoples


def algorithm(peoples):
    if peoples is None:
        return "Exception: file empty"
    else:
        max_day = [0, 0]
        for x in peoples:
            t_day = x.day
            t_count = 0
            for y in peoples:
                if t_day == y.day:
                    t_count += 1
            if max_day[0] <= t_count:
                max_day[0] = t_count
                max_day[1] = t_day
        return max_day
