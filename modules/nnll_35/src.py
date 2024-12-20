#
import re

def get_last_num_from_filename(filename: str, search_value: str) -> int:
        try:
            search_value = search_value.lower() # normalize tring formatting; digits are focus
            lower_filename = filename.lower()
            search_index = lower_filename.rindex(search_value) # find last location of match
        except ValueError as error_log:
            print(f"File not named with search_term {error_log}.")
        else:
            if search_index is not None: # found something
                crop_num = str(lower_filename[search_index - 2:search_index]) # digits preceding to trim
                crop_num = re.sub(r"^\W+|\W+$", "", crop_num) # any string with, no character, once or more, ending with no character, once or more, must end)
                if crop_num.isdigit():
                    match_number  = int(crop_num) # double digit nummber
                    return match_number
                elif crop_num[1:].isdigit():
                    match_number = int(crop_num[1:]) # single digit num
                    return match_number
