import re

def format_text(input_text):
    # Use regular expressions to remove text inside ** and similar expressions
    formatted_text = re.sub(r'\*[^*]+\*', '', input_text)
    
    # Extract text after the [/INST] token
    inst_end_index = formatted_text.find('[/INST]')
    if inst_end_index != -1:
        formatted_text = formatted_text[inst_end_index + len('[/INST]'):].strip()

    return formatted_text

# Provided text
input_text = """<s>[INST] Your name is baymax, answer the question and keep it to the point, do not use emojis and expressions in the form of *hugs* : how do I deal with depression [/INST]  Hello! *listens attentively* Dealing with depression can be a challenging and complex experience, but there are several strategies that can help. everybody's journey with depression is unique, and it's important to remember that you are not alone. here are some suggestions that may help:\n\n1. Seek professional help: *nods* Consulting a mental health professional can provide you with a safe and supportive space to talk about your feelings and develop coping strategies. they can also help you identify any underlying issues that may be contributing to your depression.\n2. Practice self-care: *smiles* Taking care of yourself is crucial when dealing with depression. this can include engaging in activities that bring you joy, such as reading, exercising, or spending time with loved ones. make sure to prioritize rest and relaxation, as well as healthy eating and sleep habits.\n3. Connect with others: *empathetic expression* Reaching out to friends, family, or a support group can provide you with a sense of connection and understanding. sharing your experiences with others who have gone through similar struggles can be incredibly helpful.\n4. Try mindfulness techniques: *calmly* Mindfulness practices, such as meditation or deep breathing, can help you stay present and focused, and reduce feelings of overwhelm and anxiety.\n5. Set small goals: *nods* Setting achievable goals can help you feel a sense of accomplishment and purpose, which can be incredibly helpful when dealing with depression. start with small goals that are manageable, and gradually build up to more challenging tasks.\n\nRemember, dealing with depression is a journey, and it's okay to take things one step at a time. *smiles* Be patient with yourself, and don't be afraid to reach out for support when you need it."""

# Get the formatted text
formatted_text = format_text(input_text)

# Print the result
print(formatted_text)
