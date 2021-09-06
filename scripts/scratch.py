true = "true"
false = "false"
null = "null"
file = {"text":"Mean 'C' was found to be significantly enhanced (+30%) only in the latanoprost-treated group compared with the baseline (P = 0.017)","tokens":[{"text":"Mean","start":0,"end":4,"id":0,"ws":true},{"text":"'","start":5,"end":6,"id":1,"ws":false},{"text":"C","start":7,"end":8,"id":2,"ws":false},{"text":"'","start":17,"end":18,"id":3,"ws":true},{"text":"was","start":19,"end":22,"id":4,"ws":true},{"text":"found","start":23,"end":28,"id":5,"ws":true},{"text":"to","start":29,"end":31,"id":6,"ws":true},{"text":"be","start":32,"end":34,"id":7,"ws":true},{"text":"significantly","start":35,"end":48,"id":8,"ws":true},{"text":"enhanced","start":49,"end":57,"id":9,"ws":true},{"text":"(","start":58,"end":59,"id":10,"ws":false},{"text":"+30","start":59,"end":62,"id":11,"ws":false},{"text":"%","start":62,"end":63,"id":12,"ws":false},{"text":")","start":63,"end":64,"id":13,"ws":true},{"text":"only","start":65,"end":69,"id":14,"ws":true},{"text":"in","start":70,"end":72,"id":15,"ws":true},{"text":"the","start":73,"end":76,"id":16,"ws":true},{"text":"latanoprost","start":77,"end":88,"id":17,"ws":false},{"text":"-","start":88,"end":89,"id":18,"ws":false},{"text":"treated","start":89,"end":96,"id":19,"ws":true},{"text":"group","start":97,"end":102,"id":20,"ws":true},{"text":"compared","start":103,"end":111,"id":21,"ws":true},{"text":"with","start":112,"end":116,"id":22,"ws":true},{"text":"the","start":117,"end":120,"id":23,"ws":true},{"text":"baseline","start":121,"end":129,"id":24,"ws":true},{"text":"(","start":130,"end":131,"id":25,"ws":false},{"text":"P","start":131,"end":132,"id":26,"ws":true},{"text":"=","start":133,"end":134,"id":27,"ws":true},{"text":"0.017","start":135,"end":140,"id":28,"ws":false},{"text":")","start":140,"end":141,"id":29,"ws":false}],"spans":[{"start":59,"end":63,"token_start":11,"token_end":12,"label":"MEAS"},{"start":77,"end":88,"token_start":17,"token_end":17,"label":"INTV"}],"relations":[{"child":11,"head":17,"label":"A1"}],"_input_hash":1434386030,"_task_hash":-1384494864,"_is_binary":false,"_session_id":null,"_view_id":"ner_manual","answer":"accept","_timestamp":1629713374}
for x in file["tokens"]:
    if x["start"] > 8:
        x["start"] = x["start"] - 8
        x["end"] = x["end"] - 8
for x in file["spans"]:
    if x["start"] > 8:
        x["start"] = x["start"] - 8
        x["end"] = x["end"] - 8

from spacy.tokens import DocBin, Doc
from spacy.vocab import Vocab
from scripts.evaluate import main as evaluate
from prodigy.components.preprocess import add_tokens
import prodigy
from prodigy.components.loaders import JSONL
from prodigy.components.preprocess import add_tokens
import spacy
from spacy.tokens import DocBin
import json
from glob import glob
import os
from collections import defaultdict
import re
from Bio import Entrez
import pickle
import tarfile

from prodigy.components.preprocess import split_sentences
import spacy

nlp = spacy.load("en_core_web_sm")

stream = split_sentences(nlp, stream, min_length=30)
for x in stream:
    print(x)