def anagram(string1, string2):
    string1_list = list(string1)
    string2_list = list(string2)
    sorted_string1 = sorted(string1_list)
    sorted_string2 = sorted(string2_list)
    if sorted_string1 == sorted_string2:
        print("that is an anagram")
    else:
        print("not an anagram")


