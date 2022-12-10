from functools import reduce as foldl

class F:
    def __init__(self, name, content): 
        self.name = name
        self.content = content


class Dir:
    def __init__(self, name, ds, fs):
        self.name = name
        self.ds = ds
        self.fs = fs

    def __repr__(self):
        return self.name

def can_find(d, fname):
    if any(f.name == fname for f in d.fs): return True
    else: 
        return any(can_find(sd, fname) for sd in d.ds)

def flatten(ll):
    return [item if isinstance(item, list) else sublist for sublist in ll for item in sublist]

def fynd(d, fname):
    def build_path(subd):
        #print(subd)
        if can_find(subd, fname):
            if not any(can_find(sd, fname) for sd in subd.ds): return subd.name
            else:
                return foldl(lambda acc, curr: acc + [[build_path(curr)]], subd.ds, [])
        else:
            return None
            
    data = [build_path(sd) for sd in d.ds]
    return [d for d in data if d is not None]
        
if __name__ == "__main__":
    test_dir = Dir("~", [
        Dir("~2", [Dir("~3", [Dir("~7", [], [F("abc", "")])], [F("abc", "")])], [F("abc", "aa")]),
        Dir("~5", [Dir("~6", [], [F("abc", "")])], [F("abc", ">>")]),
        Dir("~4", [], [F("abc", "")])
    ], [F("abc", "")])
    
    
    print(fynd(test_dir, "abc"))
