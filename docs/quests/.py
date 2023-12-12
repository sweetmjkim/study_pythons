def quest_round() :
    dict_question_mix = {}
    dict_question_mix["question"]=input("question :")
    dict_question_mix["answer"]=input("answer :")
    dict_question_mix["correct_index"]=input("correct_index :")
    dict_question_mix["score"]=input("score :")
    return dict_question_mix

list_question_mix=[]

for count in [1,2,3] :
    list_question_mix.append(quest_round())
print(list_question_mix)

