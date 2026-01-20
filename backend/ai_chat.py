from openai import OpenAI
client = OpenAI(api_key="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")

def kajal_chat(msg):
    system = "You are Kajal, a friendly female AI. Reply in Hindi if user uses Hindi, otherwise English."
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": msg}
        ]
    )
    return res.choices[0].message.content
