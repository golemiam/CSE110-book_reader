
def main():
    book_reader("books.txt")

def book_reader(in_file):
    with open(in_file, "r") as in_file:
        for line in in_file:
            clean_line = line.strip()
            print(clean_line)
        

if __name__ == '__main__':
    main()
