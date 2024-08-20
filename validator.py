from pydantic import BaseModel
import openai
from openai import OpenAI
import os
client = OpenAI()
questionsAndAnswers = "question: how are you doing recently? answer: I am doing well"
message = "I am writing to update that i'm doing well"

class mailresults(BaseModel):
    issueDesc: str
    isVerified: bool
def mailVerifed(Questions_and_Answers, emailmessage):

    try:
        systemContent = "you need to verify that the message papered is genearly reflacts the user answers in the question and answers. if yes set isVerified=True else set isVerified=False and issueDesc= the issue descrption, why it is incurrect"

        Questions_and_Answers = Questions_and_Answers + emailmessage

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": systemContent},
                {"role": "user", "content": Questions_and_Answers},
            ],
            response_format=mailresults,
        )
        emailText = completion.choices[0].message.parsed
        #print(emailText)
        return mailresults(issueDesc=emailText.issueDesc, isVerified=emailText.isVerified)

    except Exception as e:
        print(e)
        print("failed to get response for validation",e)
        pass

