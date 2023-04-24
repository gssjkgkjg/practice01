# 학점_계산기 20230423 홍제연

def credit(x):
    match x:
        case 'A+':
            return 4.5
        case 'A':
            return 4.0
        case 'B+':
            return 3.5
        case 'B':
            return 3.0
        case 'C+':
            return 2.5
        case 'C':
            return 2.0
        case 'D+':
            return 1.5
        case 'D':
            return 1.0
        case 'F':
            return 0.0


subject_dict = {}
course_list = []
subject_key = 1

while True:
    selection = int(input("""작업을 선택하세요.
1. 입력
2. 출력
3. 계산
"""))
    match selection:
        case 1:
            subject_name = input("과목명을 입력하세요:\n")
            grand_point = float(input("학점을 입력하세요:\n"))
            grade_point = input("평점을 입력하세요:\n")
            subject_dict[subject_key] = subject_name
            course_list.append((subject_key, grand_point, grade_point))
            subject_key += 1
        case 2:
            for temp_tuple1 in course_list:
                print('[' + subject_dict[temp_tuple1[0]] + ']', str(int(temp_tuple1[1])) + '학점:', temp_tuple1[2])
        case 3:
            total_for_open = 0.0
            total_for_submit = 0.0
            application_for_open = 0.0
            application_for_submit = 0.0
            for temp_tuple2 in course_list:
                total_for_open += credit(temp_tuple2[2]) * temp_tuple2[1]
                application_for_open += temp_tuple2[1]
                if temp_tuple2[2] != 'F':
                    total_for_submit += credit(temp_tuple2[2]) * temp_tuple2[1]
                    application_for_submit += temp_tuple2[1]

            gpa_for_submit = round(total_for_submit / application_for_submit, 2)
            gpa_for_open = round(total_for_open / application_for_open, 2)
            print('제출용:', str(total_for_submit) + '학점', '(GPA:', str(gpa_for_submit) + ')')
            print('열람용:', str(total_for_open) + '학점', '(GPA:', str(gpa_for_open) + ')')
            print('\n프로그램을 종료합니다.')
            break
        case _:
            print('잘못된 입력입니다.')
