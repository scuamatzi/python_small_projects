# generate numbers to print both sides of a book
def generate_numbers(total_pages):
    pages = []
    impares = list(range(1, total_pages + 1, 2))
    pares = list(range(2, total_pages + 1, 2))

    for idx in range(0, int(total_pages / 2) + 1, 5):
        pages.append(impares[idx : idx + 5])
        pages.append(pares[idx : idx + 5])

    return pages


if __name__ == "__main__":
    total_pages = int(input("Number of pages: "))
    pages = generate_numbers(total_pages)
    for idx in range(len(pages)):
        print(",".join([str(num) for num in pages[idx]]))
