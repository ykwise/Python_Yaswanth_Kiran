#16.Create a file containing a paragraph. Use read() to count the total number of words.
file = open("file16.txt","w")
file.write("The library was quiet in the early morning, with only a few students sitting near the windows and reading their notes. Outside, the streets slowly became busy as shops opened and buses carried people to work. A cool breeze moved through the trees, making the leaves rustle softly. Inside, one student was preparing for an examination while another was working on a small Python project. Although the day had started peacefully, everyone seemed focused on finishing their tasks before evening.")
file.close()

file = open("file16.txt","r")
lines = file.read()
words = lines.split()
print(f"No.of.Words: {len(words)}")
file.close()

