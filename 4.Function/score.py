#!/usr/bin/env python
import sys
import csv
import json


def load_from_csv(filepath): #csv를 읽어오는 함수
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {} #학생 점수 딕셔너리

    with open(filepath, 'r', encoding='utf-8') as f:
        #filepath에 있는 CSV 파일을 읽기 모드('r')로 연다.
        #encoding='utf-8'은 한글 깨짐을 막기 위한 지정.
        #with ... as f: 파일을 열고 닫는 과정을 처리하고 f는 파일을 가리키는 변수
        
        csv_reader = csv.reader(f) #csv파일을 읽어서 한 줄씩 리스트로 바꿔주는 도구

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader) #리스트의 첫 줄을 header 안에 저장

        for row in csv_reader: #csv파일 리스트를 한 줄씩 반복하며 
            student_scores[row[0]] = row[1:] 
            #학생 점수 딕셔너리 안에 키는 열 1번째자리(이름)
            #                      값은 열 2번째자리 ~끝(점수)
    return student_scores, header[1:] 
    #학생 점수 딕셔너리와 리스트의 첫 줄(2번자리~끝) 반환


def subject_average(student_scores: dict, subjects: list): #과목별 평균 함수
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """
    sub_avg = {}
    for i in range(len(subjects)):
        total = 0
        for students, scores in student_scores.items():
            total += int(scores[i])
        sub_avg[subjects[i]] = round(total/len(student_scores),2)     

    return sub_avg


    # sub_avg = {} #과목별 평균값 딕셔너리

    # for idx, subject in enumerate(subjects): #과목 수만큼 반복
    #     total = 0
    #     count = 0
    #     for student, scores in student_scores.items(): #학생(키)과 점수(값)를 분리 및 순회
    #         total += int(scores[idx])           
    #         count += 1

    #     sub_avg[subject] = round(total / count, 2) #소수점 두 번째 자리까지 출력
     
    # return sub_avg


def student_average(student_scores: dict):  #학생별 평균 함수
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """

    stud_avg = {}
    for student, scores in student_scores.items():
        total = 0
        for i in scores:
            total += int(i)
        stud_avg[student] = total/len(scores)
    
    return sorted(stud_avg.items(), key=lambda x: x[1], reverse=True)


    # stud_avg = {} # 학생별 평균값 딕셔너리

    # for student, scores in student_scores.items(): #학생(키)과 점수(값)를 분리 및 순회
    #     total = 0
    #     for score in scores:
    #         total += int(score)

    #     stud_avg[student] = round(total / len(scores), 2)

    # return sorted(stud_avg.items(), key=lambda x: x[1], reverse=True) 
    #     #sorted 정렬
    #     #key=lambda x: x[1] 튜플의 두 번째 원소로 정렬 / x[0]은 첫 번째 
    #     #reverce 내림차순

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")
