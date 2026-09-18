def NULL_not_found(object: any) -> int:
	if (object is str("")):
		print("Empty:", object.__class__);
	elif (object != object): #Nan is not equal to itself
		print("Cheese:", object, object.__class__);
	elif (object is bool(False)):
		print("Fake:", object, object.__class__);
	elif (object is int()):
		print("Zero:", object, object.__class__);
	elif (object is None):
		print("Nothing:", object, object.__class__);
	else:
		print("Type not Found")
		return 1
	return 0
