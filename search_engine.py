# TODO: add main comment here
import os.path
import re
import sys


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
	MAX_MATCHES = 10
	FORMAT = 25

	def __init__(self):
		self.ranking = {}

	def rank(self, index, paths, words):
		words_per_path = transpose(paths, index.get_matches(words))
		self.calculate(words_per_path, words.get_size())
		return self.get_ranking()

	def calculate(self, words_per_path, word_count):
		full_ranking = {key: (len(value) * self.PERCENTAGE / word_count) for key, value in words_per_path.items()}
		self.ranking = dict(sorted(full_ranking.items(), key=lambda x: x[1], reverse=True)[:self.MAX_MATCHES])

	def get_ranking(self):
		return self.ranking

	def print(self):
		for path, rank in self.ranking.items():
			print("..." + path[len(path) - self.FORMAT:] + ": " + str(int(rank)) + "%\n")


def transpose(keys, original):
	transposed = {key: [] for key in keys}

	for og_key, og_values in original.items():
		for og_value in og_values:
			transposed[og_value].append(og_key)

	return transposed


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
