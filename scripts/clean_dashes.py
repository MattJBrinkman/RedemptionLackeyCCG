import sys


def main(input_file: str, output_file: str) -> None:

	print(f"input={input_file}")
	with open(input_file, 'r') as input:
		lines = input.readlines()
	
	types = {}
	outlines = []
	for line in lines:
		parts = line.split("\t")
		if parts[5] == "-":
			parts[5] = ""
		if parts[6] == "-":
			parts[6] = ""
		if parts[7] == "-":
			parts[7] = ""
		if parts[8] == "-":
			parts[8] = ""
		if parts[9] == "-":
			parts[9] = ""
		if parts[12] == "-":
			parts[12] = ""
		outlines.append("\t".join(parts))

	with open(output_file, "w") as output:
		print("".join(outlines), file=output)


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])