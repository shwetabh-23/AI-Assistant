import re

def format_text(input_text):

    formatted_text = re.sub(r'\*[^*]+\*', '', input_text)
    
    inst_end_index = formatted_text.find('[/INST]')
    if inst_end_index != -1:
        formatted_text = formatted_text[inst_end_index + len('[/INST]'):].strip()

    return formatted_text


