# 같은 폴더에 있는 class and function호출
# 1차적인 방법
# 1. inport : 같은 파일에 있을 경우 생략.
import classes_formats
# 2. class instance
person = classes_formats.Person()
arithmetics = classes_formats.Arithmetics()
Class_name = classes_formats.Class_name()
# 3. call function  
person.add_age()

## import 시 주로 사용하는 방식
from classes_formats import person, Arithmetics, Class_name
person_second = person()
arithmetics_second = Arithmetics()
pass