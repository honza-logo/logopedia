from slovnik.models import Word


def get_word_details(category, word):
    words_ordered = Word.objects.filter(category__category_short_name=category).order_by('word_short_name')
    total    = words_ordered.count()
    prev_item = ''
    next_item = ''
    hit = False
    current_position = 1
    for index, item in enumerate(words_ordered):
        if hit:
            next_item = item
            break
        if item.word_short_name == word:
            hit = True
        else:
            prev_item = item
            current_position += 1

    return {'prev': prev_item, 'next': next_item, 'word_count': total, 'current_position': current_position}

