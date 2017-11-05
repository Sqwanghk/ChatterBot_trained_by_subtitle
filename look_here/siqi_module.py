from chatterbot.utils import print_progress_bar
from chatterbot.trainers import Trainer
from chatterbot.conversation import Statement, Response

class SubtitleTrainer(Trainer):

    def train(self, N = None, *corpus_paths):

        print('N=',N)
        for corpus in corpus_paths:
    
            print(corpus)
            file = open(corpus)
            l_line = []
            if N:
                for i in range(N):
                    line = file.readline().strip()   #.replace(' ',',')
                    l_line.append(line)
            else:
                l_line = file.readlines()
                N = len(l_line)
                for i in range(N):
                    l_line[i] = l_line[i].strip() 
            file.close()

            previous_statement_text = None

            for conversation_count, text in enumerate(l_line):
                print_progress_bar("Subtitle Trainer", conversation_count + 1, N)

                statement = self.get_or_create(text)

                if previous_statement_text:
                    statement.add_response(
                        Response(previous_statement_text)
                    )

                previous_statement_text = statement.text
                self.storage.update(statement)
            