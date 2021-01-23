def format_input(to_format):
    result = None
    if type(to_format) == str:
        result = to_format.lower()
        result = result.strip()
        return result
    elif type(to_format) != str:
        return print("format_input() wasn't fed a string.")


# You feed it a list and it gives you a string. pretty sure i can make it take an attribute if I rewrite it with getattr


def format_objects_string(
    given_list,
):  # Returns "nothing" if empty list, returns "object, object, and object." style string.
    final_string = ""

    if len(given_list) == 0:
        return "nothing"

    try:
        if hasattr(given_list[0], "name") == True:  # If it's a list of objects
            if len(given_list) == 1:
                return given_list[0].name + "."
            if len(given_list) == 2:
                return given_list[0].name + " and " + given_list[1].name + "."
            if len(given_list) >= 3:
                for item in given_list[:-2]:
                    final_string += item.name + ", "
                final_string += (
                    given_list[-2].name + " and " + given_list[-1].name + "."
                )
            return final_string
    except KeyError:
        pass
    if (type(given_list)) == dict:  # If it's a dictionary
        listed_dic = []
        for key, value in given_list.items():
            listed_dic.append(key)
        if len(listed_dic) == 1:
            return listed_dic[0] + "."
        if len(listed_dic) == 2:
            return listed_dic[0] + " and " + listed_dic[1] + "."
        if len(listed_dic) >= 3:
            for item in listed_dic[:-2]:
                final_string += item + ", "
            final_string += listed_dic[-2] + " and " + listed_dic[-1] + "."
        return final_string

    if (type(given_list)) == list:  # If it's a list
        if len(given_list) == 1:
            return given_list[0] + "."
        if len(given_list) == 2:
            return given_list[0] + " and " + given_list[1] + "."
        if len(given_list) >= 3:
            for item in given_list[:-2]:
                final_string += item + ", "
            final_string += given_list[-2] + " and " + given_list[-1] + "."

        return final_string