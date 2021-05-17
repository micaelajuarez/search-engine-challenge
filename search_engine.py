# TODO: add main comment here

import os.path
import re


def add_to_dictionary(words_paths, word, absolute_path):
	# TODO: implement this
	pass


def index_word_path(root, filename, words_paths):
	absolute_path = os.path.join(root, filename)

	# validate extension (file is textfile) and input path != this project path
	if filename.endswith((".txt", ".csv")) and filename != os.path.basename(__file__):
		with open(absolute_path) as textfile:
			for line in textfile:
				# assuming textfile is in English
				for word in [i for i in re.split(" ", re.sub(r"[^a-zA-Z ]", "", line.lower())) if i]:
					# TODO: clean up previous line for readability
					print(word + " ")
					# words_paths.update(add_to_dictionary(words_paths, word, absolute_path))

	return words_paths


def main(path):
	# TODO: validate empty input, raise exception?
	print("Indexing files...")

	file_count = 0
	words_paths = {}  # TODO: replace with oop alternative?

	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			words_paths.update(index_word_path(root, filename, words_paths))
			file_count += 1

	print("Done! {} files indexed.".format(file_count))

# TODO: get input text to search
