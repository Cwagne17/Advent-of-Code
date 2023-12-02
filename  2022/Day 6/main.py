def detect_packet(datastream: str, n: int):
    """In a given datastream, the function will return the position of the last unqiue substring of n length.
    Unique - A substring does not have multiple of the same letter
    Position - The index + 1

    Args:
        datastream (str): A random string of chars
        n (int): The length of the unique substring to evaluate against

    Returns:
        None: If no n length substring exists that is unique
        int: The last position of the substring of length n 
    """
    buf = []
    for char in datastream:
        buf.append(char)
        if len(set(buf)) == n:
            return datastream.index(''.join(buf)) + n
        elif len(buf) == n:
            buf.pop(0)
        
with open('input.txt') as fin:
    data = fin.readline().replace('\n', '')
    print(detect_packet(data, 4))
    print(detect_packet(data, 14))