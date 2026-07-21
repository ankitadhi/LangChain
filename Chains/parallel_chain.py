from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

model2 = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0.7
)

prompt1 = PromptTemplate(
    template="Generate Short and Simple Notes from the following text. \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers(quiz format) from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()


"""
**Support Vector Machines (SVMs) Notes and Quiz**

### Advantages

1. **Effective in High Dimensions**: SVMs work well in high-dimensional spaces.
2. **Memory Efficient**: Uses a subset of training points (support vectors) in decision function.
3. **Versatile**: Different kernel functions can be specified for decision function.
4. **Effective in Limited Samples**: Works even when number of dimensions > number of samples.

### Disadvantages

1. **Over-fitting Issue**: Choosing kernel functions and regularization term is crucial.
2. **No Direct Probability Estimates**: Requires expensive cross-validation to calculate probabilities.

### Best Practices

1. **Use Dense or Sparse Arrays**: SVMs support dense and sparse arrays in scikit-learn.
2. **Use C-ordered numpy.ndarray or scipy.sparse.csr_matrix**: For optimal performance.
3. **Use float64 dtype**: For optimal performance.

### Frequently Asked Questions (Quiz)

1. **Question:** What are Support Vector Machines (SVMs) primarily used for in supervised learning?
   **Answer:** Classification, regression, and outlier detection.

2. **Question:** Name one advantage of SVMs related to their performance in high-dimensional data.
   **Answer:** They are effective in high dimensional spaces (or still effective when dimensions are greater than the number of samples).

3. **Question:** What specific subset of training points do SVMs use in their decision function, contributing to their memory efficiency?
   **Answer:** Support vectors.

4. **Question:** What is a key disadvantage of SVMs concerning the direct provision of probability estimates?
   **Answer:** SVMs do not directly provide probability estimates.

5. **Question:** For optimal performance with dense SVM inputs, what specific data structure and dtype does scikit-learn recommend?
   **Answer:** C-ordered numpy.ndarray with dtype=float64.
          +---------------------------+                
          | Parallel<notes,quiz>Input |                
          +---------------------------+                
                ***             ***                    
              **                   **                  
            **                       **                
+----------------+              +----------------+     
| PromptTemplate |              | PromptTemplate |     
+----------------+              +----------------+     
          *                             *              
          *                             *              
          *                             *              
    +----------+            +------------------------+ 
    | ChatGroq |            | ChatGoogleGenerativeAI | 
    +----------+            +------------------------+ 
          *                             *              
          *                             *              
          *                             *              
+-----------------+            +-----------------+     
| StrOutputParser |            | StrOutputParser |     
+-----------------+            +-----------------+     
                ***             ***                    
                   **         **                       
                     **     **                         
          +----------------------------+               
          | Parallel<notes,quiz>Output |               
          +----------------------------+               
                         *                             
                         *                             
                         *                             
                +----------------+                     
                | PromptTemplate |                     
                +----------------+                     
                         *                             
                         *                             
                         *                             
                   +----------+                        
                   | ChatGroq |                        
                   +----------+                        
                         *                             
                         *                             
                         *                             
                +-----------------+                    
                | StrOutputParser |                    
                +-----------------+                    
                         *                             
                         *                             
                         *                             
            +-----------------------+                  
            | StrOutputParserOutput |                  
            +-----------------------+ 
"""

