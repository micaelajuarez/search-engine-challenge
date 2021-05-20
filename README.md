# Search-engine code challenge
Command-line-driven text search engine made for a code challenge.

## Pre-requisites
This program requires installation of Python 3.8+. 
It should only be used to search .txt files written in English characters.

## Usage
To run this program, a valid absolute path is needed as an argument, as per the next example:
````
python3 ./search_engine.py "/home/someuser/somefolder/search-engine-challenge/test/textfiles"
````

To use the search function, simply follow the program's instructions:
````
Please enter any text to search, or an empty input to quit
````

## Example 
Here is an example of the search-engine's normal behaviour:
````
Indexing files...
Done! 6 files indexed.
Please enter any text to search, or an empty input to quit: this is some example text
...t/textfiles/textfile4.txt: 60%
...e_textfiles/textfile3.txt: 60%
...e_textfiles/textfile2.txt: 60%
...st/textfiles/dynamite.txt: 40%
...t/textfiles/textfile5.txt: 20%
...t/textfiles/textfile1.txt: 0%
Please enter any text to search, or an empty input to quit: 
````