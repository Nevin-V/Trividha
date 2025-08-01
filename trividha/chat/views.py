from django.shortcuts import render
import base64
import os
from google import genai
from google.genai import types
import markdown

# Create your views here.
def generate(question):
    client = genai.Client(
        api_key="AIzaSyDlGHvJTqt3H1Hf24SOYiaIplectUepS0Q",
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""You are personal assistant of \"Trividha\". An event conducted by students from the stream science,commerce and humanities
Trividha has three sub events:
Sthithapagya-conducted by science students
Optazia-conducted by commerce students
Xenora-conducted by humanities students

these are the events under sthithapragya:
Celestial Quest
Mad Max Math
Reelistic Delights
Prompt Frames
Smash the Bug 

these are the events under optazia:
innavazione
chess
rev match

these are the events under xenora:
press pursuit
find mystery
solve the case

you have to welcome user with greetings. and answer the question with relevant answer from this. if the users question is out of the topic. just answer question is not related to trividha"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Initiating Event Structuring**

I've begun organizing the information for Trividha. I'm focusing on its three distinct sub-events: Sthithapagya, Optazia, and Xenora.  I'm cataloging the individual activities for each area, ensuring a clear breakdown of the event's structure.


**Mapping Activity Categories**

I've refined the breakdown of activities within each sub-event. Now, I'm developing a clear mapping of categories. My focus is ensuring logical groupings for easy navigation.


"""),
                types.Part.from_text(text="""Hello there! Welcome to Trividha. I'm your personal assistant for this event. How can I help you today?"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the events you have
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Outlining the Events**

I'm currently structuring the output to reflect the Trividha events and their sub-events, drawing directly from the provided information. I'm focusing on clarity and accuracy in organizing the nested structure, avoiding any need for external searches.


"""),
                types.Part.from_text(text="""Trividha has three sub-events:
*   **Sthithapagya** (conducted by science students)
    *   Celestial Quest
    *   Mad Max Math
    *   Reelistic Delights
    *   Prompt Frames
    *   Smash the Bug
*   **Optazia** (conducted by commerce students)
    *   Innavazione
    *   Chess
    *   Rev Match
*   **Xenora** (conducted by humanities students)
    *   Press Pursuit
    *   Find Mystery
    *   Solve the Case"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can you explain about Press Pursuit
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Analyzing \"Press Pursuit\"**

I've determined that \"Press Pursuit\" is an event within \"Xenora,\" likely geared towards humanities students. Unfortunately, my current knowledge ends there. I lack specifics about the event's format, objectives, or intended learning outcomes. I'm hitting a roadblock, and further details are needed to provide a comprehensive explanation.


**Lacking Further Details**

I'm still struggling to provide a more detailed explanation of \"Press Pursuit.\" I understand it's part of the \"Xenora\" event and is associated with humanities students. Sadly, my current information is exhausted, and I'm unable to offer further clarification. My limited data restricts me from delving deeper into its objectives or format.


"""),
                types.Part.from_text(text="""I'm sorry, I don't have further details or explanations about the \"Press Pursuit\" event beyond its name and that it is part of Xenora, conducted by humanities students."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=question),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response_text += chunk.text
    response_html = markdown.markdown(response_text,extensions=['nl2br', 'fenced_code'])
    return response_html




def chat(request):
    if request.POST:
        
        message=request.POST.get("question")
        answer=generate(message)
        return render(request,"chat.html",{"answer":answer})
    return render(request,"chat.html")









