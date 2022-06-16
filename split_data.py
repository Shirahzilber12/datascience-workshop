import shutil
import os
from pathlib import Path
import time

def main(dir_path):
    dir_path = Path(dir_path)
    train_dir = dir_path.joinpath("train")
    train_dir.mkdir(exist_ok=True)
    test_dir = dir_path.joinpath("test")
    test_dir.mkdir(exist_ok=True)
    list_dir = [e for e in dir_path.iterdir() if e.name not in ["test", "train", "archive"]]
    for dir in list_dir:
        print(dir)
        emotion = dir.name
        emotion_dir_train = train_dir.joinpath(emotion)
        emotion_dir_train.mkdir(exist_ok=True)
        emotion_dir_test = test_dir.joinpath(emotion)
        emotion_dir_test.mkdir(exist_ok=True)
        files = [file for file in dir.glob("*")]
        print(f"count files is: {len(files)}")
        train_count = int(len(files) * 0.8)
        print(f"train: {train_count}")
        for _file in files[0:train_count]:
            print(f"move to: {emotion_dir_train}/{_file.name}")
            shutil.move(_file, emotion_dir_train/_file.name)
        for _file in files[train_count:]:
            print(f"move to:{emotion_dir_test}/{_file.name}")
            shutil.move(_file, emotion_dir_test / _file.name)
        if not any(dir.iterdir()):
            print(f"delete folder: {dir}")
            shutil.rmtree(dir)
        else:
            raise Exception(f"{dir} not empty")

if __name__ == "__main__":
    main('./CK+48')