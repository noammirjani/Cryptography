import copy
import numpy as np


def get_number(char):
    return ord(char) - ord("a")


def get_char(number):
    return chr(number + ord('a'))


def shift_string(my_str, key_size):
    shift_str = my_str[key_size::]
    return shift_str


def count_same(my_str, key_size):
    shift_str = shift_string(my_str, key_size)
    count = 0

    for i in range(len(shift_str)):
        if shift_str[i] == my_str[i]:
            count += 1

    print("key size:", key_size, "sames char:", count)

    return count


def big_same(my_str, max_key_size):
    max_count = 0
    key = 0
    for i in range(1, max_key_size + 1):
        curr_count = count_same(my_str, i)
        if curr_count > max_count:
            max_count = curr_count
            key = i

    return key


def divide_cipher(ciphertext, key_size):
    segments = []
    for i in range(0, len(ciphertext), key_size):
        segment = ciphertext[i:i + key_size]
        segments.append(segment)
    return segments


def get_freq_vec(segments):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
                "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
                "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                "y": 0, "z": 0}

    key_size = len(segments[0])
    print("\nfinal key size", key_size)

    print("\nThe frequency of the letters:")
    vec_of_freq = [copy.deepcopy(alphabet) for _ in range(key_size)]

    for i in range(key_size):
        for segment in segments:
            vec_of_freq[i][segment[i]] += 1
        print(vec_of_freq[i])

    return vec_of_freq


# Define the function
def dict_list_to_list_of_lists(dict_list, len_str):
    # Get a list of the keys in the first dictionary
    keys = list(dict_list[0].keys())

    # Initialize an empty list for each key
    lists = [[] for _ in range(len(dict_list))]

    # Iterate over the dictionaries in the list and append the values to the corresponding lists
    for j in range(len(dict_list)):
        for i, k in enumerate(keys):
            lists[j].append(dict_list[j][k] / len_str)

    # Return the resulting list of lists
    return lists


def create_shifted_lists():
    freq_list = [8.17, 1.29, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97,
                 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99,
                 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]

    shifted_lists = []
    for i in range(len(freq_list)):
        shifted_list = freq_list[-i:] + freq_list[:-i]
        shifted_lists.append(shifted_list)
    return shifted_lists


def scalar_product(list_):
    shifted_lists = create_shifted_lists()

    key = []
    print("\nThe results of the scalar multiplications:")

    for vector in list_:
        results = []
        for shifted_list in shifted_lists:
            results.append(np.dot(vector, shifted_list))

        print(results)
        key.append(np.argmax(results))

    return key


def calc_vizner(my_str, max_key_size):
    key = big_same(my_str, max_key_size)

    # padding
    my_str = my_str + "a" * (key - len(my_str) % key)

    segments = divide_cipher(my_str, key)

    freq_vec = get_freq_vec(segments)

    list = dict_list_to_list_of_lists(freq_vec, len(segments))

    key = scalar_product(list)

    print("\nfinal key to decode:")
    for k in key:
        print(get_char(k % 26), end="")

    decode_str = ""

    for segment in segments:
        for i in range(len(segment)):
            decode_str += get_char((get_number(segment[i]) - key[i]) % 26)

    print("\n\ndecoder\n", decode_str)


if __name__ == "__main__":
    calc_vizner("sbgnlwvqumlprtpfmgklfbuilfbhxfuzlvagoegwzgjgzavqozszegfw"
                "drxzavpkisjognwiajrsavyrapnjkwagxvqmqzowaribjqgevxbukcaor"
                "tljmpowzmeiyqxgunjicnljaugktmrtzwieioavtlvjiakduqcnljabsl"
                "lpvtnlpnzdgcyjywmfzhttvyokmpxllkbstmvvihlqbtazmekiqiyrvoq"
                "amimavtlkazkusvqzowuvrplieeagmkvsgqgzowqzslvqnifgngnllmyk"
                "njicndabuublbukpjkbstmvvihlqbtztmvtnkbbrlfiajkwkvvowzrjmmz"
                "gnljubxlsbgnllcetvxbukjwvgayqbukpliyohfxuezakvyayctrpwtzut"
                "szpuuaqablfbrjhfmikuewekwgerxmmtsuyewszldmputecaojsbvuuopv"
                "ioeiqkazmaklvnbxzwkhxlwvpxfhbvuuwdrttgzrvywafouyprnhvqablfb"
                "rjyslvuazmgkswoegwzpnjhdzrgkqjrkuwaggidqfnlvnbxostsgjwvgayqj"
                "hzplzrwbazrjhoqekagbegukxbxasuryzsorhllerkukmajljiajywkrocwz"
                "zgyuwaozkgfzlepnjazmtxlsbnjcsvggnwwshlavtcpjmykzkbukzaoagslz"
                "nbldmqgzanoetsoviazzbanzbukhazgnlavikulqbtasvggsahrjazmzosab"
                "nxflprzhubvihdiqbhfbnmlkwsxhvqbgywwobpgcfoastyudklvxlubputec"
                "aojsbvuutmgclwvntflebvvavgydabuublbukuwmqlvjijoywjrzdwmazowt"
                "bihlqbtzdilouyahiosevxlaablawvvswjipzpuiyyvemgotwavswgafoidm", 6)
