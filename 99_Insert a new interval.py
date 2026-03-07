# Insert a new interval

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = []
    for interval in intervals:      
        if not merged or merged[-1][1] < interval[0]:  # No overlap
            merged.append(interval)
        else:  # Overlap, merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def insert_interval(intervals, new_interval):
    intervals.append(new_interval)  # Add the new interval to the list
    return merge_intervals(intervals)  # Merge overlapping intervals

# Example usage
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))  # Output: [[1, 5], [6, 9]]