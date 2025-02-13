# Approach for Processing 1 Million Records

If we were dealing with a massive data stream, such as 1 million records, we would need to optimize the code to avoid excessive memory consumption and improve performance. Here are some strategies/approaches that could be applied:

OBS: The only approach that I've really used is the second one, Using Optimized Data Structures with pandas, in terms of data migrations and data processing, from oracle database to a s3 bucket.

## 1. Using Stream Processing (Lazy Loading)
Currently, the code loads all records into memory (`load_json`), which is not feasible for large data volumes. Instead, we can use an iterator to process the data line by line:

```python
def stream_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield json.loads(line)  # Reading each line as an individual JSON
```
This allows processing the data without loading everything into memory.

## 2. Using Optimized Data Structures
- **`heapq`**: The use of `nsmallest` is already efficient for finding the N smallest elements without needing to sort the entire list.
- **`deque`**: To store a limited buffer, `collections.deque` is more efficient than regular lists.
- **`pandas` with `chunksize`**: If the JSON is too large, Pandas can be used with block reading:

```python
import pandas as pd

chunksize = 100000  # Processes 100k records at a time
for chunk in pd.read_json("records.json", lines=True, chunksize=chunksize):
    # Process each chunk separately
```

## 3. Reducing Comparisons with Sliding Window
Instead of keeping all records in memory for sorting, we can use a **min heap** to keep only the last 3 logins while processing the data:

```python
from heapq import heappush, heappop
from datetime import datetime

def find_top_3_streaming(records, cutoff_datetime):
    heap = []
    
    for record in records:
        last_login = datetime.strptime(record["last_login"], "%Y-%m-%dT%H:%M:%SZ")
        
        if last_login < cutoff_datetime:
            heappush(heap, (last_login, record["id"]))
            if len(heap) > 3:
                heappop(heap)  # Keep only the last 3

    return [record[1] for record in sorted(heap, reverse=True)]
```
This avoids the need to store all records for sorting.

## 4. Finding the Smallest Login Time Difference in Streaming
Instead of sorting the entire list, we can use a buffer to keep the last two records and calculate the difference incrementally:

```python
def find_closest_pair_streaming(records):
    prev_record = None
    min_diff = float("inf")
    closest_pair = None

    for record in sorted(records, key=lambda x: x["last_login"]):
        if prev_record:
            diff = (record["last_login"] - prev_record["last_login"]).total_seconds()
            if diff < min_diff:
                min_diff = diff
                closest_pair = (prev_record, record)

        prev_record = record

    return closest_pair
```
This approach avoids storing large amounts of unnecessary data.

---

## Summary
To handle 1 million records:
1. **Use stream reading** to avoid loading everything into memory at once.
2. **Apply optimized structures** such as `heapq`, `deque`, and Pandas with `chunksize`.
3. **Keep only the necessary records**, such as the last 3 logins, without needing to sort everything.
4. **Use an incremental approach** to find the closest pair in real-time.

These strategies help scale the solution for large data volumes, minimizing memory consumption and processing time. 🚀

