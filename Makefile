default:
	make build
	make minesweeper
	make clean
all:
	make build >> output.txt
	make decompress > output.txt
	make dup >> output.txt
	make fizzbuzz >> output.txt
	make map >> output.txt
	make minesweeper >> output.txt
build:
	echo Building...
	make build_minesweeper
decompress:
	python decompress.py
dup:
	dup_remove.py
fizzbuzz:
	fizzbuzz.py
map:
	map.py
build_minesweeper:
	g++ minesweeper.cpp -o minesweeper.out
minesweeper:
	./minesweeper.out
clean:
	rm *.out
