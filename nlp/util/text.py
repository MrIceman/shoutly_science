from nltk.corpus import stopwords
import nltk
import re

nltk.download('stopwords')

stop_words = stopwords.words('german')


def clean_and_tokenize_text(text):
    tokenized_words = text.replace('\n', '').replace('-', ' ').split()
    filtered_tokenized_words = [word for word in tokenized_words if word not in stop_words]

    return filtered_tokenized_words


def is_trash_word(word):
    city_names = ['cuxhaven', 'vechta', 'wiesmoor', 'giefhorn', 'aurich', 'dem', 'einbeck', 'thuedinghaueser',
                  'cloppenburg', 'stopword', 'wiesmoor', 'salzgitter', 'cuxhaven', 'vechta', 'sarstedt',
                  'waltherrathenaustraße', 'aurich', 'cloppenburg', 'braunlage', 'martinistraße', 'rinteln', 'dornum',
                  'thuedinghaeuser', 'annenheider', 'wittmund', 'sigiltrastraße', 'nienburg', 'hammenstedt', 'einbeck',
                  'groner', 'gandersheim', 'munster', 'friesoythe', 'wilhelmshaven', 'butjadingen', 'roswithastraße',
                  'polizeistation', 'hildesheim', 'schaeferhund', 'museumsbahn', 'hardegsen', 'gifhorn', 'boesel',
                  'gaststaette', 'salzdetfurth', 'herzlake', 'rollshausen', 'seesen', 'kalefeld', 'außendeicher',
                  'aufzug',
                  'bodenfelde', 'schoeppenstedt', 'delliehausen', 'meinersen', 'schanzenstraße', 'dransfeld',
                  'vielstedter',
                  'visselhoevede', 'schoningen', 'northeim', 'gierswalde', 'lueneburg', 'babynahrung', 'goslar',
                  'schuermann',
                  'uslar',
                  'lutterhausen',
                  'celle',
                  'ölhafendamm',
                  'peine',
                  'ellerbrocker',
                  'esens',
                  'herzberg',
                  'nienstaedt',
                  'bueckeburg',
                  'voller'
                  ]
    for i in city_names:
        if i == word:
            return True
    return False


def is_bp_text(word):
    return 'bp' in word and len(word) <= 5


def clean_text(text: str) -> str:
    splitted_story = text.replace('\n', '') \
        .replace('-', ' ') \
        .replace('0', '') \
        .replace('1', '') \
        .replace('2', '') \
        .replace('3', '') \
        .replace('4', '') \
        .replace('5', '') \
        .replace('6', '') \
        .replace('7', '') \
        .replace('8', '') \
        .replace('9', '') \
        .split(' ')
    new_story = []
    for word in splitted_story:
        lowered_word = word.lower()
        if lowered_word in stop_words or lowered_word.isdigit() or len(lowered_word) < 4 \
                or is_trash_word(lowered_word) or is_bp_text(lowered_word):
            continue
        else:
            if lowered_word == 'cuxhaven':
                print('Found {}'.format(lowered_word))
            new_story.append(lowered_word)
    return ' '.join(new_story)
