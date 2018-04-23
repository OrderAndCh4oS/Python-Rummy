import sys

from rummy import Rummy as Play

def main():
    try:
        Play()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
