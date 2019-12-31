import os
from mutagen.id3 import ID3
'''
TIT2: Title
TPE1: Artist
TRCK: Track #
TCON: Genre
TPE2: Album Artist
TDOR: Track Date of Release
TDRC: Track Release Date
COMM::eng: iTunes Comment
TSRC: Recording code
TPUB: Publisher
USLT::eng: Lyrics
APIC: Album Art
UFID: Owner Identifier
TMED: Media Type
TXXX: User-Defined Tags
POPM:{ID} — Sound Rating
'''

track = ID3(input())
print(track.getall("TXXX"))


