from pathlib import Path
FILENAME = "RNU6_269P.txt"
text = Path(FILENAME).read_text()
lines = text.split("\n")
print(lines[0])