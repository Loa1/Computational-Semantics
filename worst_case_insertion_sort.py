import random, time

def insertion_sort(cards):
    j = 1
    while j < len(cards):
        key = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > key:
            cards[i + 1] = cards[i]
            i = i - 1
        cards[i + 1] = key
        j = j + 1
    




number_of_cards = [10, 100, 1000, 10000]
time_list = [1, 2, 3, 4]
for n  in range(4):
    cards = list (range(number_of_cards[n], 1, -1))
    start = time.time()
    
    insertion_sort(cards)
    
    time_consumption = time.time() - start
    time_list[n] = time_consumption

    print('cards: ' + '{0:.9f}'.format(number_of_cards[n]) + '     time: ' + '{0:.9f}'.format(time_list[n]) + ' seconds')
    n = n + 1


