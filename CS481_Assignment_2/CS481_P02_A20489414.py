from CS481_P02_A20489414_Preprocessor import preprocess

from sys import argv

if argv[1] == "YES":
    ignore = True
else:
    ignore = False

print("Bode, Jacob, A20489414 Solution:")

if ignore:
    preprocess(True)
    print("Ignored pre-processing step: ignore stopwords")
else:
    preprocess(False)
    print("Included pre-processing step: ignore stopwords")
    
from CS481_P02_A20489414_Trainer import calculate_probability, calculate_probability_input
print("\nTraining Classifier...")
# Training done in import of cs481_p02_a20489414_trainer.py

print("Testing Classifier...")
test_title_list = []
test_tag_list = []
with open(r"CS481_Assignment_2/Titles.csv", "r", encoding="utf8") as f1:
    with open(r"CS481_Assignment_2/Tags.csv", "r", encoding="utf8") as f2:
        # Read every 5th line to test list
        counter = 0
        while True:
            title = f1.readline()
            tag = f2.readline()
            if title != "":
                if counter % 5 == 0:
                    test_title_list.append(title[:-2])
                    test_tag_list.append(int(tag))
                counter += 1
            else:
                break

tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(test_title_list)):
    prediction = calculate_probability(test_title_list[i])
    if prediction == test_tag_list[i] == 0:
        tn += 1
    elif prediction == test_tag_list[i] == 1:
        tp += 1
    elif prediction == 1 and test_tag_list[i] == 0:
        fp += 1
    elif prediction == 0 and test_tag_list[i] == 1:
        fn += 1
    

print("Test results / metrics:")
print("Number of true positives: %s" % tp)
print("Number of true negatives: %s" % tn) 
print("Number of false positives: %s" % fp)
print("Number of false negatives: %s" % fn)
print("Sensitivity (recall): %s" % (tp / (tp + fn)))
print("Specificity: %s" % (tn / (tn + fp)))
print("Precision: %s" % (tp / (tp + fp)))
print("Negative predictive value: %s" % (tn / (tn + fn)))
print("Accuracy: %s" % ((tp + tn) / (tp + tn + fp + fn)))
print("F-score: %s" % ((2 * tp) / (2 * tp + fp + fn)))


while True:
    calculate_probability_input()
    if input("Do you want to enter another sentence [Y/N]?").lower() != "y":
        break