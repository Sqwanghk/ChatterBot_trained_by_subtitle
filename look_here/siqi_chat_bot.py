# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import datetime
#from siqi_module import SubtitleTrainer
            
# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Siqiqiii',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.3,
            'default_response': "( ⊙ o ⊙ )！咱们能谈些别的吗?"
        }
    ],
    database='./database.sqlite3',
    trainer='siqi_module.SubtitleTrainer'
    #trainer='chatterbot.trainers.ListTrainer'
)

chatbot.train(3000,'/Users/wangsiqi/Downloads/subtitle.corpus')
chatbot.trainer.export_for_training('./database.0.30.yml')
# Get a response to the input text 'How are you?'
print('This chat bot is based on Simplified Chinese.')
while True:
    try:
        print("Me: ",end='')
        bot_input = chatbot.get_response(None)
        print('Agent:',end='')
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

