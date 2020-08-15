import random
from django.shortcuts import render

# Create your views here.

def lotto(request):
    students = [
        '신누리', 
        '김한빈', 
        '김용민', 
        '현성섭',
        '이종하',
        '황경서',
        '안동훈',
        '최정휴',
        '권기현',
        '고영길',
        '옥종훈',
        '김준호',
        '이지영',
        '이영송',
        '이건우',
        '김동현',
        '안광훈',
        '손준희',
        '김민정',
        '박민병',
    ]
    student1 = random.sample(students, 4)
    for student in student1:
        students.remove(student)

    student2 = random.sample(students, 4)
    for student in student2:
        students.remove(student)

    student3 = random.sample(students, 4)
    for student in student3:
        students.remove(student)

    student4 = random.sample(students, 4)
    for student in student4:
        students.remove(student)

    student5 = random.sample(students, 4)
    context = {
        'student1': student1,
        'student2': student2,
        'student3': student3,
        'student4': student4,
        'student5': student5,
    }
    return render(request, 'lotto.html', context)

