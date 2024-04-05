import json
from gpt4_toner import adjust_tone_of_response

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for ticket in data['tickets']:
        # Extract the conversation messages
        user_message = ticket['conversation'][0]['message']
        assistant_message = ticket['conversation'][1]['message']
        
        # Adjust the tone of the assistant's response using GPT-4
        ticket['conversation'][1]['message'] = adjust_tone_of_response(user_message, assistant_message)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_file_path = 'data/knowledgebase-raw.json'
    output_file_path = 'data/output.json'
    main(input_file_path, output_file_path)
