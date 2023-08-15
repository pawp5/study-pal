import os
import sys

# import for database gpt
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

# import for doc and web prompt
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
from . import constants

os.environ['OPENAI_API_KEY'] = constants.APIKEY

# query = sys.argv[1]

def db_response(query):
    db = SQLDatabase.from_uri("sqlite:///db.sqlite3")
    llm = ChatOpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

    return db_chain.run(query)





def gpt_response(query):
    global chat_history

    # check if response is gotten from database prompt
    db_result = db_response(query)

    # Enable to save to disk & reuse the model (for repeated queries on the same data)
    PERSIST = False

    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        loader = TextLoader("Dept/age.txt") # Use this line if you only need data.txt
        # loader = DirectoryLoader("Dept/")
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    if query in ['quit', 'q', 'exit']:
        sys.exit()
    result = chain({"question": query, "chat_history": chat_history, "db_result": db_result})
    chat_history.append((query, result['answer']))
    return result['answer']


chat_history = []




# loader = TextLoader("Dept/age.txt")
# index = VectorstoreIndexCreator().from_loaders([loader])
# print(index.query(query, llm=ChatOpenAI))

# chat_history = []
# while True:
#     if not query:
#         query = input("Prompt: ")
#     if query in ['quit', 'q', 'exit']:
#         sys.exit()
#     result = chain({"question": query, "chat_history": chat_history})
#     chat_history.append((query, result['answer']))
#     query = None
#     return result['answer']

