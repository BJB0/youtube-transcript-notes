import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # load all the nenvironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with st.expander("Available Models"):
    try:
        models = genai.list_models()
        for m in models:
            st.write(f"{m.name} => Supported: {m.supported_generation_methods}")
    except Exception as e:
        st.error(f"Error fetching models: {e}")


prompt="""You are a youtube video summarizer. You will be picking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. Please provide the summary of the text given here: """


## getting the transcript data from YT
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
 
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        return f"Error generating summary: {str(e)}"

 


st.title("Youtube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter Youtube Video Link:")

if youtube_link:
  video_id = youtube_link.split("=")[1]
  print(video_id)
  st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
  
if st.button("Get Detailed Notes"):
  transcript_text =extract_transcript_details(youtube_link)
  
  if transcript_text:
    summary=generate_gemini_content(transcript_text,prompt)
    st.markdown("Detailed Notes:")
    st.write(summary)
    
    st.download_button(
      label="Download Notes as .txt",
      data=summary,
      file_name="yotube_summary.txt",
      mime="text/plain"
    )