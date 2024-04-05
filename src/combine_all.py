import json
import glob

def combine_batches():
    print("Combining all batch files from our awesome technicians! 🛠️")

    # Find all batch files
    batch_files = glob.glob('data/output-batch-*.json')
    combined_data = []

    # Load data from each batch file
    for batch_file in batch_files:
        with open(batch_file, 'r', encoding='utf-8') as file:
            batch_data = json.load(file)['tickets']
            combined_data.extend(batch_data)

    # Generate the final training version file name
    existing_versions = glob.glob('data/final-training-version-*.json')
    existing_numbers = [int(version.split('-')[-1].split('.')[0]) for version in existing_versions]
    next_version_number = max(existing_numbers) + 1 if existing_numbers else 1
    final_file_path = f"data/final-training-version-{next_version_number:02d}.json"
    
    # Write combined data to the final training version file
    with open(final_file_path, 'w', encoding='utf-8') as file:
        json.dump({"tickets": combined_data}, file, indent=4, ensure_ascii=False)
    
    print(f"All data has been successfully combined into {final_file_path}! 🎉")

if __name__ == "__main__":
    combine_batches()
