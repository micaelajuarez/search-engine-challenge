# TODO: add main comment here
import os.path
import sys

from search_engine_classes import Words, Paths, Index, Ranker


def parse_textfile(absolute_path, filename, base_index):
	paths = Paths()
	paths.add_path(absolute_path)

	if not filename.endswith(".txt"):
		raise ValueError("Invalid file {}!".format(filename))

	# assuming textfile is in English
	with open(absolute_path) as textfile:
		for line in textfile:
			base_index.add(Words(line), paths)


def explore_directories(path, base_index, all_paths):
	print("Indexing files...")
	file_count = 0

	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			absolute_path = os.path.join(root, filename)
			parse_textfile(absolute_path, filename, base_index)
			all_paths.add_path(absolute_path)
			file_count += 1

	print("Done! {} files indexed.".format(file_count))
	return base_index


def main(argv):
	if len(argv) <= 1:
		raise ValueError("Missing path argument!")

	base_index = Index()
	all_paths = Paths()
	ranker = Ranker()

	explore_directories(argv[1], base_index, all_paths)
	input_text = input("Please enter any text to search, or an empty input to quit: ")

	while input_text:
		ranker.rank(base_index, all_paths.get(), Words(input_text))
		ranker.print()
		input_text = input("Please enter any text to search, or an empty input to quit: ")


if __name__ == "__main__":
	main(sys.argv)
