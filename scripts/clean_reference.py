import sys

CONVERT_BOOK = {
    ' Luke': 'Luke',
    '1 Kings': 'I Kings',
    '1 Samuel': 'I Samuel',
    '2 Kings': 'II Kings',
    '2 Samuel': 'II Samuel',
    '3 John': 'III John',
    'Acts ': 'Acts',
    'Amos ': 'Amos',
    'COlossains': 'Colossians',
    'Colossains': 'Colossians',
    'Deutoronomy': 'Deuteronomy',
    'Ezekiel ': 'Ezekiel',
    'Hebrews ': 'Hebrews',
    'I  Kings': 'I Kings',
    'I Corinitians': 'I Corinithians',
    'I John ': 'I John',
    'I Sammuel': 'I Samuel',
    'I Samuel ': 'I Samuel',
    'II Chronicales ': 'II Chronicles',
    'II Corithians': 'II Corinthians',
    'II KIngs': 'II Kings',
    'John ': 'John',
    'Leviticus ': 'Leviticus',
    'Malachi ': 'Malachi',
    'Mark ': 'Mark',
    'Phillipians': 'Philippians',
    'Phillippians': 'Philippians',
    'Psalm': 'Psalm',
    'Psalms': 'Psalm',
    'Revelation ': 'Revelation',
    'Ruth ': 'Ruth'
}


def main(input_file: str) -> None:
	with open(input_file, 'r') as input:
		lines = input.readlines()
	
	out_lines = [lines[0]]
	for line in lines[1:]:
		parts = line.split("\t")
		reference = parts[11]
		pieces = reference.split(" ")
		book_raw = " ".join(pieces[0:-1])
		if book_raw in CONVERT_BOOK:
			parts[11] = reference.replace(book_raw, CONVERT_BOOK[book_raw])
		out_lines.append("\t".join(parts))
		
	print("".join(out_lines))


if __name__ == "__main__":
	main(sys.argv[1])