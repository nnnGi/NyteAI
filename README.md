# NyteAI
![Python Version](https://img.shields.io/badge/Python-%3E=3.12-blue.svg) \
Generative AI using Google Gemini (Imagen, Text and Code Running)

Python Libraries Required:\
    - [PIL](https://pypi.org/project/pillow/) \
    - [Google-Genai](https://pypi.org/project/google-genai/)\
    - io (Preinstalled)

This AI program can generate text and images and run code (mostly Python).
It is NyteAI or SwiftAI, written by @\_nnn_ (A.K.A @FlyBoyAce2) in Python 3.13.2

Generate 2 Gemini API keys and put both in their corresponding variables below in the # API Keys Section
Generate Gemini API Keys at https://aistudio.google.com/

Models Used:
```python
DISTRIBUTION_MODEL = 'gemini-2.0-flash-lite' # Chooses whether to use text or image generation model
TEXT_GEN_MODEL = 'gemini-2.0-flash-thinking-exp' # Experimentive Text Generation Model with Thinking Abilities and Code Running Capabilities
IMAGE_GEN_MODEL = 'gemini-2.0-flash-exp-image-generation' # Experimentive Image Generation Model
```

API Keys Go Here:
```python
KEY_MODELS = '{Generative Model API Key Here}'
KEY_DISTRIBUTE = '{Distributive Model API Key Here}'
```

This programme pulls on two instances of Google Gemini:
1. Check if the user request wants AI to generate text or image or to end the programme<br>
2. Fufil request with corresponding model (Text or Imagen)<br><br>

# Possible Errors when Running NyteAI
```python
raise Exception("ModelActivationError: Distribution Model failed to activate Text or Imagen Model")
```
Occurs when the distribution model fails to return a result that can activate either model, which means that the output did not contain ```Text```, ```Image``` or ```Quit```

© Copyright \_nnn_ 2025 - 2025
