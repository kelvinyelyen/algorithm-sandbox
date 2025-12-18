def job_sequencing(jobs, t):
    """
    Job Sequencing Problem using Greedy Algorithm.
    jobs: list of tuples (job_id, deadline, profit)
    t: max time slots available
    """
    n = len(jobs)

    # Sort all jobs according to decreasing order of profit
    # jobs[i][2] is profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job_sequence = ['-1'] * t

    # Iterate through all given jobs
    for i in range(n):
        # Find a free slot for this job (Note that we start
        # from the last possible slot)
        # We check from min(t - 1, job_deadline - 1) down to 0
        for j in range(min(t - 1, jobs[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job_sequence[j] = jobs[i][0]
                break
    
    # Filter out empty slots if any (though logic fills available ones)
    return [job for job in job_sequence if job != '-1']

if __name__ == "__main__":
    # Job ID, Deadline, Profit
    jobs = [
        ('a', 2, 100),
        ('b', 1, 19),
        ('c', 2, 27),
        ('d', 1, 25),
        ('e', 3, 15)
    ]
    print(f"Jobs (ID, Deadline, Profit): {jobs}")
    
    # Let's assume we have 3 time slots
    t = 3
    sequence = job_sequencing(jobs, t)
    
    print(f"Following is maximum profit sequence of jobs: {sequence}")
    # Expected: c, a, e (Profit 27, 100, 15 -> Sequence might differ based on deadline)
    # Correct trace:
    # 1. 'a' (100) -> dl 2. Slot 1 (0-1) or Slot 2 (1-2). Takes Slot 1. (Index 1)
    # 2. 'c' (27) -> dl 2. Slot 1 taken. Takes Slot 0. (Index 0)
    # 3. 'd' (25) -> dl 1. Slot 0 taken. Skip.
    # 4. 'b' (19) -> dl 1. Slot 0 taken. skip.
    # 5. 'e' (15) -> dl 3. Slot 2 free. Takes Slot 2.
    # Result: c, a, e
