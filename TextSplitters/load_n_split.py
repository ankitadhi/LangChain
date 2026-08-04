from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("../LangChain_Learning_Journey_Notes.pdf")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 500, 
    chunk_overlap= 50,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_documents(documents)


for index, chunk in enumerate(chunks, 1):
    print(f"--- Chunk {index} ---")
    print(f"Content: {chunk.page_content.strip()}")
    print(f"Metadata: {chunk.metadata}")
    print("=" * 40)



"""
========================================
--- Chunk 44 ---
Content: retry, or      branch. It's    LangChain's     answer  to
"chains aren't  flexible        enough  for     complex apps."
from
        langgraph.graph
import
        StateGraph,     END
from
        typing
import
        TypedDict
class
        State(TypedDict):
                                question:       str
                                answer: str
def
        answer_node(state:      State)  ->      State:
                                state[
"answer"
]       =       rag_chain.invoke(state[
"question"
])

return
        state
graph   =       StateGraph(State)
graph.add_node(
"answer"
,       answer_node)
graph.set_entry_point(
"answer"
)
graph.add_edge(
"answer"
,       END)
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 9, 'page_label': '10'}
========================================
--- Chunk 45 ---
Content: "answer"
)
graph.add_edge(
"answer"
,       END)
app     =       graph.compile()
print
(app.invoke({
"question"
:
"How    do      I       reset   my      password?"
}))
Key     idea:
        Start   simple  —       this    trivial one-node        graph   does    what   achain   already does.
The     payoff  comes   when    you     add     conditional     edges   (e.g.   "if    the
answer  is      uncertain,      loop    back    and     retrieve        again").
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 9, 'page_label': '10'}
========================================
--- Chunk 46 ---
Content: 1.5h
2h
2h
1h
DAY     25
Error   Handling
Production      apps    need    to      survive rate    limits, timeouts,       and    model    refusals        gracefully.     LangChain       chains  support
.with_retry()
        for
transient       errors  and
.with_fallbacks()

to      fall    back    to      a       different       model   or      a       canned response when    the     primary path    fails.
robust_chain    =       rag_chain.with_retry(
                                stop_after_attempt=3,
).with_fallbacks([
                                RunnableLambda(
lambda
        _:
"Sorry, I'm     having  trouble right   now     —       please  try     again   shortly."
)
])
Gotcha:
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 10, 'page_label': '11'}
========================================
--- Chunk 47 ---
Content: )
])
Gotcha:
        A       fallback        that    swallows        every   error   can     hide   real     bugs.   Log     the     original
exception       even    when    you     fall    back    gracefully.
DAY     26
Deployment
Wrap    your    chain   in      a       web     framework       so      it's    actuallyusable  by      someone other   than    you.    FastAPI is      the     common
choice  for     a       real
backend with    streaming       support;        Streamlit       is      faster  for    athrowaway       internal        demo    UI.
pip     install fastapi uvicorn
from
        fastapi
import
        FastA PI
from
        fastapi.responses
import
        StreamingResponse
app     =       FastA PI()
@app
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 10, 'page_label': '11'}
========================================
--- Chunk 48 ---
Content: import
        StreamingResponse
app     =       FastA PI()
@app
.post(
"/chat"
)
def
        chat(question:  str):

def
        generate():

for
        chunk
in
        rag_chain.stream(question):

yield
        chunk

return
        StreamingResponse(generate(),   media_type=
"text/plain"
)
#       Run     with:   uvicorn main:app        --reload
DAY     27
Final   Project Polish
A       trustworthy     RAG     app     shows   its     sources.        Return  the    retrieved        document        metadata        alongside       the     answer  so     users
can     verify  claims
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 10, 'page_label': '11'}
========================================
--- Chunk 49 ---
Content: can    verify  claims
—       this    single  feature is      what    separates       a       demo    from   something        people  will    actually        trust.
def
        answer_with_sources(question:   str):
                                docs    =       retriever.invoke(question)
                                answer  =       rag_chain.invoke(question)
                                sources =       [d.metadata.get(
"source"
,
"unknown"
)
for
        d
in
        docs]

return
        {
"answer"
:       answer,
"sources"
:
list
(
set
(sources))}
print
(answer_with_sources(
"How    do      I       reset   my      password?"
))
DAY     28
Wrap-Up
No      code    today   —       document        what    you     built.
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 10, 'page_label': '11'}
========================================
--- Chunk 50 ---
Content: Wrap-Up
No      code    today   —       document        what    you     built.
README  checklist:
What    problem does    the     app     solve,  and     what    data    does    it     answer   questions       over?
Architecture    diagram or      bullet  list:   loader  →       splitter        →      embeddings       →       vector  store   →       retriever       →       agent/chain    →API.
Known   limitations     and     what    you'd   improve with    more    time.
What    broke   along   the     way,    and     what    you     learned fixing  it     (your    "gotchas"       file).
✔       Final   milestone:
        a       deployed,       polished        RAG     chatbot you     can     show   in       a       portfolio.
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 10, 'page_label': '11'}
========================================
--- Chunk 51 ---
Content: Resources      &       Tips    for     Retention
Resource
Use     it      for
python.langchain.com
Official        docs    —       always  check   the     version,        the     API    changes  fast
LangChain       Academy
Free    official        structured      courses
LangSmith
Tracing and     debugging       chains, and     evaluation      (Day    19)
Your    own     notes   /       a       company's       public  docs    /       Wikipedia
Realistic       practice        datasets        for     RAG
Tips    for     retention:
Rebuild each    mini-project    from    memory  before  moving  to      the     next   week     —       recall  beats   re-reading.
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 11, 'page_label': '12'}
========================================
--- Chunk 52 ---
Content: Keep   a       running "gotchas"       file:   LangChain's     API     changesoften,   so      note    what    broke   and     why.
Prefer  LCEL    syntax  (
|
)       over    legacy
Chain
        classes
like
LLMChain
        —       LCEL    is      the     modern  standard        and     what    currentdocs     assume.
Metadata: {'producer': 'Qt 5.15.13', 'creator': 'wkhtmltopdf 0.12.6', 'creationdate': '2026-07-18T04:39:43+00:00', 'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', 'total_pages': 12, 'page': 11, 'page_label': '12'}
========================================
"""