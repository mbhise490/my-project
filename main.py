from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

def main():
    print("Hello from project01!")
    information="""Elon Musk is one of the most influential and controversial entrepreneurs of the 21st century, known for pushing the boundaries of technology and innovation. Born on June 28, 1971, in Pretoria, South Africa, he showed an early interest in computers and entrepreneurship, creating and selling a video game at the age of 12."""

    summary_template = '''given the information {information} about a person I want you to create: \
    1. A short summary," \
    2. Two interesting facts,'''

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0)

    chain=summary_prompt_template | llm
    response = chain.invoke({'information': information})
    print(response.content)



    

if __name__ == "__main__":
    main()
