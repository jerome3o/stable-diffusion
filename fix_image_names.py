import sys
from pathlib import Path
from shutil import move


def main(folder: str):
    folder = Path(folder)
    for f in folder.glob("*.png"):
        move(str(f), str(f.parent / f"image_{int(f.stem[6:]):05d}.png"))
        # print(str(f.parent / f"image_{int(f.stem[6:]):05d}.png"))



if __name__ == "__main__":
    folder = sys.argv[1]
    main(folder)  
