# Chunking 

Text chunking consists of dividing a text in syntactically correlated parts of words. Text chunking is an intermediate step towards full parsing. For more information about chunking, you may refer to these links: [1](http://www.nltk.org/book/ch07.html), [2](http://www.cnts.ua.ac.be/conll2000/chunking/)

## Getting Started

### Prerequisites

Same as the first lab's assignment. We will be using different data sets this time. I have included them here.

### Running on your system

1. Using CRF++:
  
  Type following commands on your terminal:
   
  ```
  crf_learn crf_template train.txt crf_model
  
  crf_test -m crf_model test.txt > chunking_result.txt
  
  python confusion_matrix_calc.py --crf++  
  
  ```
  
2. Using HunPos Tagger
  
  Type following commands on your terminal:
   
  ```
  
  python data_for_hunPos.py 
 
  hunpos-train mytagger < hunpos_train.txt
  
  hunpos-tag mytagger < hunpos_test.txt > chunking_result.txt
  
  python confusion_matrix_calc.py --hunpos  
  
  ```
NOTE: All txt files in the above code would be auto generated when you run the above commands.


