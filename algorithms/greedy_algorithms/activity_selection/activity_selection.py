def activity_selection(activities):
    """
    activities: list of tuples (start, finish)
    Assumes activities are NOT sorted by finish time initially.
    """
    # Sort activities by finish time
    selected = []
    
    # Sort by the second element of tuple (finish time)
    activities.sort(key=lambda x: x[1])

    # The first activity is always selected
    if activities:
        i = 0
        selected.append(activities[i])
        
        # Consider remaining activities
        for j in range(1, len(activities)):
            # If this activity has start time greater than or equal
            # to the finish time of previously selected activity, then select it
            if activities[j][0] >= activities[i][1]:
                selected.append(activities[j])
                i = j
                
    return selected

if __name__ == "__main__":
    # (start, finish)
    data = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(f"Activities: {data}")
    
    selected_activities = activity_selection(data)
    print(f"Selected Activities: {selected_activities}")
    # Expected: (1, 2), (3, 4), (5, 7), (8, 9)
