# Activity Selection Problem

## What is it?
The **Activity Selection Problem** is an optimization problem to select the maximum number of activities that can be performed by a single person or machine, assuming that a person can only work on a single activity at a time. Each activity has a start time and a finish time.

## How it works (Greedy)
1.  Sort the activities according to their finishing time.
2.  Select the first activity (as it finishes first, leaving maximum time for others).
3.  Iterate through the remaining activities and select an activity if its start time is greater than or equal to the finish time of the last selected activity.

## Complexity
- **Time**: **O(N log N)** (due to sorting).
- **Space**: **O(1)** (if indices are stored) or O(N).

## Example Usage
```bash
python3 activity_selection.py
```
