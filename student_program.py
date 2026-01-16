# Student Subject Avg

student = [[12,54,6,24,7],[3,6,8,53,7],[64,7,92,4,8]]

def test(student):
    avg_sub = {}
    x = 0
    # for i in range(len(student[0])):
    #     avg_sub[i] = (student[0][x] + student[1][x] + student[2][x]) // len(student)
    #     x+=1

    for i in range(len(student[0])):
        total = 0
        for s in student:
            total+=s[i]
        avg_sub[i] = total // len(student)

    smallest_avg = float("inf")
    sub_index = None

    print('avg_sub: ', avg_sub)
    for k,v in avg_sub.items():
        if v < smallest_avg:
            smallest_avg = v
            sub_index = k
    print('smallest_avg: ', smallest_avg)
    print('sub_index: ', sub_index)

    for i in student:
        i.pop(sub_index)

    subject_total_student = {}
    for i in range(len(student)):
        subject_total_student[i] = sum(student[i])
    print("student - ", student)
    print('subject_total_student: ', subject_total_student)
        
test(student)