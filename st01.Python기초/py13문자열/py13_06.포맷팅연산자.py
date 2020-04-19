
# 포매팅 연산자( %) 에 사용 가능한 기호들에 대해 알아본다.
#
# 포맷 문자열	설명
# %s	문자열 혹은 임의의 객체를 문자열로 변환한다. (str() 함수를 이용한다.)
# %d	10진 정수
# %i	정수(%d와의 차이가 없다)
# %r	문자열 혹은 임의의 객체를 문자열로 변환한다. (repr() 함수를 이용한다.)
# %c	길이 1의 문자'%c', %'A'
# %u	부호 없는 정수'%u' %-12의 결과는'4294967284'양수는 그대로, 음수는 양수적 해석을 적용한다
# %o	8진수'%o' % 12 의 결과는'14'
# %x	16진수'%x' %12의 결과는'c'
# %X	16진수 대문자'%X' %12의 결과는'C'
# %e	부동 소수점(실수)을 지수 형태로 표현. 유효 숫자는 7자리로 표현한다.'%e' %123.45678 결과는'1.234568e+002'
# %E	%e와 동일하다. 단, 지수 표현을 대문자 E로 한다.
# %f	부동 소수점(실수)을 표현'%f' % 123.45678 결과는'123.456780'
# %g	부동 소수점을 편의에 따라서 소수점 형식 혹은 지수 형식으로 변환한다. 6자리의 유효 숫자로 표현한다.
# %G	%g와 같다. 단, 지수 표현을 대문자 E로 한다.


#################
# 문자열 포매팅
"I eat %d apples." % 3
'I eat 3 apples.'

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
# 'I ate 10 apples. so I was sick for three days.'


#################
# 정렬과 공백
"%10s" % "hi" #'          hi'
"%-10sjane." % "hi" #'hi          jane'
#################
# 소수점 표현
"%0.4f" % 0.3421342534
"%10.4f" % 0.3421342534

###############
#문자 앞에 0을 채우기 : %05d"

print( "%05d" %5) #00005
print( "%05d" %5) #00005


#################
# 문자 앞에 0을 채우기
# %05d"
# stirng.zfill(width)
# string.rjust(width[, fillchar])
