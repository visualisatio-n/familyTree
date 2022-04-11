from model.female import Female
from model.male import Male

king_shan = Male('King Shan')
queen_anga = Female('Queen Anga')
king_shan.wife = queen_anga
queen_anga.husband = king_shan

family_tree = dict()
family_tree['King Shan'] = king_shan
family_tree['Queen Anga'] = queen_anga





