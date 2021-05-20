import search_engine as se
import unittest

import search_engine_classes as sec

TEST_PATH = "/home/micaelita/PycharmProjects/search-engine-challenge/test/textfiles/more_textfiles/"
INPUT_TEXT = "This is an uninteresting piece of input text"

# Integration tests


class TestSearchEngine(unittest.TestCase):
	def test_get_correct_dictionary_with_matching_words_from_input_and_their_respective_paths(self):
		path_list = [TEST_PATH + "textfile3.txt", TEST_PATH + "textfile2.txt"]
		dictionary = {"this": path_list, "is": path_list, "of": [path_list[0]], "text": path_list}
		base_index = sec.Index()
		paths = sec.Paths()
		
		paths.add_path(path_list[0])
		paths.add_path(path_list[1])
		se.explore_directories(TEST_PATH, base_index, paths)

		self.assertEqual(base_index.get_matches(sec.Words(INPUT_TEXT)), dictionary)

	def test_get_correct_dictionary_ranking(self):
		path_list = [TEST_PATH + "textfile3.txt", TEST_PATH + "textfile2.txt"]
		dictionary = {path_list[0]: 50.0, path_list[1]: 37.5}
		base_index = sec.Index()
		paths = sec.Paths()
		ranker = sec.Ranker()

		paths.add_path(path_list[0])
		paths.add_path(path_list[1])
		se.explore_directories(TEST_PATH, base_index, paths)
		ranker.rank(base_index, paths.get(), sec.Words(INPUT_TEXT))

		self.assertEqual(ranker.get_ranking(), dictionary)


if __name__ == '__main__':
	unittest.main()
