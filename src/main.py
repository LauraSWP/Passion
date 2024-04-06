import threading
import sys
import time
import json
import os
import glob
from gpt4_toner import adjust_tone_of_responses

# List of ANSI color codes
GREEN_TEXT = '\033[92m'
COLORS = ['\033[91m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
RESET_TEXT = '\033[0m'

# Technician's name
technician_name = 'Star'

def load_json_file(file_path):
    """Load and return the content of a JSON file.

    If the file is not a valid JSON, print an error message and exit.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print_with_delay(f"⊙︿⊙ Ups el formato de tu JSON no es correcto, revisalo usando un validador online {file_path}: {e.msg}")
        sys.exit(1)  # Exit the script with an error code

def print_with_delay(message, delay=1, color=GREEN_TEXT):
    """Print a message with a delay for readability, in a given color."""
    time.sleep(delay)
    print(color + message + RESET_TEXT)

def loading_animation(event):
    """Display a colorful loading animation."""
    faces = ["(ﾉ・ω・)ﾉ♫♩", "ヽ(・ω・ヽ)♬", "ヽ(*・ω・)ﾉ"]
    index = 0
    while not event.is_set():  # Continue until the event is set
        color_code = COLORS[index % len(COLORS)]
        sys.stdout.write("\r" + color_code + faces[index % len(faces)] + RESET_TEXT)
        sys.stdout.flush()
        time.sleep(0.2)
        index += 1
    sys.stdout.write("\r" + " " * 20 + "\r")  # Clear the line

def get_next_batch_number(tech_name):
    """Get the next batch number based on existing files."""
    existing_batches = glob.glob(f'data/output-batch-{tech_name.lower()}-*.json')
    existing_numbers = [int(batch.split('-')[-1].split('.')[0]) for batch in existing_batches]
    next_number = max(existing_numbers) + 1 if existing_numbers else 1
    return f"{next_number:02d}"

def main(input_file_path, output_file_path_template, tech_name):
    data = load_json_file(input_file_path)
    print_with_delay(f"~(˘▾˘)~ Hola, {tech_name}! Veo que la de trabajar te la sabes 🎉 Vamos a procesar esos datos ricos...(づ｡◕‿‿◕｡)づ", 1)
    print_with_delay("◃┆◉◡◉┆▷ Formateando el ordenador y eliminando todos tus datos... (≖‿≖) Es broma JKJJKJKJSJSJ, estoy conectando con OpenAI 😉)", 1)

    event = threading.Event()
    load_thread = threading.Thread(target=loading_animation, args=(event,))
    load_thread.start()

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            new_tickets_data = json.load(file)['tickets']

        # Process each new ticket and add reply alternatives
        for ticket in new_tickets_data:
            user_message = ticket['conversation'][0]['message']
            reply_alternatives = adjust_tone_of_responses(user_message, num_replies=5)
            ticket['conversation'][1]['message'] = reply_alternatives

    except Exception as e:
        print("\nOcurrió un error: ", e)
        raise
    finally:
        event.set()
        load_thread.join()

    batch_number = get_next_batch_number(tech_name)
    output_file_path = output_file_path_template.format(tech_name=tech_name.lower(), batch_number=batch_number)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump({"tickets": new_tickets_data}, file, indent=4, ensure_ascii=False)

    print_with_delay("¡Listo! Datos guardados en " + output_file_path + "! 📦✨", 1)

    with open(input_file_path, 'r+', encoding='utf-8') as file:
        data = file.read()
        file.seek(0)
        file.truncate()

    with open('data/knowledgebase-raw-archive.json', 'a', encoding='utf-8') as file:
        file.write(data)

    print_with_delay("Listo (*˘︶˘*), he archivado el raw data al archivo de raw-archive! Duh ahahajkjkjsjs 📚 Todo listo, ya puedes ir a luchar por la DEMOCRACIA ( ಠ◡ಠ ), o procesar mas datos.", 1)

if __name__ == "__main__":
    input_path = 'data/knowledgebase-raw.json'
    output_path_template = 'data/output-batch-{tech_name}-{batch_number}.json'
    main(input_path, output_path_template, technician_name)