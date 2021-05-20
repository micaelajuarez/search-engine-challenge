# TODO: add main comment here
import os.path
import re


class Words:
	REGEX = r"[^a-zA-Z ]"  # no letters nor spaces

	def __init__(self, text):
		self.words = self.get_words_from(text)

	def get_words_from(self, text):
		formatted_text = re.sub(self.REGEX, "", text.lower())
		return [i for i in re.split(" ", formatted_text) if i]

	def get(self):
		return self.words


class Paths:
	def __init__(self):
		self.paths = []

	def add_path(self, path):
		self.paths.append(path)

	def add_paths(self, paths):
		self.paths.extend([i for i in paths.get() if i not in self.paths])

	def get(self):
		return self.paths

	def merge(self, paths):
		self.add_paths(paths)
		return self


class Index:
	def __init__(self):
		self.paths_per_word = {}  # {string:Paths}

	def add(self, words, paths):
		for word in words.get():
			self.paths_per_word.setdefault(word, Paths()).merge(paths)

	def get_as_dictionary(self):
		return {word: self.paths_per_word.get(word).get() for word in self.paths_per_word.keys()}

	def print(self):
		for word, paths in self.paths_per_word.items():
			print(word, paths.get())

	def create_from(self, dictionary):
		self.paths_per_word = dictionary
		return self

	def get_subindex_with_words(self, words):
		aux_dictionary = {word: self.paths_per_word.get(word) for word in words.get() if self.paths_per_word.get(word)}
		return Index().create_from(aux_dictionary)

# -------------------------------------------------------------------------------------------------------------


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


def main(path, input_text):  # remove input_text argument
	if not path:
		print("Missing path argument!")
		return

	base_index = explore_directories(path)
	index_result = base_index.get_subindex_with_words(Words(input_text))
	# TODO: get input_text from terminal instead of argument
