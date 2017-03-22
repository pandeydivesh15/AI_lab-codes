# Using Stanford Parser: PCFG and Dependency Parsing

Here I list down some commands, which may prove helpful in achieving parsing.

## Prerequisites

For running these commands, first make sure that you have downloaded Stanford Parser module from [this site](http://nlp.stanford.edu/software/lex-parser.shtml). Extract this module into this directory. 

## Running on your system

First change your current directory to Stanford Parser directory. Then start executing these commands.

1. For running Probabilistic Context-Free Grammar (PCFG) model:

	```
	java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "wordsAndTags,penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ../sample.txt
	```

2. To use the lexicalized parser, replace englishPCFG.ser.gz with englishFactored.ser.gz in the lexparser.sh script and use the flag -mx600m to give more memory to java.

	```
	java -mx600m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "wordsAndTags,penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishFactored.ser.gz ../sample.txt
	```

3. For parsing from stdin to stdout:

	```
	java -mx600m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -sentences newline -outputFormat "wordsAndTags,penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishFactored.ser.gz -
	```

4. For training your own model:
	
	i. Train and store model:
	```
	java -mx1500m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -train ../treebanks/PennTreebank/ 0-198 -saveToSerializedFile serializedGrammarFilename
	```

	ii. Run stored model on input coming from stdin.
	```
	java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -sentences newline -outputFormat "wordsAndTags,penn,typedDependencies" serializedGrammarFilename -
	```

	iii. Test your model on test data.
	```
	java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -loadFromSerializedFile serializedGrammarFilename -testTreebank ../treebanks/PennTreebank/ 0-1
	```

	iv. Train and test model. Model not saved.
	```
	java -mx1500m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -train ../treebanks/PennTreebank/ 0-198 -testTreebank ../treebanks/PennTreebank/ 199-200
	```


5. Get the typed dependencies (grammatical relations) output from the trees produced by another parser.

	```
	java -cp stanford-parser.jar edu.stanford.nlp.trees.EnglishGrammaticalStructure -treeFile ../treebanks/PennTreebank/wsj_0090.mrg
	```

6. Obtaining multiple (n) parse trees for a single input sentence with their log probabilities to compare. Only applicable using the PCFG parser. Option used '-printPCFGkBest n'

	```
	java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" -printPCFGkBest 4 edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ../sample.txt
	```

7. Get original Stanford Dependencies instead of Universal Dependencies. Add '-originalDependencies' option in your command. 
Note: Universal Dependencies were developed with the goal of being across-linguistically valid representation.

8. Storing PCFG grammar(from PCFG model) in a text file.

	```
	java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -loadFromSerializedFile edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz -saveToTextFile englishPCFG.txt
	```

9. To use the neural net dependency parser, issue the following command:
	
	```
	java -Xmx2g -cp stanford-parser.jar edu.stanford.nlp.parser.nndep.DependencyParser -model edu/stanford/nlp/models/parser/nndep/english_UD.gz -textFile data/english-onesent.txt -outFile data/english-onesent.txt.out
	```