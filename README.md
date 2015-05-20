Source code for natural language processing with Python.

## Usage:

```bash
docker run -it contentdj/nltk
```

This will open a Python shell with access to `nltk` and the brown corpus. To test that the install has been successful:

```python
>>> import nltk
>>> from nltk.corpus import brown
>>> brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
```
