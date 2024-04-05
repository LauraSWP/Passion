# FineTune Passion Training data for ADA 0.1

Scripts and datasets that mixes manual to AI techniques to fine tune a data set for AI training  purposes.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.8 or higher recommended)
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/)

## Setup

### Cloning the Repository

Using Visual Studio Code you can clone the repository directly from the home screen.

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
.\venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the script

Before running the script, make sure you prepared your data before. With your new branch, work on the raw data JSON at knowledgebase-raw.json including the question, answer, category and human required fields as the previous entries.
Once this is done, run the main.py script to create a new finetuned file, this script basically asks our assistant to transform the replies to replies using this tone.

When this is done, commit your changes to your branch, I will merge them into the final training file each time.

```bash
python src/main.py
```

### IMPORTANT

Read the answers, it's important that the assistant replies don't include things the assistant can't actually do, such as:
- Refunds
- Checking an app, account or anything external
- Fixing or checking a bug status
- Resetting a password

When this type of situations happen, the assisstant should reply something like "I will transfer you to an agent that can check this for you", so in this case, replace the answer with something like this BEFORE running the script.

### DONE?

- Commit your changes to your branch.
- Push the changes to the remote repository.
- Open a pull request for the changes to be reviewed and merged into the main branch.