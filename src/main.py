# import yt_dlp
from media_processor import MediaProcessor
import ffmpeg
from transformers import pipeline
import textwrap
from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


##################### Download Youtube Videos to Local Drive ###############################

# YOUTUBE_LINK = "https://youtu.be/rqTl-livoRo"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/65ya2V7Gi74"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"

# youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
# youtube_handler.youtube_video_downloader()


##################### Extracting Audio from Downloaded Videos ###############################
video_file = ffmpeg.input("./data/videos/Theater of Politics.mp4")
# video_file.output("./data/audio/audio.mp3", acodec="mp3").run()
video_file.output("./data/audio/audio.wav", acodec="pcm_s16le").run()


##################### Use Speech Recognition LLM Models to Create Transcriptions ###############################
# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
# output = pipe("./data/audio/audio.wav")
# transcription_text = output["text"]
# wrapped_transcription = textwrap.fill(transcription_text, width=80)

# with open("./data/text/transcription.txt", "w") as file:
#     file.write(wrapped_transcription)

#################### Use a Free LLM to Analyze the Text and Extract Words ################################
# with open("./data/text/transcription.txt", "r") as file:
#     context = file.read()
# print(context)

## LLama2-CHAT-7b --> Seem to need login and Huggingface Credentials
# llama_textgenerator = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

# messages = [
#     {"role": "user", "content": "How many countries are in the word?"},
# ]
# response = llama_textgenerator(messages)
# print(response)

## GPT2 --> Seem to just generate similar sentences to what the question is.
# gpt_textgenerator = pipeline("text-generation", model="openai-community/gpt2")
# response = gpt_textgenerator("Is there a world in the following text that is How many countries are in the world?")

## ROBERTA --> You need to give it a context and it is not that good at answering them
# questions_answering = pipeline("question-answering", model="deepset/roberta-base-squad2")
# response = questions_answering(question="How many words are in the context provided", context=context)
# print(response)

######################### Use GPT4 API to Analyze the Text and Extract Words ############################
with open("./data/text/transcription.txt", "r") as file:
    context = file.read()

content = f"Please investigate the following context and create a list of English words in the context provided that \
     that is good for an intermediate english as a second language learner to practice to improve his/her vocabulaory:\
        \n\ncontext = {context}\
        \n\nNotice there is no need for explaining the meaning of the word. The response should only include the words\
          in the format of a python list. No explanations before or after the python list.\
        \n\n Also there is no need to output words = [], remove the 'words =' and only output the python list"

def get_gpt_response(content: str = content, api_key=OPENAI_API_KEY):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
    # model="gpt-4o",
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": content}
    ]
    )
    return completion.choices[0].message.content

print(get_gpt_response(content))






