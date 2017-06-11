from slovnik.models import Word


def get_surrounding_words_in_learning(category, word):
    words_ordered = Word.objects.filter(category__category_short_name=category).order_by('word_short_name')
    prev = ''
    next = ''
    hit = False
    for index, item in enumerate(words_ordered):
        if hit:
            next = item
            break
        if item.word_short_name == word:
            hit = True
        else:
            prev = item

    return {'prev': prev, 'next': next}
