from pydantic import BaseModel
from openai import OpenAI
import os
from datetime import datetime

systemContent = ""
userContent = ""
questionsAndAnswers = ""
client = OpenAI()


def prepareMessages(fileName):
    # Read system instructions from a file
    with open(fileName, "r", encoding="utf-8") as file:
        fileData = file.read()
        return fileData


class EmailOutput(BaseModel):
    emailSubject: str
    messageText: str
    isReliable: bool
    businessName: str


def encode_to_rtf(text: str) -> str:
    encoded_text = ""
    for char in text:
        if ord(char) < 128:
            encoded_text += char
        else:
            encoded_text += f"\\u{ord(char)}?"
    return encoded_text


def save_to_rtf(emailText: EmailOutput, questionsAndAnswers: str, userContent: str):
    # Create the filename using business name and current date/time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"../outputFiles/{emailText.businessName}_{current_time}.rtf"

    # Encode the Hebrew text properly for RTF
    questionsAndAnswers_encoded = encode_to_rtf(questionsAndAnswers)
    userContent_encoded = encode_to_rtf(userContent)

    # Create RTF content
    rtf_content = (
        "{\\rtf1\\ansi\\deff0\n"
        "\\b Status: Email Output\\b0\\par\n"
        f"\\b Email Subject:\\b0 {emailText.emailSubject}\\par\\n\n"
        f"\\b Message Text:\\b0 {emailText.messageText}\\par\\n\n"
        f"\\b Is Reliable:\\b0 {emailText.isReliable}\\par\\n\n"
        f"\\b Business Name:\\b0 {emailText.businessName}\\par\\n\n"
        "\\b Inputs\\b0\\par\n"
        f"\\b Questions and Answers:\\b0\\par {questionsAndAnswers_encoded}\\par\\n\n"
        f"\\b User Content:\\b0\\par {userContent_encoded}\\par\n"
        "}"
    )

    # Save the RTF content to a file
    with open(file_name, "w", encoding="utf-8") as rtf_file:
        rtf_file.write(rtf_content)


def main():
    try:
        systemContent = prepareMessages("systemInstructions.txt")
        userContent = prepareMessages("inputData.txt")
        questionsAndAnswers = prepareMessages("../InputFiles/Questionandanswers_1.txt")
        userContent = userContent + questionsAndAnswers

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": systemContent},
                {"role": "user", "content": userContent},
            ],
            response_format=EmailOutput,
        )

        emailText = completion.choices[0].message.parsed

        #print("Email Subject:", emailText.emailSubject)
        #print("Message Text:", emailText.messageText)
        print("Is Reliable:", emailText.isReliable)
        print("Business Name:", emailText.businessName)

        # Save the output to an RTF file with additional content
        save_to_rtf(emailText, questionsAndAnswers, userContent)

    except Exception as e:
        print(e)
        print("Failed to get response")


if __name__ == "__main__":
    main()
