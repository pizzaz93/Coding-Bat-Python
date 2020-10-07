"""

Return True if the given string contains an appearance of "xyz" where the
xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

"""

def xyz_there(str):
  if str[0:3]  == "xyz":
    return True  
  for x in range(len(str)):
    if str[x:x + 1] != "." and str[x + 1:x + 2] == "x" and str[x + 2:x + 3] == "y" and str[x + 3:x + 4] == "z":
      return True
  return False
