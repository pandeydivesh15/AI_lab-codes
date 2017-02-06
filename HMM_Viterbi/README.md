# HMM and Viterbi's Algorithm 

The concept of Hidden Markov Model(HMM) is helpful in determining POS tags for some sentence. The algorithm used for HMM based tagging is [Viterbi's Algorithm](https://en.wikipedia.org/wiki/Viterbi_algorithm).

## Getting Started

### Prerequisites

Same as the first lab's assignment. We will be using the same training data that we used in first lab. I have included it here.

### Running on your system

  Type following commands on your Python terminal/Jupyter Ipython notebook:
   
  ```
  >>>from hmm_model import Hmm_model

  >>>h = Hmm_model("train.txt")

  >>>h.train()

  >>>h.tag_sentence("preacher near the mosque killed the terrorist man living next to Syrian border in Baghdad .")
  
  ```


