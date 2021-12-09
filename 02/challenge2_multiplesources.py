import glob


def find_most_common_word():
    txt_files = glob.glob('*.txt')
    tracker = dict()
    print(f"Number of .txt files : {len(txt_files)}")

    for txt in txt_files:               # read each text file found
        with open(txt) as f:
            line = f.readline()         # read text file contents line by line
            while line != '':           # ignore empty line
                words = line.split()    # split line onto words by splitting spaces
                for word in words:
                    # normalize input by removing notations
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1  # add found word t odictionary
                    else:
                        # if word already in dictionary, increment by one
                        tracker[word] = tracker[word] + 1
                line = f.readline()     # go to the next line

    maxKey = max(tracker, key=tracker.get)  # return the key with maximum value
    # return the maximum value of the key
    maxValue = max(tracker.values())

    print(f"Most common word : {maxKey}")
    print(f"How many times : {maxValue}")
    print(f"Dictionary : {tracker}")


if __name__ == "__main__":
    find_most_common_word()
