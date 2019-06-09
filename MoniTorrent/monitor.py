#!/usr/local/bin/python3.7

import os

dirpath = os.path.join(os.path.sep + "Users", "zackamiton", "Documents", "Torrents")

bandcamp = os.path.join(dirpath, "Bandcamp Downloads")
soulseek = os.path.join(dirpath, "SoulSeek Downloads")

log_file = os.path.join(dirpath, "DownloadLog.txt")
bandcamp_log = os.path.join(dirpath, "BandcampLog.txt")
soulseek_log = os.path.join(dirpath, "SoulSeekLog.txt")

with open(soulseek_log, 'r+') as ss:
    folder_entries = [file.strip() for file in os.listdir(soulseek) if file != '.DS_Store' and file.lower() != "untitled folder" and not os.path.isfile(file)]
    file_entries = [line.strip() for line in ss]

    for entry in (set(folder_entries) - set(file_entries)):
        file_entries.append(entry)

    file_entries.sort(key=lambda s: s.lower())
    ss.seek(0)
    ss.truncate()

    for item in file_entries:
        ss.write(item+"\n")


if __name__ == "__main__":
    pass