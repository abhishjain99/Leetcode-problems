class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            t = "".join(sorted(s))
            hash_map[t].append(s)
        return list(hash_map.values())