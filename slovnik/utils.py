from slovnik.models import Word, RatingChoices, RatingUser, RatingImages
from random import randint


def get_word_details(category, word):
    words_ordered = Word.objects.filter(category__category_name_short=category).order_by('word_name_short')
    total = words_ordered.count()
    prev_item = ''
    next_item = ''
    hit = False
    current_position = 1
    for index, item in enumerate(words_ordered):
        if hit:
            next_item = item
            break
        if item.word_name_short == word:
            hit = True
        else:
            prev_item = item
            current_position += 1

    return {'prev': prev_item, 'next': next_item, 'word_count': total, 'current_position': current_position}


def get_first_word_in_category(category):
    return Word.objects.filter(category__category_name_short=category).first()


def generate_four_images(category, past_images=[]):
    # choose 4 different random items from the Word, within the given category
    return_set = []
    query_set = Word.objects.filter(category__category_name_short=category).exclude(id__in=past_images).all()
    count = query_set.count()
    for i in range(1, 5):
        selected_word = query_set[randint(0, count-i)]
        return_set.append(selected_word)
        query_set = query_set.exclude(id=selected_word.id)
    return return_set


def get_image_for_user(user):
    try:
        rated_images = RatingChoices.objects.filter(user=RatingUser.objects.get(user=user))
        img_ids = []
        for img in rated_images:
            img_ids.append(img.image.id)
        return RatingImages.objects.all().exclude(id__in=img_ids).first()
    except RatingUser.DoesNotExist:
        return RatingImages.objects.first()
