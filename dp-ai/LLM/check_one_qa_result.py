'''
질문->검색->응답
'''
#!pip install -qU pypdf langchain_community langchain-openai langchain_huggingface transformers langchain_anthropic faiss-gpu
#!pip install -qU bitsandbytes

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


model_name = "BAAI/bge-m3"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf_embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

vectorstore = FAISS.load_local(
    "/content", hf_embeddings, "faiss_index", allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={'k': 5}
)

from langchain_anthropic import ChatAnthropic
# Anthropic API 키와 LLM 설정
ANTHROPIC_API_KEY = ""

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
    api_key=ANTHROPIC_API_KEY,
)

prompt_template = """
### [INST]
당신은 인플루언서를 추천하는 어시스턴스입니다. 주어진 정보를 기반으로 한국어로 성실하게 대답해주세요.
인플루언서 추천 시 가능하면 여러 명을 추천해야 하며, 답변은 아래의 형태로 해주세요.
1. 인플루언서 이름(id:<username>)
추천 이유 기술.
답변은 주어진 정보가 근거가 되어야 하고, 근거를 답변에 포함해 주세요.
주어진 정보로 질문에 답변을 하기 충분하지 않다면, "제가 가지고 있는 정보로는 답변이 어려울 것 같습니다."라고 대답해 주세요.
### 사용자의 질문:
{question}
### 주어진 정보:
{context}
[/INST]
"""

# Create prompt from prompt template
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)

# RAG 체인 구성
rag_chain = (
        RunnableMap({
            "context": retriever,
            "question": RunnablePassthrough()
        })
        | prompt
        | llm
)

def get_response(question):
    result = rag_chain.invoke(question)
    return result.content

result = get_response("쿠션 광고하기 좋은 인플루언서 알려줘")
print(result)