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

	def get_size(self):
		return len(self.words)


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

	def get(self):
		return {word: self.paths_per_word.get(word).get() for word in self.paths_per_word.keys()}

	def get_matches(self, words):
		return {word: self.paths_per_word.get(word).get() for word in words.get() if self.paths_per_word.get(word)}


class Ranker:
	PERCENTAGE = 100

	def __init__(self):
		self.ranking = {}

	def get_rank(self, index, paths, words):
		matches = index.get_matches(words)
		transposed = transpose(paths, matches)
		self.ranking = {key: (len(value) * self.PERCENTAGE / words.get_size()) for key, value in transposed.items()}
		return self.ranking


def transpose(keys, original):  # TODO: optimize :(
	transposed = {key: [] for key in keys}

	for og_key, og_values in original.items():
		for og_value in og_values:
			transposed[og_value].append(og_key)

	return transposed


def parse_textfile(absolute_path, filename, base_index):
	paths = Paths()
	paths.add_path(absolute_path)

	# validate extension (file is textfile) and input path matching this project's path
	if not filename.endswith((".txt", ".csv")) or filename == os.path.basename(__file__):
		pass  # handling?

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


def main(path, input_text):  # delete input_text argument
	if not path:
		print("Missing path argument!")
		return

	base_index = Index()
	all_paths = Paths()
	ranker = Ranker()

	explore_directories(path, base_index, all_paths)
	ranker.get_rank(base_index, all_paths.get(), Words(input_text))

	# print(ranker.get_rank(base_index, all_paths.get(), Words(input_text)))
	# TODO: get input_text from terminal instead of argument
