import string
import random
import json

# lst =[]
#
for l in range(0, 27, 1):
    random.seed(l*10)

    dict = {
        "id": "{}".format(i),
        "rollno": "{}".format(int(random.uniform(4, 60))),
        "username": "{}".format(
            ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))),
        "password": "{}".format(''.join(
            random.choices(string.ascii_letters + string.punctuation + string.digits, k=int(random.uniform(8, 16))))),
        "email": "{}.{}{}@gmail.com".format(
            ''.join(random.choices(string.ascii_lowercase, k=int(random.uniform(6, 12)))),
            ''.join(random.choices(string.ascii_letters, k=int(random.uniform(6, 12)))),
            int(random.uniform(1, 32))),
        "name": "{} {}".format(''.join(random.choices(string.ascii_letters, k=int(random.uniform(3, 12)))),
                               ''.join(random.choices(string.ascii_letters, k=int(random.uniform(5, 12))))),
        "mobile": "{}".format(int(random.random() * 10000000000)),
        "std": "{}".format(int(random.uniform(11, 13))),
        "physics": "{}".format(int(random.random() * 100)),
        "chemistry": "{}".format(int(random.random() * 100)),
        "computer": "{}".format(int(random.random() * 100)),
        "biology": "{}".format(int(random.random() * 100)),
        "maths": "{}".format(int(random.random() * 100))
    }
#     i += 1
#     lst.append(dict)
#
# for i in lst:
#     print(json.dumps(i, indent=4),",")



lst=[]
sub=["physics","chemistry","english","maths/bio","english/sanskrit"]

