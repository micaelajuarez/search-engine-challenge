import search_engine as se
import unittest

import search_engine_classes

TEST_PATH = "/home/micaelita/PycharmProjects/search-engine-challenge/test/textfiles/more_textfiles/"

# Integration tests


class TestSearchEngine(unittest.TestCase):
	def test_get_correct_dictionary_with_matching_words_from_input_and_their_respective_paths(self):
		path_list = [TEST_PATH + "textfile3.txt", TEST_PATH + "textfile2.txt"]
		input_text = "This is an uninteresting piece of input text"
		dictionary = {"this": path_list, "is": path_list, "of": [path_list[0]], "text": path_list}
		base_index = search_engine_classes.Index()
		paths = search_engine_classes.Paths()
		paths.add_path(path_list[0])
		paths.add_path(path_list[1])
		se.explore_directories(TEST_PATH, base_index, paths)

		self.assertEqual(base_index.get_matches(search_engine_classes.Words(input_text)), dictionary)


if __name__ == '__main__':
	unittest.main()
