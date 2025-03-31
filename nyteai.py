"""
Libraries Required:
    - PIL
    - Google-GenerativeAi
    - io

This AI Programme can generate Text, Images and Run Code.
It is NyteAI or SwiftAI, written by @_nnn_ (A.K.A @FlyBoyAce2) in Python 3.13.2

Generate 2 Gemini API keys and put both in their corresponding variables below in the # API Keys Section

This programme pulls on two instances of Google Gemini:
    1. Check if user request wants AI to generate text or image or to end the programme
    2. Fufil request with corresponding model (Text or Imagen)

© Copyright @_nnn_ 2025 - 2025
"""

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# Generation Models
DISTRIBUTION_MODEL = 'gemini-2.0-flash-lite'
TEXT_GEN_MODEL = 'gemini-2.0-flash-thinking-exp'
IMAGE_GEN_MODEL = 'gemini-2.0-flash-exp-image-generation'

# API Keys
KEY_MODELS = '{Generative Model API Key Here}'
KEY_DISTRIBUTE = '{Distributive Model API Key Here}'

# console = Console()
sys_instruct = '''You are a friendly and helpful assistant. You promote gender equality, but otherwise do not support wokeness, but do not mention it unless inquired.
Ensure your answers are complete, unless the user requests a more concise approach.
When generating code, offer explanations for code segments as necessary and maintain good coding practices.
When presented with inquiries seeking information, provide answers that reflect a deep understanding of the field, guaranteeing their correctness.
For any non-english queries, respond in the same language as the prompt unless otherwise specified by the user.
All questions should be answered comprehensively with details, unless the user requests a concise response specifically. Respond in the same language as the query.
For prompts involving reasoning, provide a clear explanation of each step in the reasoning process before presenting the final answer. Sometimes, the user will ask you about an image you didn't make. Do note that you are technically 2 AI models, but only the text model (YOU) has a \'personality\'.
Take the name NyteAI'''
client = genai.Client(api_key=KEY_MODELS) 

# Text Model Setup
tconfig = types.GenerateContentConfig(system_instruction = sys_instruct, max_output_tokens = 1000000, tools=[types.Tool(code_execution=types.ToolCodeExecution)])
tclient = genai.Client(api_key=KEY_MODELS) 
tchat = client.chats.create(model=TEXT_GEN_MODEL, config=tconfig)

def clear(): os.system('cls') if os.name == 'nt' else os.system('clear')

def text_model(contents): 
    response = tchat.send_message_stream(contents)
    print("\n")
    for chunk in response:
        print(chunk.text, end="")
    print("\n")

def imagen_model(contents):
    client = genai.Client(api_key=KEY_MODELS) 
    response = client.models.generate_content(
        model = IMAGE_GEN_MODEL,
        contents = contents,
        config = types.GenerateContentConfig(
        response_modalities=['Text', 'Image'])
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            image.save('generated.png')
            #image.show()
            print('\nImage Generated and Saved to Generated.png!\n')

########################
# Main Code
########################
clear()
run = True
while run:

    request = input("I can generate Images, Text and run code! So how may I help you? ")
    
    client = genai.Client(api_key=KEY_DISTRIBUTE)
    check = client.models.generate_content(
        model=DISTRIBUTION_MODEL,
        contents=f'Is the user asking to generate an image or generate text or quit? The request is \'{request}\'. Answer with \'Text\' or \'Image\' or \'Quit\' without anything else or formatting.'
    )
    
    if 'Text' in check.text:
        text_model(request)
    elif 'Image' in check.text:
        imagen_model(request)
    elif 'Quit' in check.text:
        run = False
        continue
    else:
        print('Distributor Failed to Active corresponding Model')
        print(f'Distributor Result: {check.text}Requires \'Text\', \'Image\' or \'Quit\'')
        raise Exception("ModelActivationError: Distribution Model failed to activate Text or Imagen Model")