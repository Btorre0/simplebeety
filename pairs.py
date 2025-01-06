#  place holder so can activate the chatbot

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm good, thank you!", "Doing well, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem."]
    ],
    [
        r"I (feel|am) (.*)",
        ["Why do you %2?", "How long have you been %2?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand.", "Can you elaborate?", "Interesting!"]
    ],
]
