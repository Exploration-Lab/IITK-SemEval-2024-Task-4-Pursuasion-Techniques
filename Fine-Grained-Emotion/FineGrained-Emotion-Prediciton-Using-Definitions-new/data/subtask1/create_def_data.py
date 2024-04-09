import pandas as pd 
import random
random.seed(100)
all_emotions = ['Loaded Language',
 'Slogans',
 'Reductio ad hitlerum',
 'Causal Oversimplification',
 'Thought-terminating cliché',
 'Bandwagon',
 'Repetition',
 'Appeal to authority',
 'Flag-waving',
 'Obfuscation, Intentional vagueness, Confusion',
 'Glittering generalities (Virtue)',
 "Misrepresentation of Someone's Position (Straw Man)",
 'Doubt',
 'Name calling/Labeling',
 'Presenting Irrelevant Data (Red Herring)',
 'Exaggeration/Minimisation',
 'Black-and-white Fallacy/Dictatorship',
 'Smears',
 'Appeal to fear/prejudice',
 'Whataboutism']

label2id = {'Loaded Language': 0,
 'Slogans': 1,
 'Reductio ad hitlerum': 2,
 'Causal Oversimplification': 3,
 'Thought-terminating cliché': 4,
 'Bandwagon': 5,
 'Repetition': 6,
 'Appeal to authority': 7,
 'Flag-waving': 8,
 'Obfuscation, Intentional vagueness, Confusion': 9,
 'Glittering generalities (Virtue)': 10,
 "Misrepresentation of Someone's Position (Straw Man)": 11,
 'Doubt': 12,
 'Name calling/Labeling': 13,
 'Presenting Irrelevant Data (Red Herring)': 14,
 'Exaggeration/Minimisation': 15,
 'Black-and-white Fallacy/Dictatorship': 16,
 'Smears': 17,
 'Appeal to fear/prejudice': 18,
 'Whataboutism': 19}

id2label = {'0': 'Loaded Language',
 '1': 'Slogans',
 '2': 'Reductio ad hitlerum',
 '3': 'Causal Oversimplification',
 '4': 'Thought-terminating cliché',
 '5': 'Bandwagon',
 '6': 'Repetition',
 '7': 'Appeal to authority',
 '8': 'Flag-waving',
 '9': 'Obfuscation, Intentional vagueness, Confusion',
 '10': 'Glittering generalities (Virtue)',
 '11': "Misrepresentation of Someone's Position (Straw Man)",
 '12': 'Doubt',
 '13': 'Name calling/Labeling',
 '14': 'Presenting Irrelevant Data (Red Herring)',
 '15': 'Exaggeration/Minimisation',
 '16': 'Black-and-white Fallacy/Dictatorship',
 '17': 'Smears',
 '18': 'Appeal to fear/prejudice',
 '19': 'Whataboutism'}

definition_dict = {"0":"Using specific words and phrases with strong emotional implications to influence an audience",
"1":"A brief and striking phrase that may include labeling and stereotyping",
"2":"Persuading an audience to disapprove an action or idea by suggesting that the idea is popular with groups hated in contempt by the target audience",
"3":"Assuming a single cause or reason when there are actually multiple causes for an issue",
"4":"Words or phrases that discourage critical thought and meaningful discussion about a given topic",
"5":"Attempting to persuade the target audience to join in and take the course of action because everyone else is taking the same action",
"6":"Repeating the same message over and over again so that the audience will eventually accept it",
"7":"Stating that a claim is true simply because a valid authority or expert on the issue said it was true, without any other supporting evidence offered",
"8":"Playing on strong national feeling or to any group to justify or promote an action or idea",
"9":"Using words which are deliberately not clear so that the audience may have its own interpretations",
"10":"These are words or symbols in the value system of the target audience that produce a positive image when attached to a person or issue",
"11":"When an opponent proposition is substituted with a similar one which is then refuted in place of the original proposition",
"12":"Questioning the credibility of someone or something",
"13":"Labeling the object of the propaganda campaign as either something the target audience fears hates finds undesirable or loves",
"14":"Introducing irrelevant material to the issue being discussed so that everyone attention is diverted away from the points made",
"15":"Either making things larger better worse or making something seem less important or smaller than it really is",
"16":"Presenting two alternative options as the only possibilities when in fact more possibilities exist",
"17":"A smear is an effort to damage or call into question someone's reputation by propounding negative propaganda",
"18":"Seeking to build support for an idea by instilling anxiety and panic in the population towards an alternative",
"19":"A technique that attempts to discredit an opponent position by charging them with hypocrisy without directly disproving their argument",
}

for mode in ["train","dev","test"]:
	file = mode+".tsv"
	df = pd.read_csv(file,sep="\t",names=["text","emo","id"])
	seq_labels = []
	defns = []
	text = []
	emo = []
	text_id = []
	for index, row in df.iterrows():
		emotions = list(map(int,row["emo"].split(",")))
		not_labels = list(set(range(20)) - set(emotions))
		random.shuffle(not_labels)
		for num, e in enumerate(emotions):
			defns.append(definition_dict[str(e)])
			seq_labels.append(0)
			text.append(row["text"])
			emo.append(row["emo"])
			text_id.append(row["id"])
			defns.append(definition_dict[str(not_labels[num])])
			seq_labels.append(1)
			text.append(row["text"])
			emo.append(row["emo"])
			text_id.append(row["id"])
	data = {"text":text,"defn":defns,"seq_label":seq_labels,"emo":emo,"id":text_id}
	df1 = pd.DataFrame(data)
	df1.to_csv(mode+"_def100.tsv",sep="\t",index=False,header=False)