from extractor.book import Book
from langchain_community.retrievers import TavilySearchAPIRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import os
import logging




class YearFinder:
    
    def find_year(self, book: Book) -> str:
        logging.basicConfig(level=logging.DEBUG)
        
        retriever = TavilySearchAPIRetriever(k=3, include_generated_answer=False, include_raw_content=False)
        
        # result = retriever.invoke("What is the publishing year of the book " + book.title + " by " + book.author + "? Answer with the year only.")
        
        # logging.debug(result)
        # 
        # return result[0].page_content
        
        prompt_template = ChatPromptTemplate.from_template(
            "Answer the question based only on the context provided.\n"
            "Context: {context}\n"
            "Question: {question}"
        )

        llm = ChatOpenAI(model=os.environ.get("OPENAI_MODEL"))

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        retriever_query = f"Publication date of the book '{book.title}' by {book.author}"
        llm_question = (f"What is the publication year of the book '{book.title}' by {book.author}? "
                        f"Answer with the year only. If the year is not available, answer with 'N/A'.")
        chain = (
                {"context": retriever | format_docs, "question": lambda _: llm_question}
                | prompt_template
                | llm
                | StrOutputParser()
        )

        result = chain.invoke(retriever_query)
        print("YearFinder result: ", result)

        return result
    
    
