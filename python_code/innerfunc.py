# "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
#
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때
# 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

# str_given = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
#
# result = list(map(lambda x: 4 if x == 'A' else 3 if x == 'B' else 2 if x == 'C' else 1, str_given))
#
# print(sum(result))
#


# ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# filter_result = list(filter(lambda x: x if x % 2 == 0 else False, ten))
#
# print(filter_result)

#
# dict_test = dict(a=0, b=1, c=2, d=3, e=4, f=5)
#
# for k, v in dict_test.items():
#     print(f"{k}: {v}")


def mul(*x):
    result = 1
    for i in range(len(x)):
        if type(x[i]) is not int:
            return "에러발생"
        else:
            result *= x[i]
    return result


ret_val = mul(1, 2, '3', 4)
print(ret_val)