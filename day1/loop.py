
names = ['brian','janet','james','jessica','john','julie','jennifer','jason','joseph','jane']

# for name in names:
    # print(name, ' has %s' % len(name), ' characters')
    
# Collections (List, tuple, set, dictionary)
# List: [] is an ordered collection mutable of items
# Tuple: () is an ordered collection immutable of items
# Set: {} is an unordered collection of unique items
# Dictionary: {} is an unordered collection of key-value pairs

# dictionary

# clubs = {'Manchester United': 'Old Trafford', 'Chelsea': 'Stamford Bridge', 'Arsenal': 'Emirates Stadium', 'Liverpool': 'Anfield', 'Manchester City': 'Etihad Stadium'}

# for club, stadium in clubs.items():
    # print(club, ' plays at ', stadium)
    

loan_status = {'Completed': 3, 'Current': 2, 'Late': 3, 'Default': 23}

for status in loan_status.copy().items():
    if status[1] > 2:
        print('Make more loan applications')
    else:
        print('Make more repayment  efforts')