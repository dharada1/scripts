# $ echo "hoge\nhoge" | python fileecho.py
# hoge
# hoge

import sys

def main():
	index = 0
	for line in iter(sys.stdin.readline, ""):
		print(line.rstrip("\n"))
		index += 1

if __name__ == '__main__':
	main()
