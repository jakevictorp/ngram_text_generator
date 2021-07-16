# ngram_text_generator

This tool uses a simple ngram model to train a language model based on a training text, and then generates random text based on the model.

The user should provide a desired text file (some examples are provided) to train on.

To run the generator, the user should run:

```
>>> python master.py -t [PATH TO TRAINING TEXT] -n [LENGTH OF N GRAM] -k [VALUE OF K FOR SMOOTHING] -l [LOG OR RAW PROBABILITIES] -g [LENGTH OF GENERATED TEXT]
```
