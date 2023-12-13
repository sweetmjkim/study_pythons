# 1단계 진행
# list_question_mix = []
# for x in range(1, 4):
#     list_input = {}
#     list_input["question"] = input("{}번째 문제 입력하시오.".format(x))
#     list_input["answer_1"] = input("{}번째 보기(1)를 입력하시오.".format(x))
#     list_input["answer_2"] = input("{}번째 보기(2)를 입력하시오.".format(x))
#     list_input["answer_3"] = input("{}번째 보기(3)를 입력하시오.".format(x))
#     list_input["answer_4"] = input("{}번째 보기(4)를 입력하시오.".format(x))
#     list_input["correct_index"] = input("{}번째 정답을 입력하시오.".format(x)) 
#     list_input["score"] = input("{}번째 점수를 입력하시오.".format(x))
#     list_question_mix.append(list_input)

# for total_list in list_question_mix :
#     question = total_list["question"]
#     answer_1 = total_list["answer_1"]
#     answer_2 = total_list["answer_2"]
#     answer_3 = total_list["answer_3"]
#     answer_4 = total_list["answer_4"]
#     correct_index = total_list["correct_index"]
#     score = total_list["score"]
#     print("문제: {}".format(question))
#     print("보기 1: {}".format(answer_1))
#     print("보기 2: {}".format(answer_2))
#     print("보기 3: {}".format(answer_3))
#     print("보기 4: {}".format(answer_4))
#     print("정답 : {}".format(correct_index))
#     print("점수 : {}".format(score))
#     print("----------" * 7)

# 2단계 진행
# def quest_round() :
#     dict_question_mix = {}
#     dict_question_mix["question"]=input("question :")
#     dict_question_mix["answer"]=input("answer :")
#     dict_question_mix["correct_index"]=input("correct_index :")
#     dict_question_mix["score"]=input("score :")
#     return dict_question_mix
# list_question_mix=[]
# for count in [1,2,3] :
#     list_question_mix.append(quest_round())
# print(list_question_mix)

# 3단계 진행(최종)
def quest_round() :
    dict_question_mix = {}
    dict_question_mix["문제"] = input("문제 :")

    # answer 딕셔너리를 생성
    answer_input = input("보기 (예시: 1.보기 ,2.보기,...) : ")
    answer_dict = dict(item.split(".") for item in answer_input.split(","))
    dict_question_mix["보기"] = answer_dict

    dict_question_mix["정답"] = input("정답 :")
    dict_question_mix["점수"] = input("점수 :")
    return dict_question_mix

list_question_mix = []
for count in [1,2,3] :
    list_question_mix.append(quest_round())
print(list_question_mix)