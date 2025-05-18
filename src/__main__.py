import win32clipboard
import clipboard
def inc_num(card):

    return any(i.isdigit() for i in card)

def grab_deck_list():
    """
    This function will grab the deck list from the users clipboard and return the deck list as an array containing the card quantity and name, also returns the deck name.
    """
    win32clipboard.OpenClipboard()
    deck_list = win32clipboard.GetClipboardData()
    deck_list_arr = deck_list.split("\n")
    deck_list_formatted = []

    deck_name = deck_list_arr[1]
    deck_name_formatted = deck_name.replace("Name ", "")
    
    for i, card in enumerate(deck_list_arr):
        if inc_num(card):
            deck_list_formatted.append(card.strip())
    win32clipboard.CloseClipboard()
    return deck_list_formatted, deck_name_formatted

if __name__ == "__main__":
    
    dl, dn = grab_deck_list()
    print(dl, dn)

