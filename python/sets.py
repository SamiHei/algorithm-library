#! /usr/bin/python3

class Entry:

    '''
    Parent is negative value if the entry is first entry in the set and it
    indicates the size of the set. Else the parent is entry.
    '''
    def __init__(self, parent, content):
        self.parent = parent
        self.content = content


    def set_parent(self, parent):
        self.parent = parent

        
    def get_parent(self):
        return self.parent


    def set_content(self, content):
        self.content = content


    def get_content(self):
        return self.content


'''
Test program for sets (union and find operations)
'''
def main():
    entry_1 = Entry(-1, "kiuru")
    entry_2 = Entry(-1, "lokki")
    entry_3 = Entry(-1, "rastas")
    entry_4 = Entry(-1, "sorsa")
    entry_5 = Entry(-1, "varis")

    union_find(entry_1, entry_2)
    print(entry_1.get_content())
    print(entry_1.get_parent()) # Size of the set
    print(entry_2.get_content())
    print(entry_2.get_parent()) # Parent entry memory address

    print("=" * 50)

    union_find(entry_3, entry_4)
    print(entry_3.get_content())
    print(entry_3.get_parent()) # Size of the set
    print(entry_4.get_content())
    print(entry_4.get_parent()) # Parent entry memory address

    print("=" * 50)
    
    union_find(entry_1, entry_3)
    print(entry_1.get_content())
    print(entry_1.get_parent()) # Size of the set
    print(entry_3.get_content())
    print(entry_3.get_parent()) # Parent entry memory address

    print("=" * 50)

    union_find(entry_1, entry_5)
    print(entry_1.get_content())
    print(entry_1.get_parent()) # Size of the set
    print(entry_5.get_content())
    print(entry_5.get_parent()) # Parent entry memory address


'''
fEntry and sEntry must be root entry in the set
'''
def union(fEntry, sEntry):
    size = fEntry.get_parent() + sEntry.get_parent()
    if (fEntry.get_parent() <= sEntry.get_parent()):
        fEntry.set_parent(size)
        sEntry.set_parent(fEntry)
    else:
        sEntry.set_parent(size)
        fEntry.set_parent(sEntry)


def find(entry):
    root_entry = entry
    while (type(root_entry.get_parent()) != int):
        root_entry = root_entry.get_parent()

    while (type(entry.get_parent()) != int):
        temp_entry = entry
        entry = entry.get_parent()
        temp_entry.set_parent(root_entry)

    return root_entry


def union_find(fEntry, sEntry):
    first = find(fEntry)
    second = find(sEntry)
    union(first, second)


if __name__ == "__main__":
    main()
