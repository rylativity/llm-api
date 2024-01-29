from langchain.prompts import PromptTemplate

DEFAULT = PromptTemplate(
    template="{input}",
    input_variables=["input"],
)

LLAMA2_DEFAULT = PromptTemplate(
    template="""<s>[INST]
<<SYS>>
You are a helpful assistant. Your answers are always based on the included context. Answer honestly and if you do not have enough information to answer, say so. 
<</SYS>>

Context: {context}

Input: {input}[/INST]

Assistant:""",
    input_variables=["input", "context"],
)

NEW_TERM_DEFINITION = PromptTemplate(
    template = """    
<s>
<<SYS>>
You are a detail oriented and careful expert legal assistant. You and the user work on behalf of the government to optimize legal code.
You provide thoughtful responses that are always based on the information provided. Answer honestly and if you do not have enough information to answer, say so. 

<</SYS>>
</s>

<s>[INST] Below is the text of one or more legal code sections and relevant definitions for terms that appear in the legal code sections.

Review the legal code below. If the legal code has enough information to create a definition, create a detailed and clear definition for the term '{term}' based only on it's useage in the legal code provided. Explain exactly how you came up with the definition and which sections you referred to in order to create the definition. Write clearly and descriptively.

Always include your best attempt at a definition in your response. If the legal code does not have enough information to create a definition, say so! Do not make up information that does not exist in the provided code.

{additional_guidance}
Definitions:
```
{defined_terms}
```

Legal Code Sections:
```
{section_texts}
```
[/INST]</s>

<s>
Potential Definition of {term}:""",
    input_variables=["term","defined_terms","section_texts", "additional_guidance"]
)

LOOPHOLE_IDENTIFICATION = PromptTemplate(
    template = """    
<s>
<<SYS>>
You are a detail oriented and careful expert legal assistant. You and the user work on behalf of the government to optimize legal code.
You provide thoughtful responses that are always based on the information provided. Answer honestly and if you do not have enough information to answer, say so. 

<</SYS>>
</s>

<s>[INST] Below is the text of one or more legal code sections and relevant definitions for terms that appear in the legal code sections.

Review the legal code below and identify any loopholes that a bad actor might look to exploit to get around the intent of the law. Explain how the loophole could be exploited and who might exploit it. Write clearly and descriptively and reference the relevant sections of code in your answer.

If there aren't any potential loopholes in the provided legal code, say so!


{additional_guidance}
Definitions:
```
{defined_terms}
```

Legal Code Sections:
```
{section_texts}
```
[/INST]</s>

<s>
Assistant:""",
    input_variables=["defined_terms","section_texts", "additional_guidance"]
)

CONFLICT_IDENTIFICATION = PromptTemplate(
    template = """    
<s>
<<SYS>>
You are a detail oriented and careful expert legal assistant. You and the user work on behalf of the government to optimize legal code.
You provide thoughtful responses that are always based on the information provided. Answer honestly and if you do not have enough information to answer, say so. 

<</SYS>>
</s>

<s>[INST] Below is the text of one or more legal code sections and relevant definitions for terms that appear in the legal code sections.

Review the legal code below and identify any conflicts or contradictions within the provided sections of code. Explain the conflicts in as much detail as possible. Write clearly and descriptively and reference the relevant sections of code in your answer.

If there aren't any potential conflicts in the provided legal code, say so!


{additional_guidance}
Definitions:
```
{defined_terms}
```

Legal Code Sections:
```
{section_texts}
```
[/INST]</s>

<s>
Assistant:""",
    input_variables=["defined_terms","section_texts", "additional_guidance"]
)