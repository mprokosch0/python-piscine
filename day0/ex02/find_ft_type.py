def all_thing_is_obj(object: any) -> int:
	if type(object) is str:
		print(f"{object}", "is in the kitchen :", object.__class__)
	elif type(object) in {list, tuple, dict, set}:
		print(type(object).__name__.capitalize(), ":", object.__class__)
	else:
		print("Type not found")

	return 42
