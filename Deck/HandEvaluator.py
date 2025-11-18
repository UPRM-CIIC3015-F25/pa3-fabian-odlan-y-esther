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

        # The ranks
        if card.rank in rank_count:
            rank_count[card.rank] += 1
        else:
            rank_count[card.rank] = 1

        # The suits
        if card.suit in suit_count:
            suit_count[card.suit] += 1
        else:
            suit_count[card.suit] = 1

        # Checks for flush
        is_flush = False
        for count in suit_count.values():
            if count >= 5:
                is_flush = True
                break

        # Sorts unique ranks for straight check
        unique_rank = sorted(rank_count.keys())
        is_straight = False

        # Check for straight
        if len(unique_rank) >= 5:
            # Check for a regular straight
            for i in range(len(unique_rank) - 4):
                if (unique_rank[i+4] - unique_rank[i] == 4 and len(set(unique_rank[i:i + 5])) == 5):
                    is_straight = True
                    break

            # Check for Ace-low straight
            if not is_straight and len(unique_rank) >= 5:
                low_straight_ranks = [1,2,3,4,5]
                has_ace = any(rank in [1,14] for rank in unique_rank)
                has_low_cards = all(rank in unique_rank for rank in [2,3,4,5])

                if has_ace and has_low_cards:
                    is_straight = True

        # Get rank count in descending order
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

