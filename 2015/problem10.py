seq = "1113222113"
for step in range(50):
    if step == 40:
        print("Part 1:",len(seq))
    cur_num = seq[0]
    cur_count = 1
    next_seq = ""
    for i in range(1,len(seq)):
        if seq[i] == cur_num:
            cur_count += 1
        else:
            next_seq += str(cur_count) + cur_num
            cur_num = seq[i]
            cur_count = 1
    seq = next_seq + str(cur_count) + cur_num
print("Part 2:",len(seq))