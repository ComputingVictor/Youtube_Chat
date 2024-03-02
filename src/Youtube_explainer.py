from langchain_community.llms import Ollama
from langchain import PromptTemplate
from langchain.chains import LLMChain
from googletrans import Translator

# Crear instancia de Ollama
llm = Ollama(model="llama2")

from langchain_core.prompts import ChatPromptTemplate

# Función para crear la base de datos a partir de la URL de un video de YouTube
def create_db_from_youtube_video_url(video_url: str):
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=True,
        language=["es", "id"]
    )
    db = loader.load()
    return db

# Función para obtener la respuesta a partir de una consulta en la base de datos
def get_response_from_query(db, query, k=4):
    """
    text-davinci-003 can handle up to 4097 tokens. Setting the chunksize to 1000 and k to 4 maximizes
    the number of tokens to analyze.
    """

    llm = Ollama(model="llama2")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        Eres un asistente útil que responde solo en español y que puede responder preguntas sobre videos de YouTube 
        basado en la transcripción del video.
        
        Responde la siguiente pregunta: {question}
        Buscando en la transcripción del siguiente video: {docs}
        
        Utiliza únicamente la información factual de la transcripción para responder la pregunta.
        
        Si sientes que no tienes suficiente información para responder la pregunta, di "No lo sé".
        
        Tus respuestas deben ser detalladas y completas.
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=db)
    response = response.replace("\n", "")
    return response, db

# Función para traducir texto a un idioma especificado
def translate_text(text, target_language='es'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# URL del video de YouTube
video_url = "https://www.youtube.com/watch?v=vqfooev8RNQ&t=620s"
# Crear la base de datos a partir de la URL del video
db = create_db_from_youtube_video_url(video_url)

# Bucle principal para interactuar con el chatbot
while True:
    # Solicitar al usuario que ingrese una pregunta
    query = input("Ingrese su pregunta (o escriba 'salir' para terminar): ")
    
    # Verificar si el usuario quiere salir del bucle
    if query.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    # Obtener la respuesta del chatbot
    response, docs = get_response_from_query(db, query)
    # Traducir la respuesta al español
    response_translated = translate_text(response)
    # Imprimir la respuesta traducida
    print("Respuesta:", response_translated)
