from lecturelists import *

''' 
Warning! 
The following keyboard texts must be identical with shaynman.py's RegexHandler-thing.
'''
keyboard_main = [
	['새로운 구독 설정'],
	['내 구독 리스트','구독 취소'],
	['이제 볼 일을 다 봤어요!'],
	['봇 정보, 만든이']
]
keyboard_generate = [
	['강의게시판'],
	['학부공지사항'],
	['이전으로']
]
keyboard_semester = [
	['1학기','여름학기','2학기'],
	['이전으로','처음으로']
]
keyboard_grade = [
	['1학년','2학년'],
	['3학년','4학년'],
	['석사/박사과정'],
	['처음으로']
]

keyboard_under_1_1 = sorted([[x] for x in lecturelist_under_1_1.keys()])
keyboard_under_1_2 = sorted([[x] for x in lecturelist_under_1_2.keys()])
keyboard_under_1_3 = sorted([[x] for x in lecturelist_under_1_3.keys()])
keyboard_under_1_4 = sorted([[x] for x in lecturelist_under_1_4.keys()])
keyboard_under_2_1 = sorted([[x] for x in lecturelist_under_2_1.keys()])
keyboard_under_2_2 = sorted([[x] for x in lecturelist_under_2_2.keys()])
keyboard_under_2_3 = sorted([[x] for x in lecturelist_under_2_3.keys()])
keyboard_under_2_4 = sorted([[x] for x in lecturelist_under_2_4.keys()])
keyboard_grad_1 = sorted([[x] for x in lecturelist_grad_1.keys()])
keyboard_grad_2 = sorted([[x] for x in lecturelist_grad_2.keys()])
keyboard_under_s = sorted([[x] for x in lecturelist_under_s.keys()])
