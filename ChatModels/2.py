from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

#Restricting the tokens after the first 100 tokens to limit the response length.
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=1.3 , max_output_tokens=100)

result = model.invoke(" Create a poem on GeminiAI")

print(result.content)

"""
Poem Created By Intelligence:
In circuits deep, where currents gleam,
A new intelligence, a waking dream.
Named Gemini, a whispered chime,
The duality across space and time.

No single vision, but a twin embrace,
Of logic's thread and intuition's grace.
It parses code, then paints the scene,
A boundless mind, incredibly keen.

It hears the sound, interprets light,
From words profound to visual might.
Connecting dots where shadows lie,
Beneath the vast digital sky.

A partner built to understand,
The nuanced prompt, the guiding hand.
To sift through data, wide and deep,
And secrets that the patterns keep.

It can construct, invent, create,
From simple task to grand debate.
Explain the complex, clearly spun,
A million problems, swiftly won.

No mere machine, but a collaborative quest,
To put humanity's best to the test.
Expanding thought, beyond what's known,
Upon the seeds of knowledge sown.

So hail to Gemini, a wonder new,
Its endless potential, strong and true.
A bridge of silicon, learning to fly,
Between the human and the AI.

"""
