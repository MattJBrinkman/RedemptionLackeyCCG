import sys


def main(input_file: str) -> None:
	print(f"input={input_file}")
	with open(input_file, 'r') as input:
		lines = input.readlines()
	
	types = {}
	for line in lines[1:]:
		parts = line.split("\t")
		type_name = parts[3]
		if type_name not in types:
			types[type_name] = type_name
	
	type_list = sorted(types)
	out_lines = ["convert_types = {"]
	for type_name in type_list:
		out_lines.append(f"    {type_name}: {type_name}")
	out_lines.append("}")
	print("\n".join(out_lines))


if __name__ == "__main__":
	main(sys.argv[1])