import json
import logging
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import PDFReader

# Read input JSON file to get the PDF path and query
with open('input.json', 'r') as file:
    input_data = json.load(file)
    pdf_path = input_data['pdf_path']
    query = input_data['query']

# PDF Reader with SimpleDirectoryReader
parser = PDFReader()
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(pdf_path, file_extractor=file_extractor).load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
logging.basicConfig(level=logging.WARNING)
logging.getLogger('llama_index').setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.ERROR)
logging.getLogger('httpcore').setLevel(logging.ERROR)

Settings.llm = Ollama(model="llama3", request_timeout=360.0)
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

print("\nQuestion: ", query)

try:
    response = query_engine.query(query)
    response_text = str(response)
    print("\nAnswer: ", response_text)
    
    # Write the output to a JSON file
    output_data = {"question": query, "answer": response_text}
    with open('output.json', 'w') as outfile:
        json.dump(output_data, outfile, indent=4)
except Exception as e:
    print(f"Error occurred: {e}")
    # Write the error to the output JSON file
    error_data = {"error": str(e)}
    with open('output.json', 'w') as outfile:
        json.dump(error_data, outfile, indent=4)
