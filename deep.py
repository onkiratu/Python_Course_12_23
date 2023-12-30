# deep.py

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.strip() == "42" or answer.strip().lower() in ["forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
     main()
