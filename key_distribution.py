def assign_keys(networks):
    """
    Assigns a unique symmetric key for each unique network.
    Each person gets the key in the lowest available slot on their device (1 to 4).

    Parameters:
        networks (list of tuple): Each tuple represents a network of people.
    
    Returns:
        list of dict: Each dict has the network number, key id, and a mapping of person to slot.

    Raises:
        Exception: If any person is assigned more than 4 keys (their device is full).
    """

    # Deduplication of Networks
    seen = set()
    unique_networks = []

    for net in networks:
        fs = frozenset(net)
        if fs not in seen:
            seen.add(fs)
            unique_networks.append(fs)
    
    # Assign Keys to Each Network
    device_assignments = {}
    assignments = []
    key_id = 1

    for net in unique_networks:
        net_assignment = {"network": key_id, "key": key_id, "members": {}}

        for person in net:
            if person not in device_assignments:
                device_assignments[person] = {}
            
            assigned = False
            
            # Find the Lowest Available Slot
            for slot in range(1, 5):
                if slot not in device_assignments[person]:
                    device_assignments[person][slot] = key_id
                    net_assignment["members"][person] = slot
                    assigned = True
                    break

            if not assigned:
                raise Exception(f"{person}'s device is out of keys")
            
        assignments.append(net_assignment)
        key_id += 1
    
    return assignments

def print_assignments(assignments):
    """
    Prints the key distribution instructions in a clear format.

    Parameters:
        assignments (list of dict): The key assignment instructions.
    """

    for assignment in assignments:
        print(f"Network {assignment['network']}, key {assignment['key']} -")

        for person, slot in assignment["members"].items():
            print(f"{person} - put key {assignment['key']} in slot {slot}")
        print()