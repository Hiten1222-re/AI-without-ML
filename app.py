# from openai import OpenAI
import os

from dotenv import load_dotenv
from groq import Groq
import  streamlit as st

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def generate_milestone(task_description):
    # prompt= f''''Break down the following tasks into smaller milestones:
    # \n\nTask:
    # {task_description}
    # \n\n step or milestones: '''


    prompt= f''''Give in simple and elobrated manner
    {task_description}
    \n\n '''

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",

                    #  "content":"You are a super knowledgeable, kind, super fun teacher who teaches everyone like a kid in super simple manner"
                     "content":"You are a super knowledgeable, hilarous, AI who explain everthing in steps in simple language."
                    # "content": "You are a efficient task-driven and successful person. You have helped millions of people to be more productive and able to accomplish their most important goals and milestones in their life in simpler and deeper and detailed way. "

                },
                {

                    "role": "user",
                     "content": f"\n\n{prompt} ",
                    # "content":  " \n\n{prompt} ",

                }
            ],
            model="gemma2-9b-it",
            stream=False,

        )

        # print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content
    except Exception as e: return f'an error occure here---> \n {e}'

def app_console():
    print('****** Welcome to Task And Milestone Generator ******')
    task_description = input('Enter the task you would like to breakdown: ')
    if task_description:
        print('Generating milestone... ')

        milestone  = generate_milestone(task_description)
        if milestone:
            print(milestone)

        else:print('Failed to generate milestone')
    else:print('Error getting task description ')

def main():
    # app_console()
    streamlit_app()

def streamlit_app():
    st.title("My chota Chatgpt 🤖")
    task_description = st.text_area("Enter the task you wish to be guided for:")
    if st.button('Generate...  ♪(´▽｀) '):
        if task_description:
            milestones = generate_milestone(task_description)
            st.markdown(" ============= Milestones / Steps:: =============")
            st.write(milestones)
        else:
            st.write('( ͠° ͟ʖ ͡°) Did you seriously clicked generate without any text ...？')

main()