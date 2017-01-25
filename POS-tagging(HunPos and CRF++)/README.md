# Part of Speech tagging using HunPos tagger and CRF++

The process of assigning one of the parts of speech to the given word is called Parts Of Speech tagging. It is commonly referred to as POS tagging. Parts of speech include nouns, verbs, adverbs, adjectives, pronouns, conjunction and their sub-categories.

## Getting Started

### Prerequisites

First of all, you must have HunPos scripts and CRF++ present in your system. For HunPos, download this [zipped file](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/hunpos/hunpos-1.0-linux.tgz). And for CRF++ see [here](https://taku910.github.io/crfpp/#download).

Python requirements:
  * Numpy
  * sklearn
  * pandas

### Running on your system

1. HunPos Tagger
  
  Type following commands on your terminal:
   
  ```
  python data_cleaner.py
  
  python data_splitter.py --hunpos
  
  hunpos-train mytagger < en_train.txt
  
  hunpos-tag mytagger < en_test.txt > en_pos_result.txt
  
  python confusion_matrix_calc.py --hunpos  
  
  ```
  
2. CRF++ Tagger
  
  Type following commands on your terminal:
   
  ```
  python data_cleaner.py
  
  python data_splitter.py --crf++
  
  crf_learn crf_template en_train.txt crf_model
  
  crf_test -m crf_model en_test.txt > en_pos_result.txt
  
  python confusion_matrix_calc.py --crf++  
  
  ```
NOTE: All txt files in the above code would be auto generated when you run the above commands.


