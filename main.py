# Create list
List = list()
List = []
List = [0, "any data type can be added to list", 25.12,
        ("Even tuples"), {"Dictionaries": "can also be added"},
       ["can", "be nested"]]
# Accessing items

List[1]		# 0
List[-1] 	# ["can", "be nested"]

# Operations
List.append(4)		# adds 4 to end
List.pop(n=-1)		# removes element from nth position
List.count(25.12)	# 1