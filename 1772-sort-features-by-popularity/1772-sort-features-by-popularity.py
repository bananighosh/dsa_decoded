class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:

        res = []
        feat = set(features)
        m_feat = Counter(features)
        
        for response in responses:
            curr = set(response.split(" "))
            for word in (feat & curr):
                m_feat[word] += 1
        
        features.sort(key=lambda word: m_feat[word], reverse=True)

        return features

        