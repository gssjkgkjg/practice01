class CourseHistory:
    def __init__(self):
        self.retaken_course = None
        self.course_id_map = {'id': -1}
        self.history = []
        self.archive_grade = {}
        self.submit_grade = {}

    @classmethod
    def credit(cls, x):
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

    def allocate_course_id(self, course_name):
        if course_name not in self.course_id_map:
            new_id = self.course_id_map['id'] + 1
            self.course_id_map['id'] = new_id
            self.course_id_map[course_name] = new_id
            self.course_id_map[new_id] = course_name
            self.retaken_course = False

            return new_id
        else:
            self.retaken_course = True

            return self.course_id_map[course_name]

    def input_process(self):
        course_name = input("과목명을 입력하세요:\n")
        course_id = self.allocate_course_id(course_name)
        grand_point = float(input("학점을 입력하세요:\n"))
        grade_point = input("평점을 입력하세요:\n")
        grade_score = self.credit(grade_point)

        if self.retaken_course:
            if grade_score > self.credit(self.history[course_id][2]):
                self.history[course_id] = (course_id, grand_point, grade_point)
        else:
            self.history.append((course_id, grand_point, grade_point))

    def print_process(self):
        for temp_tuple1 in self.history:
            print('[' + self.course_id_map[temp_tuple1[0]] + ']', str(int(temp_tuple1[1])) + '학점:', temp_tuple1[2])

    def query_process(self):
        course_name = input('과목명을 입력하세요: ')

        if course_name not in self.course_id_map:
            print('해당하는 과목이 없습니다.')
        else:
            temp_tuple0 = self.history[self.course_id_map[course_name]]
            print('[' + self.course_id_map[temp_tuple0[0]] + ']', str(int(temp_tuple0[1])) + '학점:', temp_tuple0[2])

    def calculate_process(self):
        total_for_open = 0.0
        total_for_submit = 0.0
        application_for_open = 0.0
        application_for_submit = 0.0

        for temp_tuple2 in self.history:
            total_for_open += self.credit(temp_tuple2[2]) * temp_tuple2[1]
            application_for_open += temp_tuple2[1]

            if temp_tuple2[2] != 'F':
                total_for_submit += self.credit(temp_tuple2[2]) * temp_tuple2[1]
                application_for_submit += temp_tuple2[1]

        gpa_for_submit = round(total_for_submit / application_for_submit, 2)
        gpa_for_open = round(total_for_open / application_for_open, 2)

        print('제출용:', str(application_for_submit) + '학점', '(GPA:', str(gpa_for_submit) + ')')
        print('열람용:', str(application_for_open) + '학점', '(GPA:', str(gpa_for_open) + ')')


course_history = CourseHistory()

while True:
    selection = int(input("""작업을 선택하세요.
1. 입력
2. 출력
3. 조회
4. 계산
5. 종료
"""))
    match selection:
        case 1:
            course_history.input_process()
        case 2:
            course_history.print_process()
        case 3:
            course_history.query_process()
        case 4:
            course_history.calculate_process()
        case 5:
            print('프로그램을 종료합니다.')
            break
        case _:
            print('잘못된 입력입니다.')
