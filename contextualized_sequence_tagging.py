from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings,CharacterEmbeddings, StackedEmbeddings, FlairEmbeddings, ELMoEmbeddings, BertEmbeddings, PooledFlairEmbeddings
from typing import List
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

data_folder = 'data/'
models_dir = 'models/'
tag_type = 'ner'

## define the text and entitities to extract
columns = {0: 'text', 1: 'ner'}

## define training and development corpus
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              dev_file='dev.txt')

## Define Embedding to initialize encoder with

embedding_types: List[TokenEmbeddings] = [

    # PooledFlairEmbeddings('news-forward'),
    # PooledFlairEmbeddings('news-backward')
    # BertEmbeddings()
    # WordEmbeddings('glove'),
    # CharacterEmbeddings()
    FlairEmbeddings('news-forward'),
    FlairEmbeddings('news-backward')
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)


### Define the BiLSTM CRF Encoder
tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)
##


trainer: ModelTrainer = ModelTrainer(tagger, corpus)
trainer.train(models_dir+'/flairs_embeddings_tagger',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=100)