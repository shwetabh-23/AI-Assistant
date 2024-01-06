from Face_Recognition import check_user, new_user
from TTS import text_to_speech, speech_to_text
from conversation import llama_chat
from transformers import (AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer, pipeline)
import torch
from googleapis import get_date_day, get_emails, get_time_of_day
import os
import sys
from system_utils import restart_program, execute_terminal_command, terminate_process_by_pid
from ObjectDetection import object_detection

all_img_path = r'/home/harsh/AI-Projects/AI-Assistant/Images'

base_model_name = "NousResearch/Llama-2-7b-chat-hf"

# Tokenizer
llama_tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
llama_tokenizer.pad_token = llama_tokenizer.eos_token
llama_tokenizer.padding_side = "right" 

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=False
)

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
        quantization_config=quant_config,
    device_map={"": 0})

time_of_day = get_time_of_day()
date, day = get_date_day()
emails = get_emails()

text_to_speech(f"good {time_of_day},  I am {day}, your personal Llama based question-answering chatbot. I will try to answer all your questions. When you are done, please say I am satisfied with my care.")
text_to_speech('I will scan you now, press space to capture a picture with a big smile on your face')

user_exists, user_name = check_user(all_img_path)

text_to_speech('Scan complete')

if user_exists:
    if user_name == 'shwetabh':
        user_name = 'Master shwetaabh'
    
    text = 'Hi {}'.format(user_name)

    text_to_speech(text)
    while True:
        query = speech_to_text()
        if query == 'none':
            continue
        print('User : ', query)

        if 'i am satisfied with my care' in query.strip().lower():
            break

        elif 'emails' in query.strip().lower() or 'email' in query.strip().lower():
            text_to_speech('Sure, emails displayed in your screen')
            for subject in emails.keys():
                print(f'{subject} : {emails[subject]}')
                print('\n')
        elif 'object' in query.strip().lower() or 'detect' in query.strip().lower() or 'holding' in query.strip().lower() or 'hand' in query.strip().lower():
            text_to_speech('Object detection activated, press space to capture the object on the screen')

            objects = object_detection()
            all_objs = ''
            for object in objects:
                all_objs += ', '
                all_objs += object

            while True : 
                query = speech_to_text()
                n = 0
                print('User : ', query)
                prelude = f'you are currently in object detection mode. the detected objects in the screen are {all_objs}. Based on this information, answer the question : ' if n == 0 else query
                if 'exit' in query.strip().lower() or 'quit' in query.strip().lower():
                    break
                elif 'i am satisfied with my care' in query.strip().lower():
                    sys.exit()
                else:
                    response = llama_chat(query = (prelude + query), base_model=base_model, llama_tokenizer=llama_tokenizer)
                    print(f'{day} :', response)
                    text_to_speech(response)
                    n += 1

        else:
            prelude = f'You are my assistant, your name is {day}, answer the question and keep it to the point : '
            response = llama_chat(query = (prelude + query), base_model=base_model, llama_tokenizer=llama_tokenizer)
            print(f'{day} :', response)
            text_to_speech(response)

else:
    text_to_speech('User not found')
    text_to_speech('Adding new user : ')

    save_path = all_img_path

    new_user(save_path=save_path)
    text_to_speech('New user added, please restart the process.')
    



