## Join the Community

For more insights and discussions, join Curious PM at [https://curious.pm](https://curious.pm) to connect, share, and learn with others.


# OpenAi DALL-E 3 Image Generation

## About the Project

This application leverages OpenAI's DALL-E 3 model to generate images from user-provided text prompts. Users can input descriptive text, select image sizes, and generate AI-based images directly within the Streamlit interface.


## How It Works

### Overview

The script interacts with OpenAI's DALL-E 3 model through an API. It processes text prompts and returns generated images. This setup can be integrated into larger projects that require dynamic image generation.

### Logic Breakdown

1. **User Input**: Users provide a text prompt and select the desired image size.
2. **API Request**: The app sends a request to the DALL-E 3 API using provided credentials.
3. **Image Generation**: Upon successful API response, the image URL and revised prompt are displayed.
4. **Output Display**: The generated image is shown in the main app, while additional details appear in the sidebar.

### Step-by-Step Explanation

1. **Import Libraries**:
   - `streamlit` for UI components and app deployment.
   - `requests` for making HTTP requests to the API.

2. **Load API Credentials**:
   - The API key and endpoint are securely loaded from the `secrets.toml` file to ensure sensitive data isn't exposed.

3. **UI Elements**:
   - Text input field for the user to enter their image prompt.
   - Dropdown selection to choose from various image sizes.

4. **Generate Image**:
   - When the "Generate Image" button is clicked, the app constructs and sends a POST request to the DALL-E 3 API with the user's prompt and selected image size.

5. **Handle API Response**:
   - If the request is successful, the app retrieves the revised prompt and image URL from the API response.
   - These details are displayed in the sidebar for user reference.

6. **Output Display**:
   - The generated image is displayed in the main content area of the app, providing an immediate visual output.

7. **Error Handling**:
   - The app displays any errors in the sidebar, offering clear feedback on issues such as incorrect API keys or invalid prompts.

## Directory Structure

```
project-root/
│
├── app.py               # Main Streamlit application script
└── .streamlit/
    └── secrets.toml     # Stores API credentials securely
```

## Sample `secrets.toml`

```
[azure_openai]
api_key = "your_api_key_here"
endpoint = "your_endpoint_url_here"
```

## Expected Output

1. **Generated Image**: Displayed prominently in the main content area.
2. **Revised Prompt**: Shown in the sidebar, indicating how the AI interpreted the original prompt.
3. **Image URL**: Provided in the sidebar for easy downloading or sharing externally.

## Screenshots

[Result](https://github.com/user-attachments/assets/fa8b3e76-086b-4e81-8849-3869b946b8a6)

## Hosted Version

(Add the link to the hosted version of the application here.)

## Video Explanation

(Add a link to a short video explaining the script, how to set it up, and a live demonstration.)

## Additional Notes

- **Customizability**: This app can be easily modified to support batch image generation, allowing users to generate multiple images from different prompts simultaneously.
- **Integration**: You can integrate this script with other AI tools, such as natural language processing or image editing APIs, to create more complex applications.
- **Scalability**: For larger projects, consider deploying this app on a scalable cloud platform to handle higher traffic and more API requests.



## Contact

For questions, feedback, or collaborations, connect with us through Curious PM at [Curious.PM](https://curious.pm).

