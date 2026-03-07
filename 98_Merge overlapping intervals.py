# Merge overlapping intervals

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = []
    for interval in intervals:      
        if not merged or merged[-1][1] < interval[0]:  # No overlap
            merged.append(interval)
        else:  # Overlap, merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]