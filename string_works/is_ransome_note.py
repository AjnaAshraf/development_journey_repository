"""
create a function ransome_note(note,magzine)
display true if all charcters in note is present in magzine otherwise display false

"""

def is_ransome_note(note,magzine):

    for ch in note.lower():

        if ch not in magzine or note.count(ch) != magzine.count(ch):

            print(False)
            break

    else:

        print(True)

is_ransome_note("hen","chicken")
is_ransome_note("ron","thrown")
is_ransome_note("pen","chicken")
is_ransome_note("zee","zebra")

    