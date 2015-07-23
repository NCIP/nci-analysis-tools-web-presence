import logging
from twisted.internet import reactor
from QueueJob import QueueJob
from SoccerProcessor import Processor

class SoccerJob(QueueJob):

    def consume(self, client, frame):
	processor = Processor(frame.body)
	processor.process()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    SoccerJob().run()
    reactor.run()
