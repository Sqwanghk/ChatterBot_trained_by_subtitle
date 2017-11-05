# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import datetime
            
# Create a new chat bot and configure it
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
)

#start training using subtitles in file. The file is based on Simplified Chinese.
chatbot.train(30000,30300,'/Users/wangsiqi/Downloads/subtitle.corpus')

#export the result
chatbot.trainer.export_for_training('./database.yml')

#talk with the chat bot
print('This chat bot is based on Simplified Chinese.')
while True:
    try:
        print("Your term: ",end='')
        bot_input = chatbot.get_response(None)
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

