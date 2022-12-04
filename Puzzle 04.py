import re

def intervals_overlap_fully_contained(intervals: tuple[int, int, int, int]) -> bool:
    if intervals[0] <= intervals[2] and intervals[1] >= intervals[3]:
        return True
    if intervals[0] >= intervals[2] and intervals[1] <= intervals[3]:
        return True

    return False

def intervals_overlap(intervals: tuple[int, int, int, int]) -> bool:
    x0 = intervals[0]
    x1 = intervals[1]
    y0 = intervals[2]
    y1 = intervals[3]

    return x0 <= y1 and y0 <= x1

def main() -> None:
    with open("Puzzle 04.txt") as f:
        intervals = [re.search("(\d+)-(\d+),(\d+)-(\d+)", line).groups() for line in f.readlines()]
        fully_contained_intervals = [val for val in map(lambda x: tuple(map(lambda y: int(y), x)), intervals) if intervals_overlap_fully_contained(val)]
        overlapping_intervals = [val for val in map(lambda x: tuple(map(lambda y: int(y), x)), intervals) if intervals_overlap(val)]
        
        print(f"There are {len(fully_contained_intervals)} elves with intervals fully contained in each other.")
        print(f"There are {len(overlapping_intervals)} elves with overlapping intervals.")

if __name__  == "__main__":
    main()