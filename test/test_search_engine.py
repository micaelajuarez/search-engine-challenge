import search_engine as se
import unittest

TEST_PATH = "/home/micaelita/PycharmProjects/search-engine-challenge/test/textfiles/more_textfiles/"

# Integration tests


class TestSearchEngine(unittest.TestCase):
	def test_get_correct_dictionary_with_matching_words_from_input_and_their_respective_paths(self):
		path_list = [TEST_PATH + "textfile3.txt", TEST_PATH + "textfile2.txt"]
		input_text = "This is an uninteresting piece of input text"
		dictionary = {"this": path_list, "is": path_list, "of": [path_list[0]], "text": path_list}

		base_index = se.explore_directories(TEST_PATH)
		index_result = base_index.get_subindex_with_words(se.Words(input_text))

		self.assertEqual(index_result.get_as_dictionary(), dictionary)


if __name__ == '__main__':
	unittest.main()
