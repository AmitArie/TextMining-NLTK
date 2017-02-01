#!/usr/bin/python3
import json
import csv

TAG = 1
VALUE = 0
NUMBER_OF_ARTICLES = 2135


def json_to_object(file_name):
    with open(file_name) as json_article:
        article = json.loads(json.load(json_article))
        return article

def print_articles(n):
    i = 0
    for article_number in range(n):
        file_name = "articlesJsons/" + str(article_number) + ".json"
        with open(file_name) as json_article:
            article = json.loads(json.load(json_article))
            print("Article name: ", article["name"])
            print("Article number: ", i)
            sent = [ [int(k),v] for k, v in article["sent_tag"].items() ]
            sent.sort(key=lambda x: x[0])
            for s in sent:
                print(s[1])
                print("  ")
        i += 1
        print("  ")
        print("  ")


def get_entities_from_sentence(sentence, entity):
    entities = [pair[VALUE] for pair in sentence if pair[TAG] == entity]
    return entities

    
def get_entities_from_article(article, entity):
    sentences_dictionary = article["sent_tag"]
    entities = set()
    
    for key in sentences_dictionary:
        entities.update(get_entities_from_sentence(sentences_dictionary[key], entity))
        
    return entities



def get_persons(articles):
    persons = set()
    for article in articles:
        persons.update(get_entities_from_article(article, "PERSON"))
    return persons



def get_organizations(articles):
    organizations = set()
    for article in articles:
        organizations.update(get_entities_from_article(article, "ORGANIZATION"))
    return organizations
    

def is_entity_in_sentence(entity, kind, sent):
    for word in sent:
        if word[TAG] == kind and word[VALUE] == entity:
            return True
    return False
    
def is_person_organization_contained_at_same_sentence(person, organization, articles):

    for index, article in enumerate(articles):
        article_name = article["name"]


        sentences_dictionary = article["sent_tag"]
        
        for key in sentences_dictionary:
            sent = sentences_dictionary[key]
            if is_entity_in_sentence(person, "PERSON", sent) and is_entity_in_sentence(organization, "ORGANIZATION", sent):
                return article_name,key,index
    return False
            
        
def create_ORG_PERSON_CSV():
    articles = [json_to_object("articlesJsons/" + str(i) + ".json") for i in range(NUMBER_OF_ARTICLES)]
    print("DONE READING JSON FILES")
    organizations = list(get_organizations(articles))
    print("There are ", len(organizations), " Organizations In all the Articles")
    persons = list(get_persons(articles))
    print("There are ", len(persons), " Persons In all the Articles")

    print(organizations)
    print(organizations[0])
    with open('POS_ORG_CO_OC.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(["Organization", "Person", "Article Name", "Article Number", "Sentence Number"])

        for organization in organizations:
            if organization == '':
                continue
            for person in persons:
                print("Checking if Organization: ",organization , " and Person: ", person , " are in the same sentence.")
                res = is_person_organization_contained_at_same_sentence(person, organization, articles)
                if res:
                    writer.writerow([organization, person, res[0].strip("\""), res[2], res[1]])
                    print("Writing into csv: ", [organization, person, res[0].strip("\""), res[2], res[1]])


def main():
    create_ORG_PERSON_CSV()


            
            
    
    

    
    


    
if __name__ == "__main__":
    main()