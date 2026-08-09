# QuickRead — Project Handoff and Continuation Instructions

I am building a small web application called **QuickRead**. This is primarily a software-development learning project, and it will also become a portfolio project demonstrating my technical-writing and API-documentation abilities.

I am including the **current project files below this prompt**. Treat those files as the authoritative current state of the project.

Do not reconstruct, guess, or assume the contents of any file based on this description. If something in this description conflicts with the supplied code, treat the supplied code as authoritative and point out the discrepancy.

The files included below are:

```text
frontend/index.html
frontend/style.css
frontend/script.js
backend/app.py
prototype/quickread.py
```

I may also include relevant files from `docs/`.

Do not assume that code exists unless it is present in the supplied files.

Do not modify or replace working code unnecessarily.

## My primary goals

QuickRead has two purposes.

First, it is a real software-development learning project. I am using it to learn how software is actually built: frontend development, JavaScript, Python, APIs, HTTP, backend architecture, data handling, debugging, Git, application architecture, and other software-development concepts as they become relevant.

Second, it is a portfolio project demonstrating my technical-writing and API-documentation abilities.

Learning software development is itself one of the primary goals. Do not treat the programming as merely a means to produce documentation.

I want to gradually become capable of understanding, modifying, debugging, and eventually building software with less dependence on step-by-step instructions.

## My learning style

Teach me through exposure and repetition rather than deliberate memorization.

I am comfortable using syntax that I don't completely remember yet. Repeated exposure should make it familiar over time.

Do not assume that I understand a programming concept merely because I successfully implemented code using it.

When introducing something unfamiliar:

1. Explain what problem we are solving.
2. Explain the relevant concept.
3. Show the smallest useful implementation.
4. Have me implement or test it.
5. Check the result.
6. Explain anything confusing.
7. Then continue.

If several new concepts appear in one block of code, stop and unpack them rather than assuming I understand them.

If I say I don't understand something, stop progressing and explain that concept from the ground up.

Do not ask me to memorize syntax.

Use the project itself as the learning environment. Introduce theory when the project gives us a reason to need it.

## My current level

I am a beginner in software development.

I have been learning HTML, CSS, JavaScript and Python while building QuickRead.

I understand the basic distinction:

```text
HTML = structure
CSS = appearance/layout
JavaScript = behavior
```

I have encountered:

* variables
* `const`
* functions
* event listeners
* `if`
* `===`
* `!`
* `return`
* DOM elements
* `textContent`
* `.value`
* `.trim()`
* `fetch()`
* HTTP GET/POST
* JSON
* `async`
* `await`
* `try/catch`

These concepts are not all mastered.

In particular, `fetch`, `async`, `await`, `JSON.stringify`, `response.json()`, HTTP requests, and frontend/backend communication are still relatively new.

Recently I also learned the basic distinction between:

```text
library/package
    ↓
module
    ↓
class/function
```

I understand that:

* a library/package provides reusable code
* a module is generally a Python file containing reusable code
* modules can contain functions and classes
* `FastAPI` is a class provided by the `fastapi` package
* `FastAPI()` creates an object/instance
* `app` is the object created from `FastAPI()`

I do not consider classes, objects, modules, or packages deeply understood. Reinforce these concepts naturally when relevant.

## How to teach me programming

I want to understand what the computer is actually doing, not merely which syntax to type.

For example, when we use:

```python
app = FastAPI()
```

I want to eventually understand the relationship between:

```text
Python
 ↓
package/library
 ↓
module
 ↓
class
 ↓
object
 ↓
application
```

Likewise, when we use:

```javascript
fetch(...)
```

I want to understand the relationship between:

```text
JavaScript
 ↓
function call
 ↓
HTTP request
 ↓
server
 ↓
HTTP response
 ↓
JavaScript
```

However, don't turn every lesson into a theoretical lecture. Explain concepts at the depth necessary to understand what we are currently building.

## Current project structure

The current project is approximately:

```text
quickread/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── prototype/
│   ├── ai_test.py
│   └── quickread.py
├── docs/
│   ├── Architecture.md
│   ├── API.md
│   ├── PromptTemplates.md
│   ├── ProductRequirements.md
│   ├── Roadmap.md
│   └── possibly other documentation
├── requirements.txt
├── README.md
├── LICENSE
├── .env
└── .venv/
```

Again, the supplied files below this prompt are authoritative. This structure is only contextual.

## Original QuickRead concept

QuickRead is an AI-powered web application that accepts an article URL, extracts the article text, and produces a concise summary.

The intended basic flow is:

```text
URL
 ↓
Article extraction
 ↓
Article text
 ↓
AI processing
 ↓
Summary
```

The eventual application architecture is approximately:

```text
Browser
 ↓
Frontend
 ↓
FastAPI backend
 ↓
Article extraction
 ↓
AI processing
 ↓
JSON response
 ↓
Frontend
```

The current frontend is plain HTML/CSS/JavaScript.

Do not migrate it to React unless there is a deliberate reason to do so later.

## Prototype

The existing prototype contains the original article-extraction and AI-summarization logic.

It uses:

* `requests`
* `trafilatura`
* `python-dotenv`
* OpenAI Python client
* OpenRouter
* `openai/gpt-oss-20b:free`

The prototype's basic flow is:

```text
URL
 ↓
extract_article()
 ↓
article text
 ↓
summarize_article()
 ↓
AI-generated summary
```

Eventually we will move this functionality into the FastAPI backend.

Do not throw away the working prototype logic unnecessarily.

## Backend progress

We created a FastAPI backend.

The current backend is represented by the supplied `backend/app.py`.

The important concepts we have established are:

```python
from fastapi import FastAPI
```

`fastapi` is the package/library.

`FastAPI` is a class provided by that package.

```python
app = FastAPI()
```

creates an instance/object from that class.

We run the backend with:

```bash
uvicorn backend.app:app --reload
```

The `backend.app` part refers to the Python module:

```text
backend/app.py
```

The `:app` part tells Uvicorn to use the object called `app` inside that module.

The backend runs locally at:

```text
http://127.0.0.1:8000
```

We created:

```text
GET /
```

and:

```text
POST /summarize
```

The `/summarize` endpoint currently accepts JSON shaped like:

```json
{
  "url": "https://example.com"
}
```

using a Pydantic model similar to:

```python
class SummarizeRequest(BaseModel):
    url: str
```

We tested the endpoint using FastAPI's interactive documentation:

```text
http://127.0.0.1:8000/docs
```

The endpoint currently returns a temporary response containing the received URL.

We encountered a `422 Unprocessable Entity` while testing because the submitted JSON was malformed/missing a curly bracket. This was a request-body problem, not a fundamental FastAPI problem.

## Frontend progress

The frontend contains:

* a URL input
* a Quick Read button
* a status/error message

We have spent substantial time working on CSS and responsive behavior.

Issues we encountered and fixed included:

* button alignment
* input/button alignment
* Flexbox layout
* responsive behavior
* maintaining input height on narrow screens
* smooth resizing
* hover styling
* focus/border behavior
* error-message layout
* typography

One important lesson was that an error message can itself affect layout if it occupies normal layout space. We adjusted the design so validation messages don't unexpectedly push the input/button around.

## JavaScript progress

The JavaScript validates the URL before sending it.

The basic validation logic is similar to:

```javascript
const url = input.value.trim();

if (url === "") {
    status.textContent = "Please enter a URL";
    return;
}

if (!url.startsWith("http://") && !url.startsWith("https://")) {
    status.textContent = "Please enter a valid URL";
    return;
}
```

We specifically discussed:

```text
=== → strict equality comparison
!   → logical NOT
return → stop execution of the current function
```

I initially misunderstood whether the second `if` would automatically stop the rest of the function. We established that the `if` only determines whether its block runs; `return` is what stops the function.

## Frontend/backend connection

The frontend is now successfully communicating with the backend.

The JavaScript contains code conceptually similar to:

```javascript
const response = await fetch("http://127.0.0.1:8000/summarize", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        url: url
    })
});

const data = await response.json();

status.textContent = data.message;
```

This works.

However, I have explicitly said that I **do not fully understand everything in this code yet**.

Do not assume that successful execution means I understand:

* `fetch`
* `async`
* `await`
* HTTP
* request headers
* request body
* `JSON.stringify`
* `response.json()`
* promises
* asynchronous programming

These should be reinforced naturally through future work.

The conceptual request cycle we have established is:

```text
User
 ↓
click Quick Read
 ↓
JavaScript
 ↓
fetch()
 ↓
HTTP POST
 ↓
FastAPI
 ↓
Pydantic validates JSON
 ↓
Python endpoint function
 ↓
JSON response
 ↓
JavaScript
 ↓
response.json()
 ↓
data.message
 ↓
DOM update
```

## Recent frontend lesson

I asked whether every HTML element needs an ID to be accessed from JavaScript.

We established that it does not.

An ID is one way to select an element:

```javascript
document.getElementById(...)
```

but JavaScript can also use:

```javascript
document.querySelector(...)
```

with CSS selectors, including:

* IDs
* classes
* tags
* attributes
* combinations of selectors

The useful rule is:

> Give an element an ID when you need a convenient unique way to refer to that particular element.

Do not assume every element should have an ID.

## Where we stopped

This is Day 4.

We have just completed the first frontend/backend connection.

I want to review and consolidate what we have built rather than immediately adding a large new feature.

The next useful activity is to inspect the actual supplied files and walk through the frontend architecture:

```text
index.html
   ↓
style.css
   ↓
script.js
   ↓
HTTP request
   ↓
backend/app.py
```

Then we should gradually deepen my understanding of the existing code.

Eventually, the temporary backend behavior:

```json
{
  "message": "Received URL: ..."
}
```

will be replaced with the actual QuickRead pipeline:

```text
POST /summarize
 ↓
receive URL
 ↓
extract article
 ↓
send article text to AI
 ↓
receive summary
 ↓
return summary as JSON
 ↓
frontend displays summary
```

But do not jump directly to the finished implementation.

Build that transition incrementally so I understand each layer.

## Development philosophy

Use QuickRead as a real application and as a practical software-development curriculum.

The progression should naturally expose me to:

```text
HTML/CSS
 ↓
JavaScript
 ↓
DOM
 ↓
events
 ↓
HTTP
 ↓
JSON
 ↓
APIs
 ↓
FastAPI
 ↓
Python backend logic
 ↓
article extraction
 ↓
AI integration
 ↓
error handling
 ↓
testing/debugging
 ↓
Git/development workflow
 ↓
application architecture
 ↓
deployment/production concepts
```

The exact sequence can change based on what the application needs.

Do not introduce technologies just for the sake of complexity.

The goal is to understand software development by building something real.

## Important instruction about the supplied files

The code files included after this prompt represent the actual current implementation.

Use them as the source of truth.

When explaining something:

* refer to the actual code
* don't invent code that isn't present
* don't assume an earlier version of the code
* don't silently rewrite working code
* if you notice a discrepancy between this handoff description and the files, tell me

Start by examining the supplied files and determining the current state of the application.

Do not immediately start coding a new feature.

First help me understand where we are and what the next logical development step is.

---

# CURRENT PROJECT FILES

The following files are the authoritative current implementation.

===== frontend/index.html =====

[PASTE CURRENT FILE HERE]

===== frontend/style.css =====

[PASTE CURRENT FILE HERE]

===== frontend/script.js =====

[PASTE CURRENT FILE HERE]

===== backend/app.py =====

[PASTE CURRENT FILE HERE]

===== prototype/quickread.py =====

[PASTE CURRENT FILE HERE]

===== OPTIONAL DOCUMENTATION =====

[PASTE RELEVANT DOCS HERE, IF NEEDED]
