**Status: Draft/Experimental**

# Overview

The QuickRead system accepts user input in form of web URL or plain text, processes it in the backend, and presents a structured output on the frontend. The product's role is classify the article type, incorporate a relevant prompt template, and output the data without introducing unsupported facts. The output will be scannable and humans can read it in under a minute. 

# High-Level Architecture

QuickRead follows a client-server architecture. The frontend is responsible for accepting web URL, while the backend handles text extraction, document classification, and communication with the AI model. This separation keeps the frontend relatively lightweight.

Data transfer and text processing in QuickReads uses the following flow:

``` architecture flow

Browser

↓

Frontend (React)

↓

Backend API (FastAPI)

↓

Article Extraction

↓

AI Processing

↓

Response

```

- **Browser:** The web browser is where the user requests QuickRead to summarize an article.

- **Frontend (React):** The frontend accepts the web URL and uses a POST method to send it to the backend.

- **Backend API (FastAPI):** The backend fetches the webpage.

- **Article Extraction:** The backend analysis the web page and extracts the main article in plain text.

- **AI Processing:** The extracted text is processed through an AI model to generate relevant summary.

- **Response:** The generated summary is sent back to the frontend and displayed to the user.

# Request Lifecycle

QuickRead processes user request using the following logic:

``` request lifecycle

User Pastes URL or plain text

↓

Backend validates URL or text

↓

Downloads webpage

↓

Extracts article

↓

Classifies article

↓

Generates summary

↓

Returns JSON

↓

Frontend displays summary

```

# Components

QuickRead is built using the following modules that work together to successfully accepts web URL, process data, and output structured results:

### HTML Parser

Parses HTML to read text on web pages.

### Article Extractor

Identifies the main article piece on the web page and extracts it.

### Article Categorizer

Uses AI to determine article type and assigns it one of the predefined category.

### Summary Generator

Generates a summary after determining the article type and empoying a revelant LLM prompt.

### Returns JSON

Content summary is sent to the frontend in JSON.

### Output Display

Presents a scannable and human readable summary on the frontend.

# Data Flow

QuickRead accepts accepts user data, processes it, and outputs the result using the following logic:

``` data flow

URL

↓

HTML

↓

Article Text

↓

Metadata

↓

Prompt

↓

JSON

↓

UI

```

# AI Pipeline



# Project Structure



# Technology Stack



# API Overview



# Future Architecture
