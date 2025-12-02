from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    # Counts the ranks and suits
    rank_count = {}
    suit_count = {}

    for card in hand:
        rank_count[card.rank] = rank_count.get(card.rank, 0) + 1
        suit_count[card.suit] = suit_count.get(card.suit, 0) + 1

    # Checks for flush
    is_flush = any(count >= 5 for count in suit_count.values())

    #Checks for Straight
    unique_values = sorted({rank.value for rank in rank_count.keys()})
    is_straight = False

    # Check for regular straight
    for i in range(len(unique_values) - 4):
        if unique_values[i + 4] - unique_values[i] == 4:
            is_straight = True
            break

    # Check for Ace-low straight
    if not is_straight:
        if 14 in unique_values and all(val in unique_values for val in [2, 3, 4, 5]):
            is_straight = True

    count_values = sorted(rank_count.values(), reverse=True)

    # In order of ranking check hand types
    if is_straight and is_flush:
        return "Straight Flush"
    elif count_values[0] == 4:
        return "Four of a Kind"
    elif count_values[0] == 3 and len(count_values) >= 2 and count_values[1] == 2:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif count_values[0] == 3:
        return "Three of a Kind"
    elif count_values[0] == 2 and len(count_values) >= 2 and count_values and count_values[1] == 2:
        return "Two Pair"
    elif count_values[0] == 2:
        return "One Pair"
    else:
        return "High Card"

