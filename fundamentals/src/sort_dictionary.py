# given a dictionary of contacts, return list of names sorted alphabetically
def sort_contacts_list(dictionary):
    sorted_list =  sorted(dictionary.items(), key = lambda x: x[1])
    names = list(x[1] for x in sorted_list)
    return names

def sort_contacts_list_v2(dictionary):
    return sorted(dictionary.values())