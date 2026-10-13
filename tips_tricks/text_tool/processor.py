import re

from text_tool.decorators import calculate_func_execution_time_decorator


@calculate_func_execution_time_decorator
def get_word_frequency_report(text):
    search_text = re.findall(r"\w+", text.lower())
    dict_final_result = {}
    for word in search_text:
        if word in dict_final_result:
            dict_final_result[word] += 1
        else:
            dict_final_result[word] = 1
    lines = [f"{word}: {count}" for word, count in dict_final_result.items() ]
    result_text = "\n".join(lines)
    return result_text
