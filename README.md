# Open AI Flask API Test

## Guide

> **Note:** Here is the basic guide to run this project on Windows. It's mandatory to have python installed.
> [Download Python for Windows](https://www.python.org/downloads/).

 1. Clone the repository
 2. Open the project in VS Code
 3. Start a new **cmd** terminal (inside de IDE)
 4. Create a [Virtual Enviroment](https://docs.python.org/3/library/venv.html): `python -m venv venv-name`
 5. Activate the VE: `call venv-name/scripts/activate`
 6. Install all the corresponding dependencies: `pip install -r requirements.txt`
> Replace **venv-name** with the desired name.
 7. Create a **.env** file and add the corresponding API key: `OPENAI_API_KEY="Your API key"`
 >Like the example in the .env.example file.
 8. Now you can run the project using one of these commands: 
 `python app.py` or `flask --app app.py run`
 9. Once the project is running, open **Postman** to test the /chat endpoint:

| Method | Url |
|--|--|
| POST | http://127.0.0.1:5000/chat  |

**Body:**

> Type: raw JSON

```json
{
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
}
```
**Response output:**
```json
{
    "response":  "Code calls itself back, Layers of logic unfold, Endless paths converge."
}
```
> The second content input inside the **"messages"** block can be replaced to obtain a different response:
> 
> **Current:** "content": "Write a haiku about recursion in programming."
> 
> **Try:**  "content": "Who is lionel messi?"

