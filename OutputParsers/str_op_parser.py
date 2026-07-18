#An example of detailed and summary without string Output Parser

from langchain_groq import ChatGroq
from dotenv import load_dotenv
# from langchain_core.output_parsers import StringOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

#1st prompt Detailed Report
template1 = PromptTemplate(
    template='Write a detailed report about the {topic}',
    input_variables=['topic']
)


#2nd Prompt Summary of detailed report
template2 = PromptTemplate(
    template='Write a summary of the following report: {report}',
    input_variables=['report']
)

prompt1 = template1.invoke({'topic': 'black hole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'report': result.content})

result2 = model.invoke(prompt2)

print("The results are:\n")
print(f'Detailed Report: {result.content}')
print(f'Summary: {result2.content}')


"""
Detailed Report: **Black Hole Report**

**Introduction**

A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape. It is formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime around it. Black holes are among the most mysterious and fascinating objects in the universe, and their study has led to a deeper understanding of the fundamental laws of physics.

**Formation of a Black Hole**

The formation of a black hole is a complex process that involves the collapse of a massive star. When a star runs out of fuel, it collapses under its own gravity, causing a massive amount of matter to be compressed into an incredibly small space. This compression creates an intense gravitational field that warps the fabric of spacetime around the star, creating a region from which nothing can escape.

**Characteristics of a Black Hole**

Black holes have several key characteristics that make them unique:

1. **Event Horizon**: The point of no return around a black hole is called the event horizon. Once something crosses the event horizon, it is trapped by the black hole's gravity and cannot escape.
2. **Singularity**: The center of a black hole is called a singularity, where the density and gravity are infinite.
3. **Gravitational Pull**: The gravitational pull of a black hole is so strong that it warps the fabric of spacetime around it, creating a gravitational field that is much stronger than anyother object in the universe.
4. **No Radiation**: Black holes do not emit any radiation, making them invisible to our telescopes.

**Types of Black Holes**

There are four types of black holes, each with different properties:

1. **Stellar Black Holes**: These are the smallest and most common type of black hole, formed from the collapse of individual stars.
2. **Intermediate-Mass Black Holes**: These black holes have masses that fall between those ofstellar and supermassive black holes.
3. **Supermassive Black Holes**: These are the largest type of black hole, found at the centers of galaxies, with masses millions or even billions of times that of the sun.
4. **Primordial Black Holes**: These are hypothetical black holes that may have formed in the early universe before the first stars formed.

**Observational Evidence for Black Holes**

Despite their elusive nature, black holes have been detected through their effects on the surrounding environment. Some of the observational evidence for black holes includes:

1. **X-rays and Gamma Rays**: Telescopes have detected X-rays and gamma rays emanating from the vicinity of suspected black holes.
2. **Radio Waves**: Radio telescopes have detected radio waves emitted by matter as it spiralsinto a black hole.
3. **Gravitational Waves**: The detection of gravitational waves by LIGO and VIRGO have provided strong evidence for the existence of black holes.
4. **Star Motions**: Astronomers have observed the motions of stars near suspected black holes, which have been found to be moving at high speeds, indicating the presence of a massive, unseen object.

**Impact of Black Holes on the Universe**

Black holes have a significant impact on the universe, including:

1. **Galaxy Formation**: Supermassive black holes are thought to play a key role in the formation of galaxies.
2. **Star Formation**: The presence of a black hole can affect the formation of stars in a galaxy.
3. **Gravitational Effects**: Black holes warp the fabric of spacetime, creating gravitationaleffects that can affect the motion of nearby objects.
4. **Cosmological Implications**: The existence of black holes has implications for our understanding of the universe, including the possibility of alternative theories of gravity.

**Conclusion**

Black holes are mysterious and fascinating objects that continue to capture the imagination ofscientists and the public alike. Their study has led to a deeper understanding of the fundamental laws of physics and has provided insights into the formation and evolution of the universe.As our understanding of black holes continues to grow, we may uncover new and exciting secretsabout these enigmatic objects.

**References**

* Hawking, S. W. (1974). Black hole explosions? Nature, 248(5443), 30-31.
* Bardeen, J. M., Carter, B., & Hawking, S. W. (1973). The four laws of black hole mechanics. Communications in Mathematical Physics, 31(2), 161-170.
* Bekenstein, J. D. (1973). Black holes and the second law of thermodynamics. Physical Review D, 7(10), 2333-2346.
* LIGO Scientific Collaboration & Virgo Collaboration. (2016). Observation of gravitational waves from a binary black hole merger. Physical Review Letters, 116(6), 061102.
Summary: **Summary of the Black Hole Report**

The Black Hole Report provides an in-depth overview of the mysterious and fascinating objects known as black holes. A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape. It is formed when a massive star collapses in on itself, creating an intense gravitational field that warps the fabric of spacetime.

The report discusses the characteristics of black holes, including:

1. **Event Horizon**: The point of no return around a black hole.
2. **Singularity**: The center of a black hole with infinite density and gravity.
3. **Gravitational Pull**: The strongest gravitational field in the universe.
4. **No Radiation**: Black holes do not emit any radiation, making them invisible to our telescopes.

The report also explores the different types of black holes, including:

1. **Stellar Black Holes**: The smallest and most common type, formed from the collapse of individual stars.
2. **Intermediate-Mass Black Holes**: Black holes with masses between stellar and supermassiveblack holes.
3. **Supermassive Black Holes**: The largest type, found at the centers of galaxies, with masses millions or even billions of times that of the sun.
4. **Primordial Black Holes**: Hypothetical black holes that may have formed in the early universe.

The report also discusses the observational evidence for black holes, including:

1. **X-rays and Gamma Rays**: Telescopes have detected X-rays and gamma rays emanating from the vicinity of suspected black holes.
2. **Radio Waves**: Radio telescopes have detected radio waves emitted by matter as it spiralsinto a black hole.
3. **Gravitational Waves**: The detection of gravitational waves by LIGO and VIRGO have provided strong evidence for the existence of black holes.
4. **Star Motions**: Astronomers have observed the motions of stars near suspected black holes, which have been found to be moving at high speeds, indicating the presence of a massive, unseen object.

The report concludes that black holes have a significant impact on the universe, including:

1. **Galaxy Formation**: Supermassive black holes are thought to play a key role in the formation of galaxies.
2. **Star Formation**: The presence of a black hole can affect the formation of stars in a galaxy.
3. **Gravitational Effects**: Black holes warp the fabric of spacetime, creating gravitationaleffects that can affect the motion of nearby objects.
4. **Cosmological Implications**: The existence of black holes has implications for our understanding of the universe, including the possibility of alternative theories of gravity.

Overall, the Black Hole Report provides a comprehensive overview of the fascinating and mysterious objects known as black holes, and highlights the significance of their study in advancing our understanding of the universe.
"""
