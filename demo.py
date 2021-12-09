import os, fnmatch
# patterns = ["*.mp3", "*.ogg", "*.flac", "*.wav"]
patterns = ["mama"]

for root, dirs, files in os.walk("/home/ok/"):
    i = 0
    for pattern in patterns:
        for filename in fnmatch.filter(files, pattern):
            print(root, dirs, filename)