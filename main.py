import streamlit as st
import requests
import base64

# Load API credentials from secrets
api_key = st.secrets["azure_openai"]["api_key"]
endpoint = st.secrets["azure_openai"]["endpoint"]

# Streamlit app title
st.title("DALL-E 3 Image Generation")

# Input for the image prompt
prompt = st.text_area("Enter your image prompt:", placeholder="e.g., A futuristic city skyline at sunset with flying cars")

# Select image size
size = st.selectbox("Select Image Size:", ["1024x1024", "1792x1024", "1024x1792"])

# Sidebar info
st.sidebar.markdown("### About DALL-E 3 Image Generator")
st.sidebar.write("This app uses OpenAI's DALL-E 3 model to generate images from text prompts. Enter a prompt describing the image you'd like to see, and the app will generate it using AI technology.")
st.sidebar.write("The generated image is based on your input and can be viewed and downloaded from the provided URL.")

# Button to generate image
if st.button("Generate Image"):
    if not prompt:
        st.error("Please enter an image prompt.")
    else:
        with st.spinner("Generating image..."):
            headers = {
                'Content-Type': 'application/json',
                'api-key': api_key
            }

            data = {
                "prompt": prompt,
                "n": 1,
                "size": size
            }

            # Make API request
            response = requests.post(endpoint, headers=headers, json=data)

            if response.status_code == 200:
                image_data = response.json()

                # Extract and display revised prompt in the sidebar
                revised_prompt = image_data['data'][0]['revised_prompt']
                st.sidebar.write("✅ Image Generated Successfully!")
                st.sidebar.write("Revised Prompt:")
                st.sidebar.write(revised_prompt)

                image_url = image_data['data'][0]['url']
                st.sidebar.write("Image URL:")
                st.sidebar.write(image_url)
                
                # Check if 'url' is present in the response
                if 'url' in image_data['data'][0]:
                    image_url = image_data['data'][0]['url']
                    st.image(image_url, caption="Generated Image", use_container_width=True)

                else:
                    st.sidebar.error("❌ Image data not found in the response. Please check your API configuration.")
            else:
                st.sidebar.error(f"❌ Error {response.status_code}: {response.text}")

# Organization link at the bottom of the sidebar
st.sidebar.markdown("### Join the Community")
st.sidebar.markdown("Join [Curious PM](https://curious.pm) to connect, share, and learn with others! ")
