#coding:utf-8
from rouge import Rouge
a = ["the group included four children , turkish official says<q>turkish military did n't say what group 's intent was<q>uk foreign office says it is trying to get information from turkish officials"]  # Ԥ��ժҪ ���������б�Ҳ�����Ǿ��ӣ�
b = ["the nine were arrested at the turkey-syria border , the turkish military says<q>it did n't say why the group allegedly was trying to get into Syria"] #��ʵժҪ
 
'''
f:F1ֵ  p����׼��  R���ٻ���
'''
rouge = Rouge()
rouge_score = rouge.get_scores(a, b)
print(rouge_score[0]["rouge-1"])
print(rouge_score[0]["rouge-2"])
print(rouge_score[0]["rouge-l"])
