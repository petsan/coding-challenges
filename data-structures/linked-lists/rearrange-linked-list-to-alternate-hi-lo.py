def alternate(ll):
    even = True
    cur = ll
    
    while cur.next:
        if cur.data> cur.next.data and even:
            cur.data, cur.next.data = cur.next.data, cur.data

        elif cur.data < cur.next.data and not even:
            cur.data, cur.next.data = cur.next.data, cur.data

        even = not even 
        cur = cur.next

        return ll

def alternate(ll):
    prev = ll
    cur = ll.next

    while cur:
        if prev.data > cur.data:
            prev.data, cur.data = cur.data, prev.data

        if not cur.next:
            break

        if cur.next.data > cur.data:
            cur.next.data, cur.data = cur.data, cur.next.data

        prev = cur.next
        cur = cur.next.next

    return ll
    