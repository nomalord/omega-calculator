from Operator import object_dict

pairOperator = object_dict['!']
pairOperator.right = 10000
print(pairOperator.operate())