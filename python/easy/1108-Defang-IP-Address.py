class Solution:
    def defangIPaddr(self, address: str) -> str:

        a = address.split(".")
        f = "[.]"
        defang = (a[0] + f + a[1] + f + a[2] + f + a[3])
        return defang
