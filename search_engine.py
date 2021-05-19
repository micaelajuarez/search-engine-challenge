# TODO: add main comment here
import os.path
import re


class Words:
	REGEX = r"[^a-zA-Z ]"

	def __init__(self, text):
		self.words = self.get_words_from(text)

	def get_words_from(self, text):
		# TODO: clean up for readability?
		return [i for i in re.split(" ", re.sub(self.REGEX, "", text.lower())) if i]

	def get(self):
		return self.words


class Paths:
	def __init__(self):
		self.paths = []

	def add_path(self, path):
		self.paths.append(path)


class Index:
	def __init__(self):
		self.paths_per_word = {}

	def add(self, words, paths):
		# TODO: fix this! When trying to insert a duplicate key, new Paths obj replaces previous Paths obj...
		# TODO: ...but instead, they should combine (how?)

		aux_dict = {k: paths for k in words.get()}
		self.paths_per_word.update(aux_dict)


def parse_textfile(root, filename, base_index):
	absolute_path = os.path.join(root, filename)
	paths = Paths()
	paths.add_path(absolute_path)

	# validate extension (file is textfile) and input path matching this project's path
	if not filename.endswith((".txt", ".csv")) or filename == os.path.basename(__file__):
		pass  # handling?

	# assuming textfile is in English
	with open(absolute_path) as textfile:
		for line in textfile:
			base_index.add(Words(line), paths)

	# return base_index?


def explore_directories(path):
	print("Indexing files...")
	file_count = 0
	base_index = Index()

	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			parse_textfile(root, filename, base_index)
			file_count += 1

	print("Done! {} files indexed.".format(file_count))
	return base_index


def main(path, input_text):
	# TODO: validate empty path: raise exception? quit?
	base_index = explore_directories(path)
	# TODO: get input_text from terminal instead of argument
