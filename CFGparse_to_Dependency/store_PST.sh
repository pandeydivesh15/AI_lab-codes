#!/bin/sh
cd ~/githubData/AI_lab-codes/Stanford_Parser/stanford-parser-full-2016-10-31/
java -mx150m -cp stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser \
-outputFormat "penn" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz \
../../CFGparse_to_Dependency/sample.txt > ../../CFGparse_to_Dependency/PST.txt