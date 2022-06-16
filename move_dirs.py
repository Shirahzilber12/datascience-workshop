import shutil
import os
from pathlib import Path
import time

emotions = ["anger", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

def main(path):
    path_dir = Path(path)
    
    print(f'Directory name is {path_dir.name }')
    print(path_dir)
    print(f'start at { time.localtime()}')

    print(f'list of sub-directories: {os.listdir(path)}')

    dirs = [e for e in path_dir.iterdir() if e.is_dir() and e.name not in emotions and e.name != "archive"]
    for dir in dirs:
        emotions_dir = [e for e in dir.iterdir() if e.is_dir()]
        for emotion in emotions_dir:
            print(f'emotion: {emotion}')
            move_dir(emotion)

    _files = [e for e in path_dir.iterdir() if e.name not in emotions and e.name != "archive"]
    archive = Path(path_dir / "archive")
    archive.mkdir(exist_ok=True)

    for _file in _files:
        shutil.move(_file, archive / _file.name)

    print(f'end at { time.localtime() }')


def move_dir(dir_to_move: Path):
    emotion = dir_to_move.name   #.split("_")[1]
    
    new_path = str(dir_to_move).replace(dir_to_move.name, emotion)
    dir_to_move = dir_to_move.rename(new_path)
    for pic in dir_to_move.iterdir():
        emotion = Path(dir_to_move.parent.parent / dir_to_move.name)
        emotion.mkdir(exist_ok=True)
        print(f"move pic: {pic}\nto {str(emotion / pic.name)}")
        shutil.move(pic, emotion / pic.name)
    if not any(dir_to_move.iterdir()):
        shutil.rmtree(dir_to_move)
    else:
        raise Exception(f"{dir_to_move} not empty")


if __name__ == "__main__":
    main('./FERG_DB_256')