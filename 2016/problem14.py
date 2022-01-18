import re
import hashlib
from collections import defaultdict

def find_key_64(additional_hashes):
    salt = "zpqevtbw"
    rx3 = r'(.)\1{2,}'
    rx5 = r'(.)\1{4,}'
    match_5 = defaultdict(list)

    #get a 1000-string head start on the 5 condition
    for i in range(0,1001):
        md5 = hashlib.md5((salt+str(i)).encode("utf-8")).hexdigest()
        for _ in range(additional_hashes):
            md5 = hashlib.md5((md5).encode("utf-8")).hexdigest()
        fives = re.findall(rx5, md5)
        for f in fives:
            match_5[f[0:1]].append(i)

    i = 0
    keys_found = 0
    while True:
        md5 = hashlib.md5((salt+str(i)).encode("utf-8")).hexdigest()
        for _ in range(additional_hashes):
            md5 = hashlib.md5((md5).encode("utf-8")).hexdigest()
        three = re.search(rx3, md5)
        if three:
            char = md5[three.start():three.start()+1]
            for index in match_5[char]:
                if index > i and index <= i + 1000:
                    keys_found += 1
                    if keys_found == 64:
                        return i
                    break
        i += 1
        md5 = hashlib.md5((salt+str(i+1000)).encode("utf-8")).hexdigest()
        for _ in range(additional_hashes):
            md5 = hashlib.md5((md5).encode("utf-8")).hexdigest()
        fives = re.findall(rx5, md5)
        for f in fives:
            match_5[f[0:1]].append(i+1000)

print("Part 1:",find_key_64(0))
print("Part 2:",find_key_64(2016))