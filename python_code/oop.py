#
# class Korean:
#     def __init__(self, country):
#         self.__country = country
#
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, country):
#         if country is not str:
#             return print("this is not valid value")
#         else:
#             self.__country = country
#
#     def __del__(self):
#         pass
#
#     def printNationality(self):
#         print(self.__country)
#
#
# con1 = Korean("대한민국")
#
# con1.printNationality()
# con1.printNationality()


# class Student:
#     def __init__(self,kor,eng,math):
#         self.kor =kor
#         self.eng = eng
#         self.math = math
#
#     def score(self):
#         return print(f"국어, 영어, 수학의 총점: {self.kor + self.eng + self.math}")
#
#
# kor, eng, math = map(int, input().split(','))
# grade = Student(kor, eng, math)
#
# grade.score()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"원의 면적: {self.radius * self.radius * 3.14}")

# 이것은 브런치


area = Circle(2)

area.area()

# T = int(input())
#
# for num in range(1, T +1):
#     list_num = str(num)
#     cnt = list_num.count('3') + list_num.count('6') + list_num.count('9')
#     if cnt:
#         print("-"*cnt, end=" ")
#     else:
#         print(num, end=" ")
