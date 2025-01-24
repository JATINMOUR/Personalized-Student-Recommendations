import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

quiz_endpoint_url = "https://www.jsonkeeper.com/b/LLQT"
submission_data_url = "https://api.jsonserve.com/rJvd7g"

# Fetch data
quiz_data = requests.get(quiz_endpoint_url).json()
submission_data = requests.get(submission_data_url).json()

# Quiz details
topic = quiz_data['quiz']['topic']
total_questions = quiz_data['quiz']['questions_count']
negative_marks = float(quiz_data['quiz']['negative_marks'])
correct_answer_marks = float(quiz_data['quiz']['correct_answer_marks'])

print(f"Quiz Topic: {topic}")
print(f"Total Questions: {total_questions}")
print(f"Correct Marks: {correct_answer_marks}, Negative Marks: {negative_marks}")


correct_answers = submission_data['correct_answers']
incorrect_answers = submission_data['incorrect_answers']
accuracy = (correct_answers / total_questions) * 100
speed = submission_data['speed']

print(f"Correct Answers: {correct_answers}")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Speed: {speed}")


response_map = submission_data['response_map']
weak_questions = [qid for qid, ans in response_map.items() if ans == 'incorrect']

print(f"Weak Questions: {weak_questions}")


#  Create Recommendations part :
recommendations = []
if accuracy < 70:
    recommendations.append(f"Focus on improving the topic: {topic}. Current accuracy: {accuracy:.2f}%.")
if weak_questions:
    recommendations.append(f"Review weak questions: {weak_questions}")

print("Recommendations:")
for rec in recommendations:
    print(f"- {rec}")

topics = ['Topic A', 'Topic B', 'Topic C']
accuracy_values = [85, 70, 50]

sns.barplot(x=topics, y=accuracy_values)
plt.title("Accuracy by Topic")
plt.xlabel("Topics")
plt.ylabel("Accuracy (%)")
plt.show()

labels = ['Correct', 'Incorrect']
values = [correct_answers, incorrect_answers]

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Answer Distribution")
plt.show()
