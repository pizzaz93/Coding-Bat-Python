"""

Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

"""
def end_other(a, b):
  if len(a) > len(b):
    c = a.lower()
    d = b.lower()
    e = c[len(c) - len(b):len(c)]
    if e == d:
      return True
  else:
    c = a.lower()
    d = b.lower()
    e = d[len(d) - len(c):len(d)]
    if e == c:
      return True
  return False
