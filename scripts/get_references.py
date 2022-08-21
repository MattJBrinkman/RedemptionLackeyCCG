import sys


def main(input_file: str) -> None:
	print(f"input={input_file}")
	with open(input_file, 'r') as input:
		lines = input.readlines()
	
	books = {}
	for line in lines[1:]:
		parts = line.split("\t")
		reference = parts[11]
		pieces = reference.split(" ")
		book_raw = " ".join(pieces[0:-1])
		book = f"'{book_raw}'"
		if book not in books:
			books[book] = book
	
	book_list = sorted(books)
	out_lines = ["convert_book = {"]
	for book in book_list:
		out_lines.append(f"    {book}: {book}")
	out_lines.append("}")
	print("\n".join(out_lines))


if __name__ == "__main__":
	main(sys.argv[1])