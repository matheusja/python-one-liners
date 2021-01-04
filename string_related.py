
# 
# Add a "\t", or a prefix of your choice, to each line(separated by "\n" or other delimiter)
#

indent_lines = lambda (lines, prefix = '\t', separator = "\n"): seperator.join(map(lambda line : f"{prefix}{line}", lines.split(seperator)))

#
#def ident_lines(lines, prefix = '\t', seperator = '\n'):
#  string = ""
#  for line in lines.split('\n')
#      if string != "":
#         string += "\n"
#      string += prefix + line
#  return string


