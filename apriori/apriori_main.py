import apriori
import sys
import time

sys.path.insert(0, '../util')
import util_functions


def run(transactions_file_name, classifier, min_supp_count, min_conf, output_file_name=None):

    transactions = util_functions.unzip_transactions_2(transactions_file_name)
    start = time.time()
    rules = apriori.generate_association_rules(transactions, min_support=min_supp_count, min_confidence=min_conf)
    # rules = apriori.generate_classification_rules(transactions,
    #                                              classifier,
    #                                              min_support=min_supp_count,
    #                                              min_confidence=min_conf)
    end = time.time()
    print('Total elapsed {}'.format((end - start)))
    if output_file_name is not None:
        print('Saving results to {}'.format(output_file_name))
        rules_str = util_functions.rules_to_string(rules)
        with open(output_file_name, 'w') as output_file:
            output_file.write(rules_str)
    else:
        rules_str = util_functions.rules_to_string(rules)
        print("\nPatterns")
        print(rules_str)


if __name__ == '__main__':
    path_name = '../data/'
    transactions_file_name = 'toMine_3_3.txt'
    min_supp_count = 100
    min_conf = 0.6
    classifier = [frozenset({'YES'}), frozenset({'NO'})]
    output_file_name = '../results/apriori/{}_supp_{}_conf_{}.txt'.\
        format(transactions_file_name[:transactions_file_name.find('.txt')], min_supp_count,
               str(min_conf).replace('.', ''))
    run(path_name + transactions_file_name, classifier, min_supp_count, min_conf, output_file_name)

