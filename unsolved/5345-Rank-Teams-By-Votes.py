import unittest


def rank_by_votes(votes: list) -> str:
    from collections import Counter

    def right_tuple(elem):
        return elem[1]

    teams = {}
    for i in votes[0]:
        teams[i] = []

    for ballot in votes:
        pos = 1
        for vote in ballot:
            teams[vote].append(pos)
            pos += 1

    ranks = []
    print(teams)
    for team in teams:
        vote_counts = Counter(teams[team])
        most_votes = 0
        position = 0
        for votes in vote_counts.keys():
            if vote_counts[votes] > most_votes:
                most_votes = vote_counts[votes]
                position = votes
        ranks.append((team, position))

    print(ranks)

    prev = ranks[0][1]
    same = True
    for i in ranks[1:]:
        if i[1] == prev:
            prev = i[1]
        else:
            same = False
    if same is True:
        ranks.sort()
    else:
        ranks.sort(key=right_tuple)

    vote_string = ""
    for i in ranks:
        vote_string += i[0]

    return vote_string


class TestRankByVotes(unittest.TestCase):

    # def test_three(self):
    #     self.assertEqual(rank_by_votes(["ABC", "ACB", "ABC", "ACB", "ACB"]), "ACB")

    def test_four(self):
        self.assertEqual(rank_by_votes(["WXYZ", "XYZW"]), "XWYZ")
    #
    # def test_lots1(self):
    #     self.assertEqual(rank_by_votes(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]),
    #                      "ZMNAGUEDSJYLBOPHRQICWFXTVK")
    #
    # def test_lots(self):
    #     self.assertEqual(rank_by_votes(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]),
    #                      "ABC")
    #
    # def test_repeat(self):
    #     self.assertEqual(rank_by_votes(["M", "M", "M", "M"]), "M")
    #
    # def test_lng(self):
    #     self.assertEqual(rank_by_votes(["FVSHJIEMNGYPTQOURLWCZKAX", "AITFQORCEHPVJMXGKSLNZWUY", "OTERVXFZUMHNIYSCQAWGPKJL", "VMSERIJYLZNWCPQTOKFUHAXG", "VNHOZWKQCEFYPSGLAMXJIUTR", "ANPHQIJMXCWOSKTYGULFVERZ", "RFYUXJEWCKQOMGATHZVILNSP", "SCPYUMQJTVEXKRNLIOWGHAFZ", "VIKTSJCEYQGLOMPZWAHFXURN", "SVJICLXKHQZTFWNPYRGMEUAO", "JRCTHYKIGSXPOZLUQAVNEWFM", "NGMSWJITREHFZVQCUKXYAPOL",
    #                                     "WUXJOQKGNSYLHEZAFIPMRCVT", "PKYQIOLXFCRGHZNAMJVUTWES", "FERSGNMJVZXWAYLIKCPUQHTO", "HPLRIUQMTSGYJVAXWNOCZEKF", "JUVWPTEGCOFYSKXNRMHQALIZ", "MWPIAZCNSLEYRTHFKQXUOVGJ", "EZXLUNFVCMORSIWKTYHJAQPG", "HRQNLTKJFIEGMCSXAZPYOVUW", "LOHXVYGWRIJMCPSQENUAKTZF", "XKUTWPRGHOAQFLVYMJSNEIZC", "WTCRQMVKPHOSLGAXZUEFYNJI"]), "VWFHSJARNPEMOXLTUKICZGYQ")


if __name__ == "__main__":
    unittest.main()
