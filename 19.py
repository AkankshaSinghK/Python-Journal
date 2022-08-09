# program to count total number of upper and lower case letters in a file
def count_char_type(file_name):
  lines = []
  uppercase = []
  lowercase = []
  total = []
  with open(file_name) as f:
    lines = f.readlines()
  for line in lines:
    uppercase.append(sum(1 for c in line if c.isupper()))
    lowercase.append(sum(1 for c in line if c.islower()))
    total.append(sum(1 for c in line))

  return (sum(uppercase), sum(lowercase), sum(total))


if __name__ == "__main__":
  # input file: testfile.txt
  # has 5 uppercase characters
  # has 18 lowercase characters
  # has 4 whitespaces
  # has 28 total characters
  (upper, lower, total) = count_char_type("testfile.txt")

  print(f"Total number of uppercase characters: {upper}")
  print(f"Total number of uppercase characters: {lower}")
  print(f"Total number of characters: {total}")
