# In built string methods - single program
s = "  kodNest Technologies 123  "
print("Original String:", s)

#Case conversation methods
print("upper() :", s.upper()) # KODNEST TECHNOLOGIES 123
print("lower() :", s.lower()) #   
print("capitalize() :", s.capitalize()) #  
print("title() :", s.title()) #  
print("swapcase() :", s.swapcase()) #

#searching and counting
print("find('Tech') :", s.find("Tech")) # 
print("count('o') :", s.count("o")) #

#replace
print("replace('123', '2025') :", s.replace("123", "2025"))

#start and check
print("startswith('  kod') :", s.startswith("  kod")) #
print("endswith('123  ') :", s.endswith("123  ")) #

#split and join
print("split() :", s.split()) #
print("join() :", "-".join(s.split())) # 

#strip spaces
print("strip() :", s.strip()) #
print("lstrip() :", s.lstrip())# 
print("rstrip() :", s.rstrip())# 

#checking methods
print("isalpha() :", s.isalpha())#
print("isdigit() :", s.isdigit())#
print("isalnum() :", s.isalnum())#

#length of string
print("Length of string:" , len(s)) 