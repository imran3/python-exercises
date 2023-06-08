# given a dictionary of contacts, return list of names sorted alphabetically
def sort_contacts_list(dictionary: dict):
    sorted_list =  sorted(dictionary.items(), key = lambda x: x[1])
    sorted_names_list = list(x[1] for x in sorted_list)
    return sorted_names_list

def sort_contacts_list_v2(dictionary: dict):
    return sorted(dictionary.values())