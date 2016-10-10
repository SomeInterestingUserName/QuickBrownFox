# QuickBrownFox
A simple test to check if a string contains all the letters in the alphabet. Named after the sentence that would satisfy this test, "The quick brown fox jumped over the lazy dog." Also trying to test out/familiarize myself with GitHub's features.

# Usage
The **Qu**ick**Br**own**F**o**x**, or QuBrFx test, is performed by calling
```python
QuBrFx("String")

False
```
where `"String"` is the sequence under test. Test returns `True` if string contains at least one instance of each character in the character set, case insensitive. Test returns `False` otherwise. Default character set is `abcdefghijklmnopqrstuvwxyz`. Testing with custom character sets can be performed by passing the `charset` argument with a string consisting of all characters in the character set:
```python
QuBrFx("This Sentence is False", charset="abc")

False

```
# Examples

```python
QuBrFx("The quick brown fox jumped over the lazy dog.")

True


QuBrFx("This sentence contains the 17th letter.")

False


QuBrFx("ABC", charset="abc")

True


QuBrFx("abc", charset="ABC")

True




```
