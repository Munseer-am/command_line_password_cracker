import hashlib
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("--hash", help="put md5 hash after adding -hash")
parse.add_argument("--file", help="Input filename")

args = parse.parse_args()

file_name = args.file
h = args.hash

try:
    with open(file_name, "rb") as f:
        str = f.read()
        for word in str.split():
            s = word.decode()
            enc = hashlib.md5(word).hexdigest()
            if enc == h:
                print("Password found")
                print(f"Password for {h} is: {s}")
                quit()
            else:
                print(f"Password not found {s}")

except FileNotFoundError:
    print("FileNotFoundError")
