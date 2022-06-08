from transformers import pipeline

nlp = pipeline("question-answering")

context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script.
"""
import os, datetime, random, pathlib, os, base64, json, io
import boto3
import rollbar

from transformers import pipeline

def lambda_handler(event, context):

    # How to send a question
    c = """AN UNEXPECTED PARTY IN A HOLE IN THE GROUND there lived a hobbit. Not a nasty, dirty, wet
    hole, filled with the ends of worms and an oozy smell, nor yet a dry,
    bare, sandy hole with nothing in it to sit down on or to eat: it was
    a hobbit-hole, and that means comfort."""
    result = nlp(question="What is extractive question answering?", context=c)
    print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
    return {"result": result}

