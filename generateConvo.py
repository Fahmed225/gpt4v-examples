from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generateConvo(items):
    llm = ChatOpenAI(model="gpt-4-turbo-preview")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Using the items provided, create a conversation between a user and an ai bot. The user query should be an organic question regarding one of the items (pick one that seems most popular). The ai bot should recommend the item in its response. Ensure the ai bot's response uses one of the items from the list provided. The response should be in the form of json for example (note this is just an example. Come up with your own Q/As): {example}"),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain.invoke({"example": "```json\r\n[{\"role\":\"User\",\"message\":\"I've got back pain from driving all day. Is there anything you recommend that can ease my pain a bit?c\"},{\"role\":\"AI\",\"message\":\"response\",\"item\":\"Recommended Item\"}]\r\n```", "input": " Items: " + str(items)})



# example usage
# items = ["shampoo for men", "laptop intel i9", "airpods"]
# convo = generateConvo(items)
# print(convo)