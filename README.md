This project is a POC for SparkIl. The main goal is to prepare the email subject and body, which are then sent as an update email to the business landers by another process. 
The script utilizes OpenAI's API to generate the content
the current results are saved in an RTF file format for testing.



# Email Content Generator

This repository contains a Python script designed to generate email content using OpenAI's API and save the output in an RTF file format. The script reads system instructions from a file, processes user inputs, and generates well-formatted email content based on the provided prompts.

## Features

- **Generate Email Content**: The script uses OpenAI's API to create email content, including the subject and body text.
- **Customizable System Instructions**: System instructions are read from a file, allowing for flexible and reusable templates.
- **Save to RTF**: The generated email content is saved in RTF format, with the filename including the business name and the current date and time.
- **Reliability Checks**: Flags are included to determine if the content is reliable or if it may be perceived as too sad.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/email-content-generator.git
    ```
2. **Install dependencies**:
    Make sure you have `pydantic` and `openai` installed:
    ```bash
    pip install pydantic openai
    ```

## Usage

1. to use it you should have a file with the information about the busines here: ../InputFiles/filename.txt and questions and answers here ""../InputFiles/filename.txt"

2. **Run the Script**:
    Use the following command to run the script:
    ```bash
    python main_2.py
    ```

3. **Generated Output**:
    The generated email content will be saved in the `outputFiles` directory, with the filename containing the business name and the current timestamp.

## Configuration

- **OpenAI API Key**: Ensure your OpenAI API key is properly configured in your environment or within the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



## Contact

For any questions or support, feel free to reach out to [avim@pulsetech.ai).

