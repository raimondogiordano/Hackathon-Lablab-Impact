import openai

def improve_text(text):
    openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key
    prompt = "Improve the following text:\n\n" + text + "\n\nImproved text:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        temperature=0.8,
        n=1,
        stop=None,
        timeout=5
    )
    improved_text = response.choices[0].text.strip()
    return improved_text

    def label_and_generate_tags(text):
        openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key
        prompt = "Label and generate tags for the following text:\n\n" + text + "\n\nTags:"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.8,
            n=1,
            stop=None,
            timeout=5
        )
        tags = response.choices[0].text.strip()
        return tags