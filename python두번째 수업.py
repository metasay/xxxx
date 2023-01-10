# a = "Hello"
# b = "Python"
# c = a + " " + b
# print(c)
# print(a * 3)
# #문자열의 길이 == 문자의 개수
# print(len(a))

#
# #문자열 관련함수
# string = "Hello Python"
# #해당 문자열에서 내가 찾는 문자열이 몇개 있는지를 알려주는 함수 count
# #find(str) = 괄호안의 문자열이 몇번째 인덱스에서 가장 먼저 나오는지를 알려준다.
# #         단, 없는 문자열을 찾을경우 -1을 리턴한다.
# print(string.index('x'))

# # replace(old,new) = 해당 문자열에서 old문자를 new문자로 치환한 값을 리턴한다.
# string = "Hello python"
# print(string.replace('Hello','Bye'))
# print(string)
#
#
# strin = "Hello Python""
#
# print(string.upper())# 해당 문자를 대문자로 변환한 값을 리턴
# print(string.lower())# 해당 문자를 소문자로 변환한 값을 리턴
#
# print(string[0].isupper())
# print(string[0].islower())

# s = ""
#
# print(s.isdigit())# 숫자값이 들어있는 문자열 자료형일 경우  ture,아니면 false
# print(s.isalpha())# 영문자가 들어있는 문자열 자료형일 경우  ture,아니면 false
# print(s.isalnum())# 숫자값이 들어있는 문자열 자료형일 경우  ture,아니면 false + 영문자가 들어있는 문자열 자료형일 경우  ture,아니면 false

# string = "Hello Python"

# split(srt) = 해당 문자열을 기준으로 해당 문자열을 나누어준 값을 리턴한다.
#                             단, 괄호 안에 아무것도 넣지 안는경우 공백을 사용 한다.
# print(string.split(' '))
# print(string.split())

# string = "Hello Python"
#
# #'str'.join(string)
# print('/'.join(string))사이에 / 을 늠

# apple = "...ap.lpe....."
# print(apple.lstrip('.'))
# print(apple.strip('.'))
# print(apple.rstrip('.'))

# letters = 'python'
# print(letters[0], letters[2])

# license_plate = "24가 2210"
#
# print(license_plate[-4:])

# string = "홀짝홀짝홀짝"
#
# print(string[::2])#홀홀홀
# print(string[1::2])#짝짝짝

# string = "PYTHON"
# print(string[::-1])
#
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", " ")
# print(phone_number1)
#
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-",  "")
# print(phone_number1)
#
# url = "www.naver.com"
# print(url.split('.')[-1])

# lang = 'python'
# lang[0] = 'P'
# print(lang)

# string = "Hello"
# string = string.replace('H','D')
# print(string)
#
# string = 'abcdstring.replace('b', 'B')> print(

# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# name = "박찬빈"
# age = 30
# print("제 이름은 %s이고, 나이는 %d살입니다." %(name, age))

# format()
# name = "박찬빈"
# age = 30
# print("제 이름은 {}이고, 나이는 {}살입니다.".format(name,age))
# f-string
# name = "박찬빈"
# age = 30
# print(f"제 이름은 {name}이고, 나이는 {age}살입니다.")
