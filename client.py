import streamlit as st
import requests

st.set_page_config(page_title="Lumina Creative", layout="centered")
st.title("🎨 Lumina Creative - Text-to-Image")

prompt = st.text_area("Enter your image prompt:", 
                      "A serene mountain landscape at sunset, cinematic lighting")
negative_prompt = st.text_input("Negative prompt (optional):", 
                                "blurry, low quality, distorted")

if st.button("Generate Image"):
    with st.spinner("Generating... (this may take 10-30 seconds)"):
        try:
            response = requests.post(
                "http://localhost:8000/generate/image",
                json={
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "num_inference_steps": 30
                }
            )
            if response.status_code == 200:
                st.image(response.content, caption="Generated Image", use_column_width=True)
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")

st.info("Start the FastAPI server first: `uvicorn main:app --reload`")
