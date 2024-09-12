import pandas as pd

def words_saver(word_list: list, words_destination_path: str="./data/words/"):
    """
    Takes a python list of new words and adds them to the words_to_learn.csv

    Returns:
    ---------
    None
    """
    
    # Read in the main word repository csv file as a dataframe
    words_Dataframe = pd.read_csv(words_destination_path + "words_to_learn.csv")
    # Creating a new dataframe from the new words python list
    new_words_pd = pd.DataFrame({"English":word_list})

    #Add the new words to the main word repository Dataframe and drop the duplicates
    words_Dataframe = pd.concat([words_Dataframe, new_words_pd], axis=0, ignore_index=True).drop_duplicates()
    words_Dataframe.to_csv(words_destination_path + "words_to_learn.csv", index=False)


#     pass
# world_list = ["Hello", "Goodbye", "Hi"]
# world_list_2 = ["byebye", "book", "desk"]
# list_of_words = pd.read_csv("./data/words/words_to_learn.csv")
# new_pd = pd.DataFrame({"English":world_list})
# # print(list_of_words)
# print(new_pd)
# list_of_words = pd.concat([list_of_words, new_pd], axis=0, ignore_index=True)
# print(list_of_words)
# new_pd = pd.DataFrame({"English":world_list_2})
# list_of_words = pd.concat([list_of_words, new_pd], axis=0, ignore_index=True)
# print(list_of_words)
# list_of_words["English"] = world_list
# print(list_of_words)
# # list_of_words.append
# list_of_words = list_of_words.append(pd.DataFrame({'English': world_list_2}), ignore_index=True)
# print(list_of_words)
