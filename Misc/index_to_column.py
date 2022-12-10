from math import floor

def index_to_column(idx):
    supermajor = chr(65 + floor((idx - 26) / (26**2) - 1)) if (idx > 26**2 + 25) else ""
    major = chr(65 + (floor((idx / 26 - 1)) % 26)) if idx > 25 else ""
    minor = chr(65 + idx % 26)
    return str(supermajor + major + minor)

def column_to_index(col):
    return ord(col[-1]) - 65 + (26*(ord(col[-2]) - 65 + 1) if len(col) > 1 else 0) + (26**2*(ord(col[-3]) - 65 + 1) if len(col) > 2 else 0)

if __name__ == '__main__':
    print(index_to_column(18277))