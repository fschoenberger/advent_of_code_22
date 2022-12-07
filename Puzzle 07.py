import math

class xmas_folder:
    def __init__(self, parent = None):
        self.parent: xmas_folder | None = parent
        self.children_dirs: dict[str, xmas_folder] = {}
        self.children_files: dict[str, int] = {}

    def get_size(self) -> int:
        sum = 0
        for dir in self.children_dirs.values():
            sum += dir.get_size()
        
        for size in self.children_files.values():
            sum += size

        return sum

    def add_ls_entry(self, entry: str) -> None:
        if entry.startswith("dir"):
            self.children_dirs[entry[4:]] = xmas_folder(self)
            # print(f"Added directory {entry[4:]}")
        else:
            file_info = entry.split(" ")
            self.children_files[file_info[1]] = int(file_info[0])
            # print(f"Added file {file_info[1]} ({file_info[0]})")

    def navigate_to_relative_path(self, path: str):
        if path == "":
            return self


        next_hop = path.split("/")[0]
        # print(f"Changing to directory {next_hop}")

        if next_hop == "..":
            return self.parent.navigate_to_relative_path(path[len(next_hop):])
        else:
            return self.children_dirs[next_hop].navigate_to_relative_path(path[len(next_hop):])

    def __str__(self) -> str:
        return self.get_pretty_print_string()

    def get_pretty_print_string(self, tabs: str = "") -> str:
        ret = ""
        for name, size in self.children_files.items():
            ret += f"{tabs}- {name} ({size})\n"
        
        for name, dir in self.children_dirs.items():
            ret += f"{tabs}-  {name} (dir, size = {dir.get_size()})\n"
            ret += dir.get_pretty_print_string(tabs + "  ")
        
        return ret

    def walk_directories(self, walker):
        walker(self)
        
        for name, dir in self.children_dirs.items():
            dir.walk_directories(walker)
            # walker(name, dir)

class part1_directory_walker:
    def __init__(self):
        self.running_total = 0

    def __call__(self, folder: xmas_folder) -> None:
        # print(f"Looking at folder {name}")
        size = folder.get_size()
        if size <= 100000:
            self.running_total += size

    def get_total_size(self):
        return self.running_total

class part2_directory_walker:
    def __init__(self, required_space: int):
        self.required_space = required_space
        self.current_min = math.inf

    def __call__(self, folder: xmas_folder) -> None:
        size = folder.get_size()
        if size >= self.required_space and size <= self.current_min:
            self.current_min = size

    def get_size(self) -> int:
        return self.current_min

def main():
    with open("./Puzzle 07.txt") as f:
        xmas_root = xmas_folder()

        current_folder = xmas_root

        for line in f.readlines():
            if line.startswith("$"):
                if line.startswith("$ cd /"):
                    current_folder = xmas_root.navigate_to_relative_path(line[6:-1])
                elif line.startswith("$ cd"):
                    current_folder = current_folder.navigate_to_relative_path(line[5:-1])
            else:
                # Add files from directory listing 
                current_folder.add_ls_entry(line[:-1])

        # print(xmas_root)

        walker1 = part1_directory_walker()
        xmas_root.walk_directories(walker1)
        print(f"Solution to part 1 is {walker1.get_total_size()}")

        free_space = 70000000 - xmas_root.get_size()

        print(f"Free space is {free_space}, thus we required {30000000 - free_space} more")

        walker2 = part2_directory_walker(30000000 - free_space)
        xmas_root.walk_directories(walker2)
        print(f"Solution to part 2 is {walker2.get_size()}")

if __name__ == "__main__":
    main()