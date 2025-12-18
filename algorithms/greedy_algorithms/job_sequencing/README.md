# Job Sequencing Problem

## What is it?
The **Job Sequencing Problem** is a greedy algorithm where the objective is to maximize profit by completing jobs that have deadlines.
Each job has:
- A Job ID.
- A Deadline (time by which it must be finished).
- A Profit (earned if finished by deadline).

Assumption: Each job takes 1 unit of time.

## How it works
1.  **Sort**: Sort all jobs in decreasing order of profit.
2.  **Initialize**: Create a time slot array (size equal to max deadline) initialized to empty.
3.  **Iterate**: For each job in the sorted list:
    - Try to assign it to the latest possible free time slot (closest to its deadline).
    - If a slot is found, mark it as occupied and add the job to the result.
    - If no slot is free before its deadline, skip the job.

## Complexity
- **Time**: **O(n^2)**. Sorting takes O(n log n), but finding a slot takes O(n) for each of n jobs in the worst case (using simple array). Using Disjoint Set (DSU) can optimize slot finding to nearly O(n).
- **Space**: **O(t)**, where t is the maximum deadline.

## Example Usage
```bash
python3 job_sequencing.py
```
