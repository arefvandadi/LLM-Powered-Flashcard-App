# Overview
The project focuses on creating a Flashcard App that can use LLM to extract words from youtube videos on youtube and articles online selected by the user.


# Requirements
Install packages in requirements.txt. Use the following code in terminal:

pip install -r requirements.txt


Also, FFmpeg need to be installed on your operating system. You can find FFmpeg package [HERE](https://www.gyan.dev/ffmpeg/builds/)
- Installation Instructions for Windows:[Click Here](https://phoenixnap.com/kb/ffmpeg-windows)
- Installation Instructions for Mac:[Click Here](https://phoenixnap.com/kb/ffmpeg-mac)


# Configuration
You need to provide an OpenAI API Key for the project to work. OPENAI API is needed for the word extraction. You can do wither o the following two approaches to set the key in your system:
- **Environment Variable**: You can set the `OPENAI_API_KEY` environment variable in your system.
- **.env File**: Alternatively, you can create a `.env` file in the root directory of your project with the following content: OPENAI_API_KEY=your_openai_api_key_here






