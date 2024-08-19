from pydantic import BaseModel
from openai import OpenAI
import os

#print(os.getenv("OPENAI_API_KEY"))
systemContent=""
userContent=""
questionsAndAnswers = ""
client = OpenAI()

def prepareMessages(fileName):
    # Read system instructions from a file
    with open(fileName, "r") as file:
        fileData = file.read()
        return fileData

class EmailOutput(BaseModel):
    emailSubject: str
    messageText: str
    isReliable: bool
    businessName: str
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

        print("Email Subject:", emailText.emailSubject)
        print("Message Text:", emailText.messageText)
        print("Is Reliable:", emailText.isReliable)
        print("Business Name:", emailText.businessName)

        #print(emailText)
        #print(completion.choices[0].message.parsed.dict())
    except Exception as e:
        print(e)
        print("failed to get response")
        pass



if __name__ == "__main__":
    main()
