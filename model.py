from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training dataset
texts = [
"internet not working",
"wifi slow",
"server down",
"network issue",

"payment failed",
"charged twice",
"refund not received",
"billing issue",

"customer support not responding",
"service very slow",
"need help from support"
]

labels = [
"technical","technical","technical","technical",
"billing","billing","billing","billing",
"service","service","service"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = MultinomialNB()

model.fit(X, labels)



def predict_category(text):

    x = vectorizer.transform([text])
    category = model.predict(x)[0]

    return category



def predict_priority(text):

    text = text.lower()

    if "urgent" in text or "immediately" in text or "server down" in text:
        return "High"

    elif "not working" in text or "failed" in text:
        return "Medium"

    else:
        return "Low"



def assign_team(category):

    if category == "technical":
        return "IT Support Team"

    elif category == "billing":
        return "Finance Team"

    else:
        return "Customer Support"