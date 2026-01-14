from bisect import bisect_right


def parse_input(raw):
	sections = raw.strip().split("\n\n")
	if len(sections) < 2:
		print("Invalid input format")
		return

	range_lines = [line.strip() for line in sections[0].splitlines() if line.strip()]
	id_lines = [line.strip() for line in sections[1].splitlines() if line.strip()]

	ranges = []
	for line in range_lines:
		start_str, end_str = line.split("-")
		start, end = int(start_str), int(end_str)
		if start > end:
			start, end = end, start
		ranges.append((start, end))

	ids = [int(value) for value in id_lines]
	return ranges, ids


def merge_ranges(ranges):
	if not ranges:
		return []

	sorted_ranges = sorted(ranges)

	def helper(index, merged):
		if index == len(sorted_ranges):
			return merged

		start, end = sorted_ranges[index]
		if merged and start <= merged[-1][1]:
			prev_start, prev_end = merged[-1]
			merged[-1] = (prev_start, max(prev_end, end))
		else:
			merged.append((start, end))
		return helper(index + 1, merged)

	return helper(0, [])


def count_fresh(ids, merged):
	if not merged:
		return 0, 0

	total_in_ranges = sum(end - start + 1 for start, end in merged) # Part 2 solution here!

	starts = [start for start, end in merged]
	count = 0
	for value in ids:
		idx = bisect_right(starts, value) - 1
		if idx >= 0 and value <= merged[idx][1]:
			count += 1
	return total_in_ranges, count



with open("input.txt", 'r') as f:
	raw = f.read()
ranges, ids = parse_input(raw)
merged = merge_ranges(ranges)
total_in_ranges, fresh_count = count_fresh(ids, merged)
print("Total available fresh ingredients in ranges:", total_in_ranges)
print("Total number of fresh ingredients:", fresh_count)



